from flask import Flask,render_template
import pandas as pd
#commit: add app fn using loc,series and df,query Sec30

app=Flask(__name__)

df=pd.read_csv('dictionary.csv') #load csv in df

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route('/api/v1/<word>/')
def api(word):
    # this uses the df.loc!!!
    def_series=df.loc[df['word']==word]['definition'] #this returns a series
    if def_series.empty: #check if the series is empty
        definition=''
    else:
        definition=def_series.squeeze()
    result_dict={'definition':definition,'word':word} #form dict/json to return
    return(result_dict)

@app.route('/api/v2/<word>/')
def translate(word):
    # this uses the df.query() method!!!
    def_df=df.query(f'word=="{word}"') #query df and returns a df!!!
    # df.query already returns all results concatenated, so no need to iterate!!!
    # def_df.isnull() #this checks for empty and puts bool in each cell is DF!!!
    if def_df['definition'].empty: # check if cell is empty in the df!!!
        definition=''
    else:
        definition=f"{def_df['definition'].squeeze()}"
    result_dict={'definition':definition,'word':word} #form dict/json to return
    return(result_dict)

if __name__=='__main__':
    app.run(debug=True,port=5001)