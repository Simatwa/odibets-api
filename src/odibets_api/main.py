import requests
import typing
import odibets_api.utils as odibets_utils
from odibets_api import models

session = requests.Session()

session.headers.update(
    {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Origin": "https://www.odibets.com",
        "Referer": "https://www.odibets.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
    }
)


def fetch_json(*args, **kwargs) -> dict[typing.Any, typing.Any]:
    """Get resource `requests.get`"""
    resp = session.get(*args, **kwargs)
    resp.raise_for_status()
    return resp.json()


class Odibets:

    def __init__(self):
        """Constructor"""
        pass

    def daily_jackpot(self) -> models.JackpotMatches:
        """Laki tatu daily jackpot

        Returns:
            models.JackpotMatches: __
        """
        data: dict = fetch_json(odibets_utils.Urls.daily_jackpot)["data"]
        jackpot: dict = data["jackpots"][0]  # assume there's only one jackpot
        jackpot_meta = jackpot["meta"]
        jackpot["meta"] = models.JackpotMeta(**jackpot_meta)

        matches_list = []
        for match in data["matches"]:
            outcomes = list
            for outcome in match["outcomes"]:
                outcomes.append(models.Outcome(**outcome))
            match["outcomes"] = outcomes
            matches_list.append(models.Match(**match))

        return models.JackpotMatches(
            jackpot=models.Jackpot(**jackpot), matches=matches_list
        )
