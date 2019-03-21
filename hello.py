# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)


@app.route("/")

def hello():
    while True:
        test = int(input("Command"))
        if test == 1:
        
        
            return start()
        elif test == 2:
            return stop()
        else:
            print("false")
            return "no"
if __name__ == "__main__":
    app.run()
while True:
    hello()
    
def start():
    return "started"
def stop():
    return "stop";