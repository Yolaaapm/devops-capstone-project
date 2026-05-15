from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
app = Flask(__name__)
# Konfigurasi CORS (Cross-Origin Resource Sharing)
CORS(app)
# Konfigurasi Talisman untuk Security Headers
# Memaksa HTTPS didefinisikan sebagai False jika di lingkungan
lokal/lab
talisman = Talisman(app, force_https=False)
from service import routes, models
