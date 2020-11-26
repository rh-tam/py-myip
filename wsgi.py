from flask import Flask, render_template, request, jsonify
import random

application = Flask(__name__)
identity = random.randint(10000, 100000)
@application.route("/", methods=["GET"])
def get_my_ip():
    return render_template(
        'index.html', ip = request.environ['REMOTE_ADDR'],
        serverIP = request.host_url,
        ID = identity
        )

@application.route("/api", methods=["GET"])
def get_my_ip_api():
    return jsonify(
        {'ip': request.environ['REMOTE_ADDR']}
        ),200


if __name__ == '__main__':
    application.run()