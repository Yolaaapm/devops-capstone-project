from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Inisialisasi Security
CORS(app)
# Pastikan tidak ada teks 'lokal/lab' tanpa tanda pagar di sini
talisman = Talisman(app, force_https=False)

from service import routes, models  # noqa: F401, E402
