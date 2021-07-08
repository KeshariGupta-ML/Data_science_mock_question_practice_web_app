import time

from flask import Flask,render_template,jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)
df=pd.read_csv("assets/mock_interview_questions.csv",header=0)
df2=pd.read_csv("assets/AppliedAI_revision.csv",header=0)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/get_question/<int:_type>",methods=["GET"])
def get_question(_type):
    if not _type:
        rand_int=np.random.randint(1,len(df))
        resp={"result":df.iloc[rand_int,0]}
        time.sleep(1)
        return jsonify(resp),200
    else:
        rand_int = np.random.randint(1, len(df2))
        resp = {"result": df2.iloc[rand_int, 0].split(r"\t")[0]}
        time.sleep(1)
        return jsonify(resp), 200

if __name__=="__main__":
    app.run("localhost","2100",debug=True)