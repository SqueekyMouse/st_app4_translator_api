import pandas as pd

word='sun'
df=pd.read_csv('dictionary.csv')
# definition=df['definition'].where(df['word'] == word) 
def_df=df.query(f'word=="{word}"')
definition=''

for index,row in def_df[0:].iterrows():
    definition=f"{row['definition']}\n"
    # print(row['definition'])

print(f"Definition: {definition}\nWord:{word}")