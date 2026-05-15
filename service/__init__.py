from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Tambahkan baris ini agar aplikasi tidak error saat testing
CORS(app)
talisman = Talisman(app, force_https=False)

from service import routes, models
