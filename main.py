import streamlit as st
import time

st.title("Streamlit 超入門")
st.write("Start!!")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(10):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

expander = st.expander("問い合わせ")
text = expander.text_input("問い合わせ内容をどうぞ")
st.write("test_inputの内容：", text)



option = st.text_input('あなたの趣味を教えてください')
'あなたの好きな数字は', option, 'です'


condition = st.slider('あなたの今の調子は？' ,0,100,50)
'コンディション：',condition

