import pandas as pd
# scratch pad for sec31 st proj


df=pd.read_csv('tmp/wines.csv')
len=len(df.loc[df['points']==100]['points'])
print(len)
max=df.loc[df['price']==df['price'].max(skipna=True)]
df.loc[df['price']<100]['price'].hist()
df.plot(x='price',y='points',kind='scatter')