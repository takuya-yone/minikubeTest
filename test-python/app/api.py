from fastapi import FastAPI, Response
import hashlib
import datetime
import jwt
import redis

app = FastAPI()

@app.get('/') 
async def hello(response: Response):
    return {"text": "hello world!"}

@app.get('/set_cookie') 
async def set_cookie(response: Response):
    # define value
    user='user01'
    unixtime = datetime.datetime.now().strftime('%s')
    cookie = jwt.encode({'user':user ,'unixtime':unixtime}, 'secret', algorithm='HS256')
    # set cookie to redis
    redis_cli = redis.Redis(host='redis-service', port=6379, db=0)
    redis_cli.set(user, cookie)
    # set cookie to response
    response.set_cookie('mycookie', cookie)
    return {"cookie setted!": cookie}

@app.get('/get_cookie') 
async def get_cookie(response: Response):
    # define value
    user='user01'
    # get cookie from redis
    redis_cli = redis.Redis(host='redis-service', port=6379, db=0)
    cookie = redis_cli.get(user)
    # return cookie from redis
    return {"cookie getted!":cookie.decode()}

@app.get('/json') 
async def hello():
    return {"text": "Json!"}

@app.get('/api') 
async def hello():
    return {"text": "APIAPIAPI!"}