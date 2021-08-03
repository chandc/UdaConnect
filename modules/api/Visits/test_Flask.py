from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route("/test",  methods = ['POST'])
def hello():
    print(request.get_json())
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == "__main__":
    app.run()