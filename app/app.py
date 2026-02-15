from flask import Flask
import redis
import os

app = Flask(__name__)
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def hello():
    count = r.incr("hits")
    return f"Hello DevOps. Visits: {count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

