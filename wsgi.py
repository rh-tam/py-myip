from flask import Flask, render_template, request, jsonify

application = Flask(__name__)

@application.route("/", methods=["GET"])
def get_my_ip():
    return render_template(
        'index.html', ip = request.environ['REMOTE_ADDR'],
        serverIP = request.host_url
        )

@application.route("/api", methods=["GET"])
def get_my_ip_api():
    return jsonify(
        {'ip': request.environ['REMOTE_ADDR']}
        ),200


if __name__ == '__main__':
    application.run()