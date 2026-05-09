
import random
import datetime
import streamlit as st


st.set_page_config(
    page_title="MockChat",
    page_icon="💬",
    layout="centered",
)



GREETINGS = {"hi", "hello", "hey", "howdy", "hiya", "greetings", "sup", "yo"}

FAQ = {
    "how are you":        "I'm doing great, thanks for asking! How about you?",
    "what is your name":  "I'm MockChat — a fully local, API-free chatbot built with Streamlit.",
    "what can you do":    "I can reply to your messages using a simple local Python function. No AI, no API!",
    "who made you":       "I was coded in Python using Streamlit. My responses come from plain `if/elif` logic.",
    "what time is it":    lambda: f"Your system time is {datetime.datetime.now().strftime('%H:%M:%S')}.",
    "what is today":      lambda: f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}.",
    "tell me a joke":     (
        "Why do programmers prefer dark mode?\n"
        "Because light attracts bugs! "
    ),
    "help":               (
        "Try asking me:\n"
        "- 'Tell me a joke'\n"
        "- 'What time is it?'\n"
        "- 'What can you do?'\n"
        "- 'Who made you?'\n"
        "- Or just say hi!"
    ),
}

FALLBACKS = [
    "Interesting! Tell me more.",
    "I'm not sure I understand — could you rephrase that?",
    "That's a great point! (Though I'm just a mock bot )",
    "I only know a handful of things, but I'm learning!",
    "Fascinating. My creator hard-coded that reaction.",
    "As a locally-simulated bot, I have limited wisdom. Try asking for 'help'.",
    "Hmm, I don't have a scripted answer for that. Try 'help' to see what I know.",
]


def generate_response(user_text: str) -> str:
 
    clean = user_text.lower().strip().rstrip("?.!")

   
    if clean in GREETINGS or any(g in clean for g in GREETINGS):
        return "Hello there! How can I help you today? (Type 'help' to see what I know.)"


    for key, reply in FAQ.items():
        if key in clean:
         
            return reply() if callable(reply) else reply

    return random.choice(FALLBACKS)




if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                " Hi! I'm **MockChat**, a fully local chatbot — "
                "no API, no LLM, just Python!\n\n"
                "Type `help` to see what I can do."
            ),
        }
    ]


st.title("MockChat")
st.caption("A ChatGPT-style app powered by pure Python — zero external APIs.")
st.divider()



for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("Type a message…"):

   
    with st.chat_message("user"):
        st.markdown(prompt)

  
    st.session_state.messages.append({"role": "user", "content": prompt})

   
    response = generate_response(prompt)

  
    with st.chat_message("assistant"):
        st.markdown(response)

    
    st.session_state.messages.append({"role": "assistant", "content": response})

