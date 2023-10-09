from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Auto-Accept-Join-Request'
if __name__ == "__main__":
    app.run()
