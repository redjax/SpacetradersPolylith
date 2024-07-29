from __future__ import annotations

import logging

log = logging.getLogger(__name__)

import dynaconf
from pydantic import ConfigDict, Field, ValidationError, computed_field, field_validator
from pydantic_settings import BaseSettings

DYNACONF_SPACETRADERS_SETTINGS = dynaconf.Dynaconf(
    environments=True,
    environment="spacetraders_api",
    envvar_prefix="st",
    settings_files=["config/settings.toml", "config/.secrets.toml"],
)


class SpacetradersAPISettings(BaseSettings):
    api_base_url: str = Field(
        default=DYNACONF_SPACETRADERS_SETTINGS.ST_BASE_URL, env="ST_BASE_URL"
    )
