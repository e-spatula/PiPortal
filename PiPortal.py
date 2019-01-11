"""
@author: Eddie Atkinson
@version: 0.1
@date: 07/01/18

"""
from flask import Flask, request, jsonify
import requests
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
cardURL = "https://auth.uwamakekers.com/api/card"
token = config["setup"]["token"]

"""
Method that takes the uid string provided by the ESP, strips it of the 
extra formatting added by the ESP and converts the hexadecimal string to an array 
of 4 digits. 

For example the uid string b'04050607' becomes:
0405060708
which becomes:
[4,5,6,7]
"""
def uidSplitter(uid):
    uid = str(uid)
    uid = uid.replace("b'", "").replace("'", "")
    if(len(uid) != 8):
        print("UID length is wrong")
        return(-1)
    byteArray = []
    for i in range(1,8,2):
        byte = int(uid[i-1 : i+1], 16)
        byteArray.append(byte)
    return(byteArray)