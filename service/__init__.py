from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Inisialisasi Security
CORS(app)
talisman = Talisman(app, force_https=False)

# Berikan tanda # noqa agar Flake8 tidak error
from service import routes, models  # noqa: F401, E402
