from flask import Flask
import redis
import os

app = Flask(__name__)
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
r = redis.from_url(redis_url, decode_responses=True)

@app.route("/")
def hello():
    try:
        count = r.incr("hits")
        return f"Hello DevOps. Visits: {count}\n"
    except Exception as e:
        return f"Redis Error: {str(e)}"

# זה הסעיף החדש (3)
@app.route("/health")
@app.route("/health")
def health():
    return "OK", 200
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
