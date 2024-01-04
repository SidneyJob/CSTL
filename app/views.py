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
import utils

logger = setup_logger()
lab_views = Blueprint('lab_views', __name__)


@lab_views.route('/', methods=['POST', 'GET'])
def hello():
    return utils.return_cookie(request)


@lab_views.route('/csrf', methods=['POST', 'GET'])
def csrf_route():
    return make_response(render_template("csrf.html",
                                         cook=dict(request.cookies)
                                         ))


@lab_views.route('/cors', methods=['POST', 'GET'])
def cors_route():
    return make_response(render_template("cors.html",
                                         cook=dict(request.cookies)
                                         ))


@lab_views.route('/send', methods=['POST', 'GET'])
def js_file():
    return make_response(render_template("vuln_client.html"))


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
    # cookies = []

    if utils.check_result(request):
        return "Successfull reset!"

    return "None"


@lab_views.route('/api_gen', methods=['POST', 'GET'])
def api_gen():
    res = Response(json.dumps(
        {"key": None}
    ))

    try:
        Origin = request.headers['Origin']
    except:
        Origin = "https://discovery-lab.su"

    res.headers['Content-Type'] = "application/json"
    res.headers['Access-Control-Allow-Origin'] = Origin
    res.headers['Access-Control-Allow-Credentials'] = 'true'

    cookies = []
    if request.cookies.get('None'):
        cookies.append(f'None: {request.cookies.get("None")}')

    if request.cookies.get('Lax'):
        cookies.append(f'Lax: {request.cookies.get("Lax")}')

    if request.cookies.get('Strict'):
        cookies.append(f'Strict: {request.cookies.get("Strict")}')

    if cookies:
        logger.info(f"Authentication passed on {request.url}")
        logger.info(f"Cookies:\n{utils.print_cookies(cookies)}")

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
    res.headers['Access-Control-Allow-Origin'] = "https://discovery.sidneyjob.ru"
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
