from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "AIzaSyByAysbdqAj7sxIIP1fcjKU6swc34A3uTE")
    # TODO: Replace mock data with real YouTube API search
    results = [
        {"id": "x1", "title": "Funny Cat Video", "description": "A very funny cat!", "thumbnail": "https://example.com/cat.jpg"},
        {"id": "x2", "title": "Amazing Dog Tricks", "description": "A clever dog.", "thumbnail": "https://example.com/dog.jpg"}
    ]
    return jsonify({"results": results})

@app.route("/watch")
def watch():
    video_id = request.args.get("id", "")
    # TODO: Replace mock link with real YouTube direct stream link (MP4/3GP)
    video_url = "https://example.com/video.mp4"
    return jsonify({"url": video_url})

if __name__ == "__main__":
    app.run(debug=True)
