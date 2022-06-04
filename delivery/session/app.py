from flask import Flask, session

app = Flask(__name__)

app.config["SECRET_KEY"] = 'abacate'


@app.route('/')
def index():    
    if "counter" not in session:
        session["counter"] = 0

    msg  = f"a contagem est em {session['counter']}"
    session["counter"] += 1
    return msg