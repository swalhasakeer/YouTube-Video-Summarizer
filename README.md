# 🎬 YouTube Video Summarizer

A web application that extracts and summarizes the **automatic subtitles** from any public YouTube video using powerful NLP techniques like **TF-IDF**, **Word Frequency**, and **SpaCy**. Built with **Flask**, it provides an elegant interface to choose summarization methods and download the result.


## 🚀 Features

- 🎥 Extracts subtitles directly from YouTube video links
- 🧠 Provides 3 summarization methods:
  - TF-IDF Based
  - Word Frequency Based
  - SpaCy-Based
- 📋 Displays clean and readable summaries
- 💾 Allows downloading summaries as `.txt`
- 🎨 Beautiful UI with glassmorphism + gradients
- 📱 Mobile responsive design
- 🔄 Loading spinner during processing

---

## 🛠️ Tech Stack

| Frontend  | Backend   | NLP Libraries |
|-----------|-----------|---------------|
| HTML5 + CSS3 | Flask (Python) | spaCy, scikit-learn, numpy |
|               | yt_dlp | pandas |

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/swalhasakeer/YouTube-Video-Summarizer.git
   cd YouTube-Video-Summarizer
   ```

2. **Create a virtual environment (optional but recommended)**

```bash

python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate     # For Windows
```

3. **Install dependencies**

```bash

pip install -r requirements.txt
```

4. **Download spaCy model**

```bash

python -m spacy download en_core_web_sm
```

---

## ▶️ Usage
1. **Start the Flask server**

```bash

python app.py
```

2. **Open in browser**

 Navigate to: http://localhost:5000

3. **Paste a YouTube URL**, choose a summarization method, and click **"Generate Summary"**.


---


## 📸 Demo Preview

![Demo](https://github.com/user-attachments/assets/892db2e4-d6f1-4832-b8c4-bfd171862ece)


---
## 📁 Folder Structure

```bash

📂 youtube-video-summarizer/
├── app.py
├── summarizer.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

---


## 🤝 Contributing

Contributions are welcome! Feel free to submit issues, fork the repo and send pull requests.
