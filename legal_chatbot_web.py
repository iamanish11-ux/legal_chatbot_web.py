# Legal Chatbot
# Created by Anish LS. Tamang – Your Legal AI Assistant

import streamlit as st

# Title and creator info
st.title("Legal Chatbot")
st.subheader("Created by Anish LS. Tamang – Your Legal AI Assistant")
st.write("Ask me about landmark judgments, constitutional provisions, cyber and IT laws, or criminal sections. Type 'exit' to quit.")

# Button to show creator information
if st.button("About Creator"):
    st.info("Created by Anish LS. Tamang, an Advocate and AI enthusiast.")

# Dictionary of cases, articles, sections
responses = {
    # Constitutional landmark cases
    "maneka gandhi case": "Maneka Gandhi v. Union of India (1978) – Expanded Article 21, Right to Life and Personal Liberty.",
    "kesavananda bharati": "Kesavananda Bharati v. State of Kerala (1973) – Basic Structure Doctrine of the Constitution.",
    "indira gandhi case": "Indira Gandhi v. Raj Narain (1975) – Judicial review and election validity.",
    
    # Articles of the Constitution
    "article 19": "Article 19 – Right to Freedom of Speech, Expression, Assembly, Association, Movement, and Residence.",
    "article 21": "Article 21 – Protection of life and personal liberty.",
    "article 14": "Article 14 – Right to Equality before law and equal protection of laws.",
    
    # Criminal sections
    "section 420": "Section 420 IPC – Cheating and dishonestly inducing delivery of property.",
    "section 376": "Section 376 IPC – Punishment for rape.",
    
    # Cyber & IT laws
    "section 66": "Section 66 IT Act – Computer-related offences.",
    "section 66c": "Section 66C IT Act – Identity theft and phishing.",
    "section 43": "Section 43 IT Act – Penalty and compensation for damage to computer, etc.",
    
    # General greetings and exit
    "hello": "Hello! I am your Legal AI Assistant. Ask me about laws, judgments, or sections.",
    "hi": "Hi there! How can I help you with legal information today?",
    "exit": "Goodbye! Thank you for using the Legal Chatbot.",
    
    # Instructions for listing available topics
    "list": "You can ask me about landmark cases, constitutional articles, criminal sections, or cyber laws. Try asking about 'Article 21' or 'Maneka Gandhi case'."
}

# Function to handle user queries
def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I have no information on that. Try another query.")

# Streamlit input/output
user_input = st.text_input("You:", "")
if user_input:
    response = chatbot_response(user_input)
    st.text("Bot: " + response)
