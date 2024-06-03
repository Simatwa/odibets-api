from odibets_api import Odibets

inf = Odibets().daily_jackpot()

print(inf.matches)

for match in inf.matches:
    print(match.sport_id, match.home_team, match.away_team, match.start_time, sep=" - ")
