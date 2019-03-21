from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello():
    
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

def start():
    return "started"
def stop():
    return "stop";
