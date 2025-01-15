# GroqChatbot

# 🤖 Llama 3.1 Chatbot

This project features a customizable AI chatbot powered by **Llama 3.1**, an advanced language model. Built using **Streamlit** and **Groq**, this app allows users to interact with the chatbot, personalize its behavior, and adjust its settings to suit their preferences.

## Features
- **Customizable Themes**: Select between **Light** or **Dark** themes.
- **Personalization Options**:
  - **Language**: Choose between English and Spanish.
  - **Chatbot Behavior**: Select a **Casual** or **Formal** tone for the chatbot's responses.
  - **Area of Expertise**: Set the assistant's area of expertise (e.g., **Technology**, **Science**, **History**).
  - **Interests**: Personalize the chatbot's responses based on selected interests (e.g., **Artificial Intelligence**, **Space Exploration**, etc.).
  - **Temperature & Max Tokens**: Adjust the creativity and length of the responses.
- **Footer**: A footer in the sidebar credits the creator and provides links to a personal website.

## Table of Contents
1. [Installation](#installation)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Customization](#customization)
5. [License](#license)

## Installation

### Prerequisites
- **Python 3.7+**: Ensure that you have Python installed on your system.
- **Streamlit**: The app is built using Streamlit, a Python library to create web apps.
- **Groq**: Used to access the Llama 3.1 model via API.

### Steps to Install
1. Clone the repository:
    git clone https://github.com/8669393253/GroqChatbot?tab=readme-ov-file
    cd llama-chatbot

2. Create a virtual environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install the required dependencies:

    pip install -r requirements.txt

4. Make sure you have an API key for **Groq** and add it to the `config.json` file in the project folder. The file should look like this:

    {
        "GROQ_API_KEY": "your-groq-api-key"
    }


## Setup

1. After installation, ensure that your `config.json` file contains the correct **Groq API Key**.
   
2. To start the app, simply run:

    streamlit run app.py

3. This will launch a local server, and you can view the app in your browser at `http://localhost:8501`.


## Usage

1. **Interact with the chatbot**: Once the app is running, you can enter any query into the chat input box and interact with the assistant.
   
2. **Customize the chatbot**:
    - Use the **sidebar** to customize the behavior and settings of the chatbot, including selecting themes, languages, tone, area of expertise, and interests.
    - The assistant will tailor its responses based on these preferences.

3. **View chat history**: As you chat with the assistant, the conversation history is displayed above the input box.

4. **Footer**: At the bottom of the sidebar, you will see a footer containing credits and a link to the creator's website.

## Customization

You can customize the chatbot and app's behavior by modifying the following:

- **Chatbot Behavior**: Adjust the tone (Casual/Formal) based on your preference.
- **Language**: Change the language to English or Spanish.
- **Area of Expertise**: Set the assistant’s area of expertise, such as **Technology**, **Science**, **History**, etc.
- **Interests**: Add multiple interests, such as **Artificial Intelligence**, **Space Exploration**, etc., to personalize the assistant's responses.
- **Temperature & Max Tokens**: Adjust the creativity and length of the responses to suit your needs.
- **Theme**: Switch between **Light** and **Dark** themes for the app.

### Footer Customization
The footer inside the sidebar credits the creator and provides a link to a personal website. To customize it:
1. Replace your name or another credit.
2. Update the link in the footer to point to your personal website or other relevant URLs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
