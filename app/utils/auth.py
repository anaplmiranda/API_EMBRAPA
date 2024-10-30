from app import auth

USERS ={
    "admin":"secret",
    "user":"password"
}

"""
Verifies the username and password for basic authentication.

Parameters:
username (str): The username provided by the client.
password (str): The password provided by the client.

Returns:
str: The username if the credentials are valid, otherwise None.
"""

@auth.verify_password
def verify_password(username, password):
    if username in USERS and USERS[username] == password:
        return username
    return None