import os
import json
import streamlit as st
from groq import Groq

# Streamlit page configurations
st.set_page_config(
    page_title="🤖 Llama 3.1 Chatbot",
    page_icon="🗪",
    layout="wide"  # Use wide layout for more space
)

# Load configuration data
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

GROQ_API_KEY = config_data["GROQ_API_KEY"]

# Save the API key to the environment
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

# Initialize chat history in Streamlit session state if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar with a title and user options
with st.sidebar:
    st.title("🤖 Llama 3.1 Chatbot Settings")
    st.markdown("### Chatbot Customization")
    st.markdown("Customize the chatbot's behavior and appearance.")

    # Theme selection
    theme = st.selectbox("Select Theme", ["Light", "Dark"])

    # Language selection
    language = st.selectbox("Preferred Language", ["English", "Spanish"])

    # Chatbot behavior (tone)
    behavior = st.radio("Chatbot Behavior", ["Casual", "Formal"])

    # Area of expertise selection
    expertise = st.selectbox("Select Area of Expertise", 
                             ["General Knowledge", "Technology", "Science", "History", "Art", "Literature"])

    # Interests selection (Multiple choices)
    interests = st.multiselect("Select Interests", 
                               ["Artificial Intelligence", "Space Exploration", "Health", "Gaming", "Music", "Literature", "Sports"])

    # Optional settings for the assistant
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
    max_tokens = st.slider("Max Tokens", min_value=50, max_value=2000, value=500)

    # Footer inside the sidebar
    st.markdown(
        """
        <footer style="text-align: center; padding: 20px; font-size: 12px; color: #777; background-color: #f1f1f1; border-top: 1px solid #ccc; margin-top: 40px;">
            Made with ❤️ by Tansen.<br>
            Version 1.0 | <a href="https://www.linkedin.com/in/tansen-balpande-48604420b?trk=contact-info" target="_blank" style="color: #0073e6;">Visit my Linkedin Page</a>
        </footer>
        """, unsafe_allow_html=True
    )

# Adjusting the page based on the selected theme
if theme == "Dark":
    st.markdown(
        """
        <style>
        .streamlit-expanderHeader {
            background-color: #333;
            color: #FFF;
        }
        .stButton>button {
            background-color: #555;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )

# Main page content
st.title("🤖 Llama 3.1 Chatbot")
st.markdown(
    """
    ### Welcome to Llama 3.1 Chatbot
    Ask anything, and Llama will respond! 
    Use the sidebar for customization options.

    ### How to Use:
    - Type your questions in the input box below.
    - Adjust the settings in the sidebar for a more personalized experience.
    - You can even guide the assistant's behavior and expertise!
    """
)

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user query
user_prompt = st.chat_input("Ask Llama...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Constructing a detailed system message
    system_message = "You are a helpful assistant."
    
    # Adjust behavior based on the selected tone
    if behavior == "Casual":
        system_message = "You are a friendly assistant, using a casual tone."
    elif behavior == "Formal":
        system_message = "You are a professional assistant, using a formal tone."

    # Add expertise and interests to the system message
    system_message += f" Your area of expertise is {expertise}."
    
    if interests:
        system_message += f" Your areas of interest include {', '.join(interests)}."
    
    # Adding language context (optional for future multilingual support)
    if language == "Spanish":
        system_message += " Respond in Spanish."

    # Add previous chat history
    messages = [
        {"role": "system", "content": system_message},
        *st.session_state.chat_history,
    ]
    
    # Send messages to the model and get the response
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # Display the assistant's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
