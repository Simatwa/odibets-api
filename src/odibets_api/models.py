from pydantic import BaseModel
from datetime import datetime
from typing import Any, Union


class JackpotMeta(BaseModel):
    """
    ```json
     {
          "week_id": "720",
          "name": "Laki-2024-06-01",
          "status": "1",
          "start_time": "2024-06-01 21:30:00"
      }
    ```
    """

    week_id: int
    name: str
    status: int
    start_time: datetime


class Jackpot(BaseModel):
    """
    ```json
    {
        "jackpot_id": "16",
        "name": "LAKITATU DAILY JACKPOT",
        "bet_amount": "15.00",
        "prize": "300000.00",
        "games": "10",
        "bonus_starts_at": "8,9,10",
        "binomen": "lakitatu",
        "meta": {
          "week_id": "720",
          "name": "Laki-2024-06-01",
          "status": "1",
          "start_time": "2024-06-01 21:30:00"
        }
    }
    ```
    """

    jackpot_id: int
    name: str
    bet_amount: float
    prize: float
    games: int
    bonus_starts_at: str
    binomen: str
    meta: JackpotMeta


class Outcome(BaseModel):
    """
    ```json
    {
        "outcome_id": "1",
        "outcome_key": "1",
        "outcome_name": "CA Chacarita Juniors",
        "specifiers": "",
        "odd_value": "1.84",
        "status": "1",
        "sub_type_id": "1",
        "odd_type": "3 Way",
        "live": "0"
    }
    ```
    """

    outcome_id: int
    outcome_key: str
    outcome_name: str
    specifiers: str
    odd_value: float
    status: str
    sub_type_id: str
    odd_type: str
    live: str


class Match(BaseModel):
    """
    ```json
    {
        "parent_match_id": "46928063",
        "home_team": "CA Chacarita Juniors",
        "away_team": "CA Guemes",
        "start_time": "2024-06-01 21:30:00",
        "sport_id": "1",
        "jp_week_id": "720",
        "outcomes": [
          {
            "outcome_id": "1",
            "outcome_key": "1",
            "outcome_name": "CA Chacarita Juniors",
            "specifiers": "",
            "odd_value": "1.84",
            "status": "1",
            "sub_type_id": "1",
            "odd_type": "3 Way",
            "live": "0"
          },
        ]
    }
    ```
    """

    parent_match_id: int
    home_team: str
    away_team: str
    start_time: datetime
    sport_id: int
    jp_week_id: int
    outcomes: list[Outcome]


class JackpotMatches(BaseModel):
    """Combines Jackpot and Matches"""

    jackpots: list[Jackpot]
    matches: list[Match]
