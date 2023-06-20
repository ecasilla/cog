import yaml
import os.path
from typing import Any, Dict

from fastapi import APIRouter

Router = APIRouter()

@Router.get("/metadata")
async def get_metadata():
    # read the hypc_aim.yaml file and return it'
    config = load_config()
    return config

class HypcError(Exception):
    """Base class for all Hypc errors."""


class ConfigDoesNotExist(HypcError):
    """Exception raised when a hypc_aim.yaml does not exist."""

def load_config() -> Dict[str, Any]:
    """
    Reads hypc_aim.yaml and returns it as a dict.
    """
    # Assumes the working directory is /src
    config_path = os.path.abspath("hypc_aim.yaml")
    try:
        with open(config_path) as fh:
            config = yaml.safe_load(fh)
    except FileNotFoundError as e:
        raise ConfigDoesNotExist(
            f"Could not find {config_path}",
        ) from e
    return config
