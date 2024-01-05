from flask import (
    render_template,
    request,
    make_response,
    send_file,
    Blueprint,
    Response
)
from logger import setup_logger

import json
import os
import utils

logger = setup_logger()
lab_views = Blueprint('lab_views', __name__)
origin_domain = os.getenv("ORIGIN_DOMAIN")


@lab_views.route('/', methods=['POST', 'GET'])
def hello():
    return utils.return_cookie(request)


@lab_views.route('/attack', methods=['POST', 'GET'])
def attack_route():
    return make_response(render_template("attack.html",
                                         cook=dict(request.cookies)
                                         ))


# Return JavaScript files
@lab_views.route('/main.js', methods=['GET'])
def xss():
    return send_file('./js/main.js', download_name='xss.js')


@lab_views.route('/csrf.js', methods=['GET'])
def xss1():
    return send_file('./js/csrf.js', download_name='xss.js')


@lab_views.route('/cors.js', methods=['GET'])
def xss2():
    return send_file('./js/cors.js', download_name='xss.js')


# Page to test CSRF
@lab_views.route('/reset_password', methods=["GET", "POST"])
def reset_password():
    if utils.check_result(request):
        return "Successfull reset!"

    return "None"


@lab_views.route('/api_gen', methods=['POST', 'GET'])
def api_gen():
    res = Response(json.dumps(
        {"key": None}
    ))

    try:
        origin = request.headers['Origin']
    except:
        origin = origin_domain

    res.headers['Content-Type'] = "application/json"
    res.headers['Access-Control-Allow-Origin'] = origin
    res.headers['Access-Control-Allow-Credentials'] = 'true'


    if utils.check_result(request):
        logger.info(f"Authentication passed on {request.url}")

        res.data = json.dumps(
            {"key": f"SidneyJob{{{utils.gen_random_string(16)}_gen_page}}"}
        )

        return res
    return res


@lab_views.route('/api_null', methods=['POST', 'GET'])
def api_null():
    res = Response(json.dumps(
        {"key": None}
    ))

    res.headers['Content-Type'] = "application/json"
    res.headers['Access-Control-Allow-Origin'] = 'null'
    res.headers['Access-Control-Allow-Credentials'] = 'true'

    if utils.check_result(request):
        res.data = json.dumps(
            {"key": f"SidneyJob{{{utils.gen_random_string(16)}_null_page}}"}
        )

        return res
    return res


@lab_views.route('/api_correct', methods=['POST', 'GET'])
def api_correct():
    res = Response(json.dumps(
        {"key": None}
    ))

    res.headers['Content-Type'] = "application/json"
    res.headers['Access-Control-Allow-Origin'] = utils.setup_cors(request, origin_domain)
    res.headers['Access-Control-Allow-Credentials'] = 'true'  

    if utils.check_result(request):
        res.data = json.dumps(
            {"key": f"SidneyJob{{{utils.gen_random_string(16)}_creds_page}}"}
        )

        return res
    return res

@lab_views.route('/api_wildcard', methods=['POST', 'GET'])
def api_creds():
    res = Response(json.dumps(
        {"key": None}
    ))

    res.headers['Content-Type'] = "application/json"
    res.headers['Access-Control-Allow-Origin'] = "*"

    if utils.check_result(request):
        res.data = json.dumps(
            {"key": f"SidneyJob{{{utils.gen_random_string(16)}_creds_page}}"}
        )

        return res
    return res
