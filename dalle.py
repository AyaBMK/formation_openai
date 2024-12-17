import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

prompt = st.text_input("Entrez une description pour générer une image avec DALL-E ")

# client.images.create_variation(
#     model="dall-e-3",
#     prompt=prompt,
#     size="1024x1024"
# )
#   def openai_create_image_variation(self, data, model="dall-e-2"):
#         return self._client.images.create_variation(
#             model=model,
#             image=data,
#             n=1,
#             size="1024x1024",
#             ).data[0].url

if st.button("Générer l'image"):
    if prompt:
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024"
            )
            image_url = response.data[0].url
            st.image(image_url, caption="Image générée par DALL-E", use_container_width=True)
        except Exception as e:
            st.error(f"Erreur: {e}")
    else:
        st.warning("Veuillez entrer une description pour générer une image.")
