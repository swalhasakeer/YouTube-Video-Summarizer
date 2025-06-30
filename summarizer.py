# summarizer.py

import re
import os
import webvtt
import yt_dlp as youtube_dl
import pandas as pd
import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def get_caption(url):
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'outtmpl': 'test.%(ext)s',
        'nooverwrites': False,
        'quiet': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'video_summary')
        except Exception as e:
            raise RuntimeError("Error downloading subtitles: " + str(e))

    corpus = []
    for caption in webvtt.read('test.en.vtt'):
        corpus.append(caption.text)

    full_text = " ".join(corpus).replace('\n', ' ')
    return full_text, video_title


def summarizer(text, option, fraction=0.3):
    if option == "TfIdf-Based":
        return tfidf_based(text, fraction)
    elif option == "Frequency-Based":
        return freq_based(text, fraction)
    elif option == "Spacy-Based":
        return spacy_based(text, fraction)
    else:
        return "Invalid summarization option."


def tfidf_based(text, fraction=0.3):
    doc = nlp(text)
    sents = [sent.text for sent in doc.sents]
    num_sent = int(np.ceil(len(sents) * fraction))

    tfidf = TfidfVectorizer(stop_words='english', token_pattern='(?ui)\\b\\w*[a-z]+\\w*\\b')
    X = tfidf.fit_transform(sents)

    df = pd.DataFrame(data=X.todense(), columns=tfidf.get_feature_names_out())
    index_list = list(df.sum(axis=1).sort_values(ascending=False).index)

    selected = sorted(index_list[:num_sent])
    summary = " ".join([sents[i] for i in selected])
    return summary.replace("\n", "")


def freq_based(text, fraction=0.3):
    doc = nlp(text)
    sents = list(doc.sents)
    num_sent = int(np.ceil(len(sents) * fraction))

    words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    freq = Counter(words)
    max_freq = max(freq.values())

    word_weights = {word: round(count / max_freq, 3) for word, count in freq.items()}
    
    sent_weights = []
    for sent in sents:
        weight = sum(word_weights.get(token.text.lower(), 0) for token in sent)
        sent_weights.append(weight)

    top_indices = np.argsort(sent_weights)[-num_sent:]
    top_indices.sort()
    
    summary = " ".join([sents[i].text.strip() for i in top_indices])
    return summary


def spacy_based(text, fraction=0.3):
    doc = nlp(text)
    sents = list(doc.sents)
    num_sent = int(np.ceil(len(sents) * fraction))

    words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    word_freq = Counter(words)
    max_freq = max(word_freq.values())
    word_weights = {word: freq / max_freq for word, freq in word_freq.items()}

    sent_scores = []
    for sent in sents:
        score = sum(word_weights.get(token.text.lower(), 0) for token in sent if not token.is_stop)
        sent_scores.append(score)

    best_sent_indices = np.argsort(sent_scores)[-num_sent:]
    best_sent_indices.sort()

    summary = " ".join(sents[i].text.strip() for i in best_sent_indices)
    return summary
