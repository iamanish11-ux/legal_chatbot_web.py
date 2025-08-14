 HEAD
# legal_chatbot_web.py
# Legal Chatbot
# Created by Anish LS. Tamang – Your Legal AI Assistant

def chatbot_response(user_input):
    user_input = user_input.lower()  # makes input case-insensitive

    # Dictionary of responses
    responses  {
        # Greetings
        "hello": "Hello! I am your Legal AI Assistant. Ask me about judgments or laws.",
        "hi": "Hi there! How can I help you with legal questions today?",
        "hey": "Hey! Ready to discuss laws and judgments.",
        
        # Constitutional Articles
        "article 21": "Article 21 of the Indian Constitution: Protection of life and personal liberty.",
        "article 19": "Article 19: Right to freedom of speech and expression.",
        "article 14": "Article 14: Right to equality before law.",
        
        # Landmark Judgments
        "maneka gandhi": "Maneka Gandhi vs Union of India (1978): Expanded interpretation of Article 21.",
        "kesavananda bharati": "Kesavananda Bharati (1973): Fundamental rights cannot be altered by amendment.",
        "golaknath": "Golaknath vs State of Punjab (1967): Parliament cannot take away fundamental rights.",
        "s r bommai": "S.R. Bommai vs Union of India (1994): Limits on President's Rule and state government dismissal.",
        "t m a pai": "T.M.A. Pai Foundation vs State of Karnataka (2002): Right to establish educational institutions.",

        # Cyber & IT Laws
        "it act": "Information Technology Act, 2000: Governs cyber activities and e-commerce.",
        "cyber law": "Cyber Law includes laws relating to cybercrime, IT Act, and data protection.",
        "data protection": "Data Protection laws ensure privacy and proper handling of personal data.",
        "information technology": "Information Technology Act provides legal recognition of electronic records and digital signatures."
    }

    # Check dictionary for keyword match
    for key in responses:
        if key in user_input:
            return responses[key]

    # General responses
    if "judgment" in user_input:
        return "I can summarize a judgment for you. Please provide the case name."
    if "law" in user_input:
        return "I can help explain laws. Which law do you want to know about?"
    if "exit" in user_input:
        return "Goodbye! Thank you for using the Legal Chatbot."

    return "I am sorry, I do not have information on that."

# Main program loop
if __name__  "__main__":
    print("Legal Chatbot – Created by Anish LS. Tamang")
    print("Type 'exit' to quit.\n")
    while True:
        user_input  input("You: ")
        response  chatbot_response(user_input)
        print("Bot:", response)
        if user_input.lower()  "exit":
            break

import streamlit as st

# Chatbot title and creator name
st.title("Legal Chatbot")
st.subheader("Created by Anish LS. Tamang – Your Legal AI Assistant")

# Pre-written legal cases and laws
cases_and_laws {
    # Landmark judgments
    "maneka gandhi": "Maneka Gandhi vs Union of India (1978): Landmark judgment on personal liberty under Article 21.",
    "kesavananda bharati": "Kesavananda Bharati vs State of Kerala (1973): Introduced the Basic Structure Doctrine.",
    "golaknath": "Golaknath vs State of Punjab (1967): Parliament cannot amend Fundamental Rights.",
    "indira gandhi vs raj narain": "Indira Gandhi vs Raj Narain (1975): Election petition case.",

    # Important constitutional articles
    "article 21": "Article 21 of the Indian Constitution: Protection of life and personal liberty.",
    "article 19": "Article 19: Freedom of speech, expression, assembly, and association.",

    # Indian Penal Code Sections
    "section 420": "Section 420 IPC: Cheating and dishonestly inducing delivery of property.",
    "section 406": "Section 406 IPC: Punishment for criminal breach of trust.",
    "section 375": "Section 375 IPC: Defines rape and consent.",
    "section 302": "Section 302 IPC: Punishment for murder.",
    "section 307": "Section 307 IPC: Attempt to murder.",
    "section 34": "Section 34 IPC: Acts done by several persons in furtherance of common intention.",
    "section 498a": "Section 498A IPC: Cruelty by husband or relatives of husband towards a woman.",
    "section 138": "Section 138 NI Act: Dishonor of cheque for insufficiency of funds.",
    "section 3": "Section 3 PDPP Act: Damage to public property."
}

# Chatbot function
def chatbot_response(user_input):
    user_input  user_input.lower()  # Makes it case-insensitive
    for key in cases_and_laws:
        if key in user_input:
            return cases_and_laws[key]
    return "I don't have information on that. Ask me about judgments or laws."

# Streamlit input and output
user_input  st.text_input("You:")
if user_input:
    response chatbot_response(user_input)
    st.text("Bot: " + response)

# About Creator button
if st.button("About Creator"):
    st.info("This Legal Chatbot was created by Anish LS. Tamang, an advocate and AI enthusiast.")
 bffa2abae5e99547557e91d98ebcc300a4f8145c
