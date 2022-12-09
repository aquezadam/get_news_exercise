# REGISTRATION : name, email, password, id(code pact)
# user_details -> credentials -> documents_of_user{"Name": name, "Email":email, "Password":password after hashing? }
# ------ shark 256 - convert passwords into hascode for enscrtiptin, stored in hex and cannot be reversed
# Check for existence of registered user
import hashlib
import uuid #  generates id fro mongo
import pymongo
import certifi  # ensure secure connectio
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://aqm:abcd1234@20221207test.xeknavy.mongodb.net/?retryWrites=true&w=majority",
                             tlsCAFile=certifi.where())
db = client["User_details"]
collection_a = db["Registration"]


def user_registration(name, email, password):
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    user_details = {"id": uuid.uuid4().hex, "Name": name, "Email": email, "Password": hashed_password}
    # print(email)
    user = collection_a.find_one({"Email": email})
    # print(user)
    if user:
        return "User already exists"
    else:
        collection_a.insert_one(user_details)
        return"Successful registration"
## LOGIN - collect email and password from the user.
# search for email using .find({}). Is email exists, check if
# if hashed password given by user == password in the database -> success
# if email exists but the hashed password do no match -> not successful
# if email does not exists - no uset found


def login(email, password):
    user_check = collection_a.find_one({"Email": email})  # fin_one will return value
    if user_check:
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        if user_check["Password"] == hashed_password:
            return "success"
        else:
            return "wrong password"
    else:
        return "No user found with these credentials. Try again."


def change_password(email, new_password):
    """
    1)find user with this email and
    2)update this user password with the new password
    """
    email_confirm = collection_a.find_one({"Email": email})
    if email_confirm:
        new_hashed_password = hashlib.sha256(new_password.encode("utf-8")).hexdigest()
        collection_a.update_one({"Email": email}, {'$set': {'Password': new_hashed_password}})
    return "You have a new password"

