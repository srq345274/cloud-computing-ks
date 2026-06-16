from flask import Flask
import redis
import os
app=Flask(__name__)
rh=os.getenv("REDIS_HOST")
rp=os.getenv("REDIS_PORT")
rpwd=os.getenv("REDIS_PASSWORD","")
rd=redis.Redis(host=rh,port=int(rp),password=rpwd,decode_responses=True)

@app.route("/api/ping")
def ping():
    print("收到前端访问请求")
    return {"status":"ok"}

if __name__=="__main__":
app.run(host="0.0.0.0",port=5000)
