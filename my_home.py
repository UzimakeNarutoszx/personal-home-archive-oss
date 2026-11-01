import streamlit as st
from PIL import Image

def change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

st.title("图片通道实验")
upload = st.file_uploader("选择测试图片", type=["png", "jpg", "jpeg"])
if upload:
    image = Image.open(upload).convert("RGB")
    st.image(image, caption="原图")
    st.image(change(image.copy(), 2, 1, 0), caption="红蓝通道交换")
