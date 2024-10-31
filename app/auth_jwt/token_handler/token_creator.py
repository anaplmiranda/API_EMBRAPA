import time
from datetime import datetime, timedelta
import jwt

class TokenCreator:

    def __init__(self, token_key: str, exp_time_min: int, refresh_time: int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time_min
        self.REFRESH_TIME_MIN = refresh_time

    def create(self, uid: int) -> str:    
        return self.__encode_token(uid=uid)
    
    def refresh(self, token: str) -> str:
        token_information = jwt.decode(token, key=self.__TOKEN_KEY, algorithms="HS256")
        uid = token_information['uid']
        exp_time = token_information['exp']

        if ((exp_time - time.time()) / 60) < self.REFRESH_TIME_MIN:
            return self.__encode_token(uid=uid)
        
        return token    

    def __encode_token(self, uid:int):    
        return jwt.encode({
            'uid': uid,
            'exp': datetime.utcnow() + timedelta(minutes=self.__EXP_TIME_MIN)
        }, key=self.__TOKEN_KEY, algorithm="HS256")