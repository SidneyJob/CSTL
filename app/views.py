from flask import (
    render_template,
    request,
    make_response,
    send_file,
    Blueprint,
    Response
)
import json
import os
import utils

lab_views = Blueprint('lab_views', __name__)

cors_pages = os.getenv("CORS_PAGES")
cors_domain = os.getenv("CORS_DOMAIN")
attack_domain = os.getenv("ATTACK_DOMAIN")
interactsh_domain = os.getenv("INTERACTSH_DOMAIN")


@lab_views.route('/', methods=['POST', 'GET'])
def hello():
    return utils.return_cookie(request)

@lab_views.route('/docs', methods=['POST', 'GET'])
def docs():
    return make_response(
        render_template("docs.html")
                )

@lab_views.route('/cors_testing', methods=['POST', 'GET'])
def cors_attack_route():
    return make_response(
        render_template("attack/cors.html",
                        ATTACK_DOMAIN=attack_domain,
                        INTERACTSH_DOMAIN=interactsh_domain,
                        CORS_PAGES=cors_pages)
                        )

@lab_views.route('/csrf_testing', methods=['POST', 'GET'])
def csrf_attack_route():
    return make_response(
        render_template("attack/csrf.html",
                        ATTACK_DOMAIN=attack_domain,
                        INTERACTSH_DOMAIN=interactsh_domain)
                        )

@lab_views.route('/edit', methods=['POST', 'GET'])
def edit_route():
    with open('templates/custom/payload.html','r') as f:
        body = f.read()

    with open('templates/custom/headers.json','r') as f:
        headers = f.read()

    res = make_response(render_template("edit.html",
                                        body=body,
                                        headers=headers
                                    ))
    try:
            # VIEW
            if request.form.get('action') == "View":
                res = make_response("Some",301)
                res.headers = {"Location":"/payload"}
            
            # STORE
            if request.form.get('action') == "Save":
                body = request.form.get('Body')
                headers = request.form.get('Headers')

                with open('templates/custom/payload.html','w') as f:
                    f.write(f"{body}")
                
                with open('templates/custom/headers.json','w') as f:
                    f.write(f"{headers}")
                
                res = make_response(render_template("edit.html",
                                        body=body,
                                        headers=headers
                                ))
                return res
                
    except() as f:
        pass

    return res


@lab_views.route('/payload', methods=['POST', 'GET'])
def payload_route():
    with open('templates/custom/headers.json','r') as f:
        headers_ = f.read()

    res = make_response(render_template("custom/payload.html"))
    res.headers = json.loads(headers_)

    return res


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
        origin = cors_domain

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
    res.headers['Access-Control-Allow-Origin'] = utils.setup_cors(request, cors_domain)
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
