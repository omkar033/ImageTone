import streamlit as st
import base64
st.set_page_config(
    page_title="Multipage App",
    page_icon=" ",
)
with open('llm.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.title(" :grey[About us]")

st.write("Welcome to ImageTone, the leading platform for transforming images into captivating audio experiences. At ImageTone, we are passionate about combining visual artistry with auditory creativity, empowering individuals and businesses to express themselves in unique and innovative ways.")
st.divider()
st.markdown("Our Mission")
st.divider()
st.write("Our mission at ImageTone is to provide a seamless and intuitive platform for converting images into high-quality audio, enabling users to unleash their creativity and explore new dimensions of storytelling and expression.")
st.divider()
st.markdown("What We Offer")
st.divider()
st.write("Advanced Conversion Technology: We utilize cutting-edge algorithms and technologies to ensure accurate and high-fidelity conversion of images to audio, delivering exceptional results every time.")
st.write("Versatility and Compatibility: Our converter supports a wide range of image formats, making it easy for users to transform their artwork, photographs, and designs into immersive soundscapes.")
st.write("Customization Options: Tailor the audio output to suit your preferences with customizable settings such as audio format, bitrate, and sound effects, allowing for a personalized audio experience.")
st.write("Fast and Efficient Processing: Experience quick and efficient conversion times, so you can focus on unleashing your creativity without delays or interruptions.")


st.divider()
st.write("Thank you for choosing ImageTone for your image to audio conversion needs. We look forward to helping you bring your vision to life through the power of sound and imagery!!")