import streamlit as st

from PIL import Image                     #PIL is pillow library    #Image is class/type


with st.expander("Start Camera"):               #this expander method works like a button so that our browser
                                                # wait till we give permission to camera

    camera_image = st.camera_input("camera")

if camera_image:                                 #to not get none type error that is when we run the code,
                                                # it quickly opens camera but our laptop is asking us for permission ,
                                                #if camera_image is now something than 'none'
    #created pillow(PIL) image instances
    img = Image.open(camera_image)                    #Image needs open method and open method needs camera image

    #converted image to grayscale(b/w)
    gray_img = img.convert("L")                     #L is grayscale algo(notation)

    st.image(gray_img)                             #st.image is rendering image to grayscale