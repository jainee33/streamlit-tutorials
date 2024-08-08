import streamlit as st 

st.write("Hello World:Getting Bore, Hello Brother!!")
st.title("Display Title use st.title()")
st.write("To write text use st.write()")
st.header("I am header to write header use st.header use st.header()")
st.subheader("I am subheader To write subheader use st.subheader()")
st.text("Hey I am simple text to write simple text use st.text")
# To create hyperlink
st.markdown("[Streamlit](https://share.streamlit.io/)")
st.markdown("[Streamlit CheatSheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)")
st.success("Success!")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error!")

from PIL import Image
img=Image.open("smj.jpg")
st.image(img, width=300, caption="Satyamev Jayte")

video_file=open("vid.mp4","rb")
video_bytes=video_file.read()
st.video(video_bytes)

st.video("https://youtu.be/kYcu17Eci0A?si=LGr_pAEoPP4Pcl3F")
audio_file = open("song.mp3","rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

st.button("Play")

st.header("Button Widgets")
if st.button("Play2"):
	st.text("Enjoy Music")
	st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")
    
if st.checkbox("Checkbox"):
    st.text("Checkbox selected")