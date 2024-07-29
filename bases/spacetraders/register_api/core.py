from __future__ import annotations

import logging

log = logging.getLogger(__name__)

from spacetraders.constants import SPACETRADERS_API_BASE_URL

def print_api_url():
    print(f"API base URL: {SPACETRADERS_API_BASE_URL}")
