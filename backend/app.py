from flask import Flask

app = Flask(__name__)

@app.route("/api/ping")
def ping():
    print("收到前端访问请求")
    return {
        "status": "ok",
        "version": "v2"
    }

if __name__ == "__main__":
    print("CI/CD Test v2")
    app.run(host="0.0.0.0", port=5000)