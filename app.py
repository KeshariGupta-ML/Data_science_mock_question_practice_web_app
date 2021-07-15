import time

from flask import Flask,render_template,jsonify
import pandas as pd
import numpy as np
import warnings
# warnings.filterwarnings(action="ignore")
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
        if df.iloc[rand_int,1] is np.nan:
            resp = {"result": df.iloc[rand_int, 0],"ans":"Not Answered Yet!!"}
        else:
            resp={"result":df.iloc[rand_int,0],"ans":df.iloc[rand_int,1]}
        time.sleep(1)
        # print(resp)
        return jsonify(resp),200
    else:
        rand_int = np.random.randint(1, len(df2))
        # print(df2.iloc[rand_int, 0].split(r"\t")[1].strip())
        resp = {"result": df2.iloc[rand_int, 0].split(r"\t")[0],"ans":df2.iloc[rand_int, 0].split(r"\t")[1].strip(" )(")}
        time.sleep(1)
        # print(resp)
        return jsonify(resp), 200

if __name__=="__main__":
    app.run("localhost","2100",debug=True)
    # app.run()