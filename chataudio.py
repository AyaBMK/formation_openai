from openai import OpenAI
import streamlit as st
from pathlib import Path

client = OpenAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

def new_message(content: str):
    with st.chat_message("user"):
        st.session_state.messages.append({"role": "user", "content": content})
        st.write(content)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.text("Waiting for an answer...")

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": content}
            ]
        )
        
        response = completion.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": response})
        placeholder.text(response)

        file_path = Path(__file__).parent / "output.mp3"
        tts_response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=response
        )
        tts_response.stream_to_file(file_path)

        st.audio(file_path)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.text(message["content"])

audio = st.audio_input("Dites quelque chose")
if audio:
    file_path = Path(__file__).parent / "input.mp3"

    with open(file_path, "wb") as file:
        file.write(audio.getbuffer())

    with open(file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=file
        )
        user_input = transcription.text
        st.write(f"Vous avez dit : {user_input}")

        new_message(user_input)
