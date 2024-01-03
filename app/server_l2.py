from imports import *
from vulns import *

@app.route('/', methods=['POST', 'GET'])
def hello():
    return return_cookie(request)


@app.route('/csrf', methods=['POST', 'GET'])
def csrf_route():
    return make_response(render_template("csrf.html", cook=dict(request.cookies)))
 
@app.route('/cors', methods=['POST', 'GET'])
def cors_route():
    return make_response(render_template("cors.html", cook=dict(request.cookies)))


#               JS FILES
@app.route('/main.js', methods=['GET'])
def xss():
    return send_file('./js/main.js', download_name='xss.js')

@app.route('/csrf.js', methods=['GET'])
def xss1():
    return send_file('./js/csrf.js', download_name='xss.js')

@app.route('/cors.js', methods=['GET'])
def xss2():
    return send_file('./js/cors.js', download_name='xss.js')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++



## Start Server
if __name__ == "__main__":
    os.system('clear')
    print_c("\t\t<------------------START-SERVER----------------------->", "MAGENTA")
    app.run(host=app.host, port=app.port, ssl_context=('certs/cert.pem', 'certs/privkey.pem'))

