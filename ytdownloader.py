from pytube import YouTube
import streamlit as st
import pandas as pd
import base64
from io import BytesIO

def main():
    link = st.text_input("Masukkan URL Youtube")
    option = st.selectbox(
     'Select type of download',
     ('audio', 'highest_resolution', 'lowest_resolution'))

    matches = ['audio', 'highest_resolution', 'lowest_resolution']
    if st.button("download"):
        yt = YouTube(link)
        st.write("Judul :", yt.title)
        st.write("Total Tayangan :", yt.views)
        if option == 'audio':
            yt.streams.get_audio_only().download() 
        elif option == 'highest_resolution':
            yt.streams.get_highest_resolution().download()
        elif option == 'lowest_resolution':
            yt.streams.get_highest_resolution().download()


        # Muat file ke dalam memori
        file_data = BytesIO()
        yt.download(output_stream=file_data)

        # Unduh file dari memori ke disk
        st.download_file(file_data.getvalue(), f"{yt.title}.mp4")

    if st.button("view"):
        st.video(link)

if __name__=='__main__':
    main()
