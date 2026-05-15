from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Inisialisasi Security
CORS(app)
talisman = Talisman(app, force_https=False)

# Import routes dan models di bawah agar tidak circular import
# Kita tambahkan noqa agar Flake8 tidak protes
from service import routes, models  # noqa: F401, E402
