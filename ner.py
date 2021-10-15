import fool
from flask import request
from flask import render_template
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from flask import Flask
app = Flask(__name__)


@app.route('/ner',methods=["GET", "POST"])
def ner():    
    text = request.args.get("text")
    print(text)
    output = fool.analysis([text])
    print(output)
    return json.dumps(output,ensure_ascii=False).encode("UTF-8")

@app.route('/',methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)