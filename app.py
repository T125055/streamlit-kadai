import streamlit as st
import pandas as pd

st.title('自然公園の公園数と年間利用者数')

df = pd.read_csv('park.csv')

df['年次'] = pd.to_numeric(df['年次'], errors='coerce')
df = df.dropna(subset=['年次'])
df['年次'] = df['年次'].astype(int)

with st.sidebar:
    branch = st.multiselect('公園分類を選択してください（複数選択可）',
                            df['公園分類'].unique())
    year = st.slider('年を選択してください',
                     min_value=int(df['年次'].min()),
                     max_value=int(df['年次'].max()),
                     value=int(df['年次'].min()),
                     step=1)
    
if branch:
    df = df[df['公園分類'].isin(branch)]

df = df[df['公園分類'].isin(branch)]
df = df[df['年次']==year]
df.drop('年次',axis=1,inplace=True)
df.set_index('公園分類',inplace=True)

st.dataframe(df, width=800, height=200)
st.line_chart(df)