import jwt
import secrets

json = {
    "id": "justkode",
    "password": "password"
}

print(secrets.token_urlsafe(32))
str = secrets.token_urlsafe(32)

encoded = jwt.encode(json, str, algorithm="HS256")  # str
decoded = jwt.decode(encoded, str, algorithms="HS256")  # dict

print(encoded)
print(decoded)
