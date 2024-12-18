from openai import OpenAI
import streamlit as st
 
client = OpenAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

def new_message(content: str):
    with (st.chat_message("user")):
        st.session_state.messages.append({"role":"user", "content": content})
        st.write(content)

    with (st.chat_message("assistant")):
        field = st.text("waiting for an answer...")
    
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user","content": content}
        ]
        )
        
        st.session_state.messages.append({"role": "assistant", "content": completion.choices[0].message.content})
        field.text(completion.choices[0].message.content)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.text(message["content"])
value = st.chat_input("Say something")
if (value and value != ""):
    new_message(value)
    value = ""

# import streamlit as st

# path = "root/pages/"
# pg = st.navigation([
#         st.Page(path + "Home.py", icon=":material/home:"), 
#         st.Page(path + "NLP.py", title="1. Natural Language Processing (NLP)"),
#         st.Page(path + "OpenAI.py", title="2. API OpenAI"), 
#         st.Page(path + "DALL-E.py", title="3. API DALL-E 2"),

#         st.Page(path + "Whisper.py", title="4. Whisper"),
#         st.Page(path + "Fine-tuning.py", title="5. Fine-tuning"),
#         st.Page(path + "Exercise.py", title="6. Exercice final"),
#     ]) 
# pg.run()

