from odibets_api import Betika

b = Betika()

for jackpot in b.jackpot_events():
    print(jackpot.event_name, "\n", jackpot.prize)
