import jwt
from django.conf import settings
import datetime

def create_token(payload, exp=10):
    secret = settings.SECRET_KEY
    expiry = datetime.datetime.timestamp(datetime.datetime.now()+datetime.timedelta(seconds=exp))
    # options = {"course": "EDU4101", "exp": int(expiry)}
    payload['exp'] = int(expiry)
    ALG = "HS256"
    token = jwt.encode(payload, secret, algorithm=ALG)
    return token

def check_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        course, exp = payload['course'], payload['exp']

    except (ValueError, jwt.DecodeError, jwt.ExpiredSignatureError):
        return False, None


    return True, course