from flask import Flask
from views import lab_views
from logger import setup_logger
# import ssl
import os

# ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# ctx.load_cert_chain('certs/cert.pem', 'certs/privkey.pem')

app = Flask(__name__, template_folder='templates')
app.register_blueprint(lab_views, url_prefix="/", name="lab_views")

app.secret_key = os.getenv("SECRET_KEY")
app.debug = os.getenv("FLASK_DEBUG", 'False').lower() in ['1', 'true']

logger = setup_logger()

# Start server
if __name__ == "__main__":
    logger.debug("Server started")
    app.run(
        host='0.0.0.0',
        port=8081,
        # debug=True,
        # ssl_context=ctx
        )
