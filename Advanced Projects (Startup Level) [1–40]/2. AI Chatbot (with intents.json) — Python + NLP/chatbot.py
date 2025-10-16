import torch
import random
from train_chatbot import NeuralNet
from nltk_utils import bag_of_words, tokenize
import json

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open("intents.json", 'r') as f:
    intents = json.load(f)

data = torch.load("model.pth")

input_size = data['input_size']
output_size = data['output_size']
hidden_size = data['hidden_size']
all_words = data['all_words']
tags = data['tags']

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(data["model_state"])
model.eval()

print("🤖 Chatbot is ready! Type 'quit' to exit")

while True:
    sentence = input("You: ")
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = torch.from_numpy(X).float().unsqueeze(0)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{random.choice(intent['responses'])}")
    else:
        print("I didn't understand that. Can you try again?")
