import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPEN_API_KEY")
client = OpenAI(api_key=key)

def generate_article(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "user", "content": f"Écrivez un article sur le thème suivant : {prompt}"}
        ]
    )
    
    return completion.choices[0].message.content

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",  
        prompt=prompt,
        size="1024x1024"
    )
    
    return response.data[0].url

prompt = st.text_input("Entrez un sujet")

if st.button("Générer"):
    if prompt:
        try:
            article = generate_article(prompt)
            st.header(f"Article sur : {prompt}")
            st.write(article)
        except Exception as e:
            st.error(f"Erreur: {e}")

        try:
            image_url = generate_image(prompt)
            st.header("Image générée par DALL-E")
            st.image(image_url, caption="Image générée par DALL-E", use_container_width=True)
        except Exception as e:
            st.error(f"Erreur: {e}")
    else:
        st.warning("Veuillez entrer un sujet pour générer un article et une image")



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