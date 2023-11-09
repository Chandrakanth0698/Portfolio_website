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
df = pandas.read_csv("data_pf.csv", sep=";")
left_column = [i for i in range(0, 21, 2)]
right_column = [i for i in range(1, 21, 2)]
with col3:
    for index, row in df.iterrows():
        if index in left_column:
            st.header(row['title'])
            st.write(row['description'])
            st.info(f"Website: {row['url']}")
            st.image(f"images/{row['image']}")
            st.write(f"[Source code]({row['src']})")

with col4:
    for index, row in df.iterrows():
        if index in right_column:
            st.header(row['title'])
            st.write(row['description'])
            st.info(f"Website: {row['url']}")
            st.image(f"images/{row['image']}")
            st.write(f"[Source code]({row['src']})")
