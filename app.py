import streamlit as st
from Facial_2 import main
def main_app():
    
    st.title("Facial Attendance")

    # Create a Streamlit column for the video and another for the table
    video_column, Alert_column = st.columns(2)

    # In the video column, display the camera feed and the "Start" button
    with video_column:
        start_button = st.button("Start")
        video = st.empty()

        if start_button:
            table_A=st.empty()
            main(video,table_A)
       

if __name__ == '__main__':
    main_app()
    




