from importlib import metadata

try:
    __version__ = metadata.version("odibets-api")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0"

__repo__ = "https://github.com/Simatwa/odibets-api"

__author__ = "Smartwa"

from odibets_api.main import Odibets
