from instagrapi import Client
from time import sleep
import sys

cl = Client()

with open('list.txt') as f:
    lines = f.readlines()

for line in lines:
    userpass = False

    user = ""
    password = ""

    for letter in line:
        if letter != ":":
            if not userpass:
                user += letter
            else:
                password += letter
        else: 
            userpass = True
    try:
        if cl.login(user, password):
            print("login to " + user + " was successful")
    except:
            print("login to " + user + " was unsuccessful")
