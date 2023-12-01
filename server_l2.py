from imports import *
from vulns import *

@app.route('/', methods=['POST', 'GET'])
def hello():
    return return_cookie(request)


@app.route('/send', methods=['POST', 'GET'])
def js_file():
    return make_response(render_template("vuln_client.html"))
 

@app.route('/script.js', methods=['GET'])
def xss():
    return send_file('./test.js', download_name='xss.js')


## Start Server
if __name__ == "__main__":
    os.system('clear')
    print_c("\t\t<------------------START-SERVER----------------------->", "MAGENTA")
    app.run(host=app.host, port=app.port, ssl_context=('certs/cert.pem', 'certs/privkey.pem'))

