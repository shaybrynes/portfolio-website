import flask

from config import Config

from flask_cors import CORS

config = Config()

app = flask.Flask(__name__)
app.secret_key = bytes.fromhex(config.get("webserver", "secret_key"))

cors = CORS(app)
app.config["DEBUG"] = config.get("webserver", "debug")
app.config["CORS_HEADERS"] = config.get("webserver", "cors_headers")


@app.route('/', methods=['GET'])
def home():
    """
    A catchall page
    :return:
    """
    return "hello world"


if __name__ == "__main__":
    app.run(host=config.get("webserver", "host"),
            port=config.get("webserver", "port"))
