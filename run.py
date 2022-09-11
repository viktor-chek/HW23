from marshmallow import ValidationError
from flask import Flask, request
from models import Request
from builder import response_builder


def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/perform_query', methods=["POST"])
def perform_query():
    try:
        params = Request().load(request.json)
    except ValidationError as e:
        return e.messages, 400
    res = response_builder(
        path=params['filename'],
        cmd1=params['cmd1'],
        param1=params['value1'],
        cmd2=params['cmd2'],
        param2=params['value2']
    )

    return res


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7000)
