from flask import Flask
from views import lab_views
from logger import setup_logger, check_decision
import ssl
import os

app = Flask(__name__, template_folder='templates')
app.register_blueprint(lab_views, url_prefix="/", name="lab_views")

app.secret_key = os.getenv("SECRET_KEY")
app.debug = check_decision("FLASK_DEBUG", 'False')

logger = setup_logger()

flask_run_cert = check_decision("FLASK_RUN_CERT", 'False')
if flask_run_cert:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain('certs/cert.pem', 'certs/privkey.pem')
    logger.info("Server will use SSL certificates")
else:
    ctx = None

# Start server
if __name__ == "__main__":
    logger.debug("Server started")
    app.run(
        host='0.0.0.0',
        port=8081,
        ssl_context=ctx
        )
