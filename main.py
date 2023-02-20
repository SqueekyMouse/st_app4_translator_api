from flask import Flask,render_template
import pandas as pd
#commit: updated port and url Sec29

app=Flask(__name__)

df=pd.read_csv('dictionary.csv') #load csv in df

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route('/api/vi/<word>/')
def translate(word):
    definition=''

    def_df=df.query(f'word=="{word}"') #query df and get result df
    for index,row in def_df.iterrows(): #get definitions fron the df
        definition=f"{definition}{row['definition']}\n"
    
    result_dict={'definition':definition,'word':word} #form dict/json to return
    return(result_dict)

if __name__=='__main__':
    app.run(debug=True,port=5001)