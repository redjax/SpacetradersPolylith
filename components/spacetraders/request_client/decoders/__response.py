from __future__ import annotations

import logging

log = logging.getLogger(__name__)

import json

import httpx

def decode_response_content(res: httpx.Response = None) -> dict:
    _content: dict = json.loads(res.content)

    return _content
