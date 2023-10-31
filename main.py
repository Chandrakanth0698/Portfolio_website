import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/my_image.jpeg")

with col2:
    st.title("Chandrakanth Bogra")
    content = """ Hey there! 👋 I am a passionate Python developer with a 
    Master's in Computer Science.  
    🐍 I thrive on exploring the world of code and embrace challenges 
    like old friends. A fast learner? That's my middle name!
     (Well, not literally, but you get the drift.) 
     Let's embark on this digital journey together! 🚀
    """
    st.info(content )
st.write("Below you can find some of the apps i have built in python."
         " Feel free to contact me!")
