from google.auth.transport import requests
from google.oauth2 import id_token
from google.auth.transport import requests
import secrets

class GoogleUserData:
    def __init__(
        self, email=None, name=None, picture=None, *args, **kwrds
    ) -> None:
        self.email = email
        self.name = name
        self.picture = picture


def validateToken(access_token):
    request = requests.Request()

    resp = id_token.verify_oauth2_token(access_token, request)
    if "https://accounts.google.com" in resp["iss"]:
        return  GoogleUserData(**resp)


def generate_random_password(length=16):
    # Generate a secure random hex string and convert it to uppercase
    password = secrets.token_hex(length // 2).upper()
    return password