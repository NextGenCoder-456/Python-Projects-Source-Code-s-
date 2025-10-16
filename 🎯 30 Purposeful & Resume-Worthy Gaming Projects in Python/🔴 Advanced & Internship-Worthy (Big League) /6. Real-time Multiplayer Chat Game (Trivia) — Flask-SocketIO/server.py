from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

QUESTIONS = [{"q":"2+2?","a":"4"}, {"q":"Capital of India?","a":"Delhi"}]

@socketio.on('connect')
def on_connect():
    emit('message', {'msg':'Connected to Trivia Server'})

@socketio.on('join')
def on_join(data):
    join_room('game')
    emit('message', {'msg': f"{data['name']} joined"}, room='game')

@socketio.on('answer')
def on_answer(data):
    if data.get('ans') == QUESTIONS[data.get('qidx')]['a']:
        emit('correct', {'player': data['name']}, room='game')
    else:
        emit('incorrect', {'player': data['name']}, room='game')

@app.route('/')
def index(): return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, debug=True)

Note: Install: pip install flask-socketio

