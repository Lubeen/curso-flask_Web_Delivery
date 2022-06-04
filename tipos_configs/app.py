from flask import Flask

app = Flask(__name__)
app.config.from_object['settings']


@app.route("/")
def index():
    return f"Um exemplo de como startar as configs no app, metodo de classe config, from_object passando 'settings' {app.config['FOO']}"