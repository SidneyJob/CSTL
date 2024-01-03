from flask import Flask
from views import lab_views
import logging
import ssl

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain('certs/cert.pem', 'certs/privkey.pem')

app = Flask(__name__, template_folder='templates')
app.register_blueprint(lab_views, url_prefix="/", name="lab_views")

app.config.from_pyfile("config.py")

# disable logging requests
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

# start Server
if __name__ == "__main__":
    # os.system('clear')
    print("\t\t<-START-SERVER----------------------->", "MAGENTA")
    app.run(
        host='0.0.0.0',
        port=8081,
        debug=True,
        ssl_context=ctx
        )