import streamlit as st
import pandas

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

col3, col4 = st.columns(2)
df = pandas.read_csv("data_pf.csv",sep=";")
with col3:
    for index, row in df.iterrows():
        if index/2 == 0:
            st.header(row['title'])
            st.write(row['description'])
            st.info(f"Website: {row['url']}")
            st.image(f"images/{index+1}.png")

with col4:
    for index, row in df.iterrows():
        if index/2 != 0:
            st.header(row['title'])
            st.write(row['description'])
            st.info(f"Website: {row['url']}")
            image_path = f"images/{index+1}.png"
            st.image(image_path)
