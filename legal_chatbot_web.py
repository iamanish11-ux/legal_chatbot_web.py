# legal_chatbot_web.py
# Legal Chatbot
# Created by Anish LS. Tamang – Your Legal AI Assistant

def chatbot_response(user_input):
    user_input = user_input.lower()  # makes input case-insensitive

    # Dictionary of responses
    responses = {
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
if __name__ == "__main__":
    print("Legal Chatbot – Created by Anish LS. Tamang")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if user_input.lower() == "exit":
            break
