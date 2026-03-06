from typing import Any, Dict, Optional
from config.settings import settings
import httpx


class CoreAPIClient:
    def __init__(self, timeout: int = 30):
        self.base_url = settings.CORE_URL.rstrip("/")
        self.client = httpx.Client(timeout=timeout)

    def _post(self, endpoint: str, data: Optional[Dict] = None) -> httpx.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.client.post(url, json=data)
        response.raise_for_status()
        return response

    def _patch(self, endpoint: str, data: Optional[Dict] = None) -> httpx.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.client.patch(url, json=data)
        response.raise_for_status()
        return response

    def _get(self, endpoint: str) -> httpx.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.client.get(url)
        response.raise_for_status()
        return response
