import sys
import os

# Caminho da pasta /orquestrator
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho da pasta /backend
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))

# Adiciona ambas no PYTHONPATH
sys.path.insert(0, CURRENT_DIR)
sys.path.insert(0, ROOT_DIR)

# --- AQUI SIM pode importar ---
from config.settings import settings
import httpx

base_url = settings.CORE_URL


def execute_al():
    post_url = f"{base_url.rstrip('/')}/assembly/upsert"
    httpx.post(post_url)

execute_al()