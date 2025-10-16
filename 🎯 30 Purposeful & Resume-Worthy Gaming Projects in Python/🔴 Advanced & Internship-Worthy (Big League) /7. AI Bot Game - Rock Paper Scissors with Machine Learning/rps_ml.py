# rps_ml.py
import random
import pickle
from collections import defaultdict, deque

# Simple pattern learner: transition counts of opponent moves
trans = defaultdict(lambda: defaultdict(int))
history = deque(maxlen=3)

def predict():
    key = tuple(history)
    if key in trans:
        # choose highest freq next move and beat it
        predicted = max(trans[key].items(), key=lambda x:x[1])[0]
        # map to move that beats predicted
        beats = {'R':'P','P':'S','S':'R'}
        return beats[predicted]
    return random.choice(['R','P','S'])

def update(prev_history, actual):
    trans[tuple(prev_history)][actual] += 1

def human_to_code(s):
    return {'r':'R','p':'P','s':'S'}[s.lower()]

if __name__ == "__main__":
    print("Enter r/p/s. Type exit to quit.")
    while True:
        human = input("You: ")
        if human == 'exit': break
        human = human_to_code(human)
        # AI predicts based on history
        ai = predict()
        print("AI:", ai)
        # update model
        prev = list(history)
        update(prev, human)
        history.append(human)
