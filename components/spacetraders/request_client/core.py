from __future__ import annotations

import logging
import typing as t

log = logging.getLogger(__name__)

import chardet
import hishel
import httpx

def get_httpx_client(
    headers: t.Union[httpx.Headers, dict] | None = None,
    params: t.Union[httpx.QueryParams, dict] | None = None,
    follow_redirects: bool = False,
    max_redirects: int = 20,
    timeout: t.Union[httpx.Timeout, int, float] | None = 5.0,
) -> httpx.Client:
    try:
        _client: httpx.Client = httpx.Client(
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
            max_redirects=max_redirects,
            timeout=timeout,
        )

        return _client
    except Exception as exc:
        msg = f"({type(exc)}) Unhandled exception getting HTTPX client. Details: {exc}"
        log.error(msg)

        raise exc
