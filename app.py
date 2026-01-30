import streamlit as st
import pandas as pd

st.title('都道府県別にみた年別死亡数')

df = pd.read_csv('people.csv', encoding='cp932')

# 縦長に変換
df_long = df.melt(
    id_vars='都道府県',
    var_name='年',
    value_name='死亡数')

df_long['年'] = df_long['年'].astype(int)

# 年のリスト
years = sorted(df_long['年'].unique())


with st.sidebar:
    branch = st.multiselect('都道府県を選択してください（複数選択可）',
                            df['都道府県'].unique())
    
    year = st.selectbox('表示する年を選択してください',
                    years)

    year_range = st.slider(label='年を選択してください',
                        min_value= 1975,
                        max_value= 2024,
                        value=(1990, 2015) )
    
    range_mode = st.checkbox('年の推移を表示する')


df = df_long.copy()

df = df[df['都道府県'].isin(branch)]
df = df[df['年'] == year]

df.drop('年', axis=1, inplace=True)
df.set_index('都道府県', inplace=True)

st.subheader(f'{year}年 都道府県別死亡数')
st.dataframe(df, width=800, height=200)
st.bar_chart(df)

df2 = df_long.copy
df2 =  df_long[df_long['都道府県'].isin(branch)]
df2 = df2[(df2['年'] >= year_range[0]) &
            (df2['年'] <= year_range[1])]

st.dataframe(df2, width=800, height=200)
st.line_chart(df2)