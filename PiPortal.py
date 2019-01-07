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
