import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')


pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "How can I help you today?"]
    ],
    [
        r"what is your name?",
        ["I am a simple chatbot.", "You can call me Chatbot."]
    ],
    [
        r"how are you ?",
        ["I'm good, thanks. How about you?", "I'm just a computer program, so I don't have feelings, but I'm here to assist you."]
    ],
    [
        r"what can you do for me ?",
        ["I can answer questions, provide information, and have a simple conversation with you."]
    ],
    [
        r"bye|quit",
        ["Goodbye! Have a great day.", "See you later!", "Bye!"]
    ],
]

def chatbot():
    print("Hi, I'm your chatbot. You can type 'bye' to exit the chat.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
