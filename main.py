from projetchatbot.Prediction import get_response
from requete import get_value
import streamlit as st

zero_op = ['marques_batteries','tension_minimale','tension_maximale','poids_minimal','poids_maximal','capacite_maximale','capacite_minimale']
one_op = ['information_batterie','tension_inferieure','tension_superieure','poids_inferieur','poids_superieur','capacite_inferieure','capacite_superieure']
two_op = ['tension_intervalle','poids_intervalle','capacite_intervalle']

st.title("ChatBot")

def getAndFormatResponse(question):
    flat_response = get_response(question)
    tag = ""
    display_res = ""

    if flat_response["tag"] in zero_op and len(flat_response["valeur"]) != 0:
        return (tag, display_res, "")
    if flat_response["tag"] in one_op and len(flat_response["valeur"]) != 1:
        return (tag, display_res, "")
    if flat_response["tag"] in two_op and len(flat_response["valeur"]) != 2:
        return (tag, display_res, "")
    
    display_res = flat_response["reponse"]

    if flat_response["tag"] in ['salutation','remerciement','au_revoir','name','age']:
        tag = "common"
        display_res = flat_response["reponse"]
    elif flat_response["tag"] == 'information_batterie':
        tag ="dict"
        display_res = get_value(flat_response["tag"], flat_response["valeur"])
    elif flat_response["tag"] in ['tension_minimale','tension_maximale','poids_minimal','poids_maximal','capacite_maximale','capacite_minimale']:
        tag ="dict"
        display_res = get_value(flat_response["tag"])
    elif "batteries_" in flat_response["tag"] or flat_response["tag"] == "marques_batteries":
        tag ="dict"
        display_res = get_value(flat_response["tag"])
    elif flat_response["tag"] != 'information_batterie' and (len(flat_response["valeur"]) == 1 or len(flat_response["valeur"]) == 2):
        tag = "dict"
        display_res = get_value(flat_response["tag"], flat_response["valeur"])

    return (tag, display_res, flat_response["reponse"])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        message["content"]

# Accept user input
if prompt := st.chat_input("message"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        tag, full_response, rep = getAndFormatResponse(prompt)

        if tag == "common":
            st.write(full_response)
        elif tag == "dict":
            st.write(rep)
            st.table(full_response)
        else:
            full_response = "veuillez reformuler votre question"
            st.write("veuillez reformuler votre question")
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})