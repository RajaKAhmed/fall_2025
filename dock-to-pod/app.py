from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi I am a container. I was made in Python, built and running in Docker! \\n"

if __name__ == "__main__":
    # 0.0.0.0 means "listen on all network interfaces inside the container"
    app.run(host="0.0.0.0", port=5000)


