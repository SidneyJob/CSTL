from flask import Flask
from views import lab_views
<<<<<<< HEAD
from logger import setup_logger, check_decision
from dotenv import load_dotenv
=======
from colorful_logger import check_decision
from utils import logger
>>>>>>> cc8aa7d (Add colors to logger facility)
import ssl
import os

load_dotenv()
logger = setup_logger()

app = Flask(__name__, template_folder='templates')
app.register_blueprint(lab_views, url_prefix="/", name="lab_views")

app.secret_key = os.getenv("SECRET_KEY")
app.debug = check_decision("FLASK_DEBUG", 'False')

<<<<<<< HEAD

=======
>>>>>>> cc8aa7d (Add colors to logger facility)
flask_run_cert = check_decision("FLASK_RUN_CERT", 'False')
if flask_run_cert:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain('certs/cert.pem', 'certs/privkey.pem')
    logger.info("Server will use SSL certificates")
else:
    ctx = None

# Start server
if __name__ == "__main__":
    logger.warning(f"[+] Server started! {os.getenv('HOST')}:{os.getenv('PORT')}")

    app.run(
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT")),
        ssl_context=ctx
        )
