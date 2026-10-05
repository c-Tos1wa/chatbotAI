import streamlit as st
from openai import OpenAI
import os

model_ai = OpenAI(
    api_key = os.environ['API_KEY'],
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
)

st.write("## Criando um chatbot com IA Generativa")

# session state : para manter um histórico das mesagens passadas ao streamlit
if not "mensagens" in st.session_state:
    st.session_state["mensagens"] = []
    
for prompt in st.session_state["mensagens"]:
    role = prompt["role"]
    content = prompt["content"]
    st.chat_message(role).write(content)

user_prompt = st.chat_input("Tire sua dúvida aqui")

if user_prompt:
    st.chat_message("user").write(user_prompt)
    mensagem = {
        "role": "user",
        "content": user_prompt
    }
    st.session_state["mensagens"].append(mensagem)
    
    model_response = model_ai.chat.completions.create(
        messages = st.session_state["mensagens"],
        model = "gemini-flash-lite-latest"
    )
    #print(model_response)
    
    ai_response = model_response.choices[0].message.content
    
    st.chat_message("assistant").write(ai_response)
    mensagem_ia = {
        "role": "assistant",
        "content": ai_response 
    }
    st.session_state["mensagens"].append(mensagem_ia)
    
    