from flask import Flask, render_template, request
from summarizer import get_caption, summarizer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    title = ""
    if request.method == "POST":
        url = request.form.get("url")
        method = request.form.get("method")  # SAFELY get method
        try:
            full_text, title = get_caption(url)
            summary = summarizer(full_text, method)
        except Exception as e:
            summary = f"Error: {str(e)}"
    return render_template("index.html", summary=summary, title=title)


if __name__ == "__main__":
    app.run(debug=True)
