import streamlit as st

from PIL import Image                     #PIL is pillow library    #Image is class/type


with st.expander("Upload Image"):               #this expander method works like a button so that our browser
                                                # wait till we give permission to file uploader

     uploaded_image = st.file_uploader("Upload Image")            #file_uploader method for uploading file

if uploaded_image:                                             #we do not need if here but ok
    #created pillow(PIL) image instances
    img = Image.open(uploaded_image)                          #Image needs open method and open method needs camera image

    #converted image to grayscale(b/w)
    gray_img = img.convert("L")                     #L is grayscale algo(notation)

    st.image(gray_img)                             #st.image is rendering image to grayscale