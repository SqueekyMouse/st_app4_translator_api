from flask import Flask,render_template
import pandas as pd
#commit: df search api implemented Sec29
# commit: html updated Sec29

app=Flask(__name__)

df=pd.read_csv('dictionary.csv')

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route('/api/vi/<word>')
def translate(word):
    definition=''

    def_df=df.query(f'word=="{word}"')
    for index,row in def_df[0:].iterrows():
        definition=f"{definition}{row['definition']}\n"

    return({'definition':definition,
            'word':word})

if __name__=='__main__':
    app.run(debug=True)