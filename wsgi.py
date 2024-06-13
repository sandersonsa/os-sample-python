from flask import Flask
from flask import request
application = Flask(__name__)

@application.route("/")
def hello():
    print(request.headers)  
    return "Hello World!"

if __name__ == "__main__":
    application.run( host='0.0.0.0', port=8080 )
