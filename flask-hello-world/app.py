from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")

def hello_world():
    return "Hello, World!"

@app.route("/test/<search_query>")
def search(search_query):
    return search_query


if __name__ == "__main__":
    app.run()
