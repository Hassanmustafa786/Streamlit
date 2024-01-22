import streamlit as st

output = "آپ کا جواب صحیح ہے"
message = f"{output} <br> براہ مہربانی دوسرے سوال کی طرف جائیں۔"

# Using st.markdown to include an emoji
st.markdown(f'<div style="font-size: x-large; color: orange;"> {message}</div>', unsafe_allow_html=True)
