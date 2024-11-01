import streamlit as st
with open('llm.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
st.title(":grey[How To Use!!?]")
st.divider()
st.write("Note: image should not contain any pictures or videos because they cant be converted to text make sure the image you want to convert has plain texts only")
st.divider()
st.write("Step 1: Click on browse and search for the image you want to convert.")
st.divider()
st.write("Step 2: Read the extracted text once. If entire text is not extracted from image refresh and reload the image")
st.divider()
st.write("Step 3: Select the Language You want to convert into.")
st.divider()
st.write("Step 4: An audio bar will appear with play button.")
st.write("And Done!!!")
st.divider()
st.write("We have successfully converted and image to audio in preferable Language.... ")
