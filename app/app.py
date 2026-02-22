from flask import Flask
import redis
import os

app = Flask(__name__)

# קריאת כתובת ה-Redis ממשתנה הסביבה שהגדרנו ב-Render
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")

# התחברות ל-Redis עם תמיכה בחיבור מאובטח (SSL)
r = redis.from_url(redis_url, decode_responses=True, ssl_cert_reqs=None)

@app.route("/")
def hello():
    try:
        count = r.incr("hits")
        return f"Hello DevOps. Visits: {count}\n"
    except Exception as e:
        return f"Error connecting to Redis: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
