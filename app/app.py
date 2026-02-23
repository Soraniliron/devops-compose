from flask import Flask
import redis
import os

app = Flask(__name__)

# קריאת הכתובת. אם אין כתובת, הוא ינסה localhost
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")

# חיבור בסיסי ביותר
r = redis.from_url(redis_url, decode_responses=True)

@app.route("/")
def hello():
    try:
        # בדיקה אם החיבור עובד
        count = r.incr("hits")
        return f"Hello DevOps. Visits: {count}\n"
    except Exception as e:
        # אם יש שגיאה, היא תודפס ישירות לדפדפן כדי שנראה אותה
        return f"Redis Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
