from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """<!DOCTYPE html>
<html>
    <body>
        <h1>Welcome to Just for Dockerize Project.</h1>
        <h4>https://github.com/ssbostan/just-for-dockerize</h4>
    </body>
</html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
