import streamlit as st

# アプリタイトル
st.title("Hello World App")

# ボタンを表示
if st.button("押してください"):
    # ボタンが押されたら表示
    st.write("Hello World")
