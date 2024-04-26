from flask import Flask

app = Flask(__name__)


@app.get("/hello_world")
def hello_world() -> str:
    return "<h1>hello, world!</h1>"


app.run()
