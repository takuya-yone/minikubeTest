from fastapi import FastAPI, Response
import hashlib
import datetime
import jwt
import redis
import logging
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger(__name__)
logger.info("Hello, World!")


app = FastAPI()

# logger
# logger = getLogger(__name__)
# handler = StreamHandler()
# handler.setLevel(DEBUG)
# logger.setLevel(DEBUG)
# logger.addHandler(handler)
# logger.propagate = False

# console
# console = Console()

@app.get('/') 
async def hello(response: Response):
    logger.debug('----xxxx-----')
    logger.debug('----aiueo-----')
    logger.error("error!!!")
    logger.critical("critical...")
    # console.log(logger)

    # print('hello')
    return {"text": "root!!!!"}
@app.get('/api/') 
async def hello(response: Response):
    return {"text": "helleo world!"}

@app.get('/api/set_cookie') 
async def set_cookie(response: Response):
    # define value
    user='user01'
    unixtime = datetime.datetime.now().strftime('%s')
    cookie = jwt.encode({'user':user ,'unixtime':unixtime}, 'secret', algorithm='HS256')
    # set cookie to redis
    # redis_cli = redis.Redis(host='redis-service', port=6379, db=0)
    # redis_cli.set(user, cookie)
    # set cookie to response
    response.set_cookie('mycookie', cookie)
    return {"cookie setted!": cookie}

@app.get('/api/get_cookie') 
async def get_cookie(response: Response):
    # define value
    user='user01'
    # get cookie from redis
    # redis_cli = redis.Redis(host='redis-service', port=6379, db=0)
    # cookie = redis_cli.get(user)
    # return cookie from redis
    return {"cookie getted!":cookie.decode()}

@app.get('/api/json') 
async def hello():
    return {"text": "Json!"}

@app.get('/api/api') 
async def hello():
    return {"text": "APIAPIAPI!"}