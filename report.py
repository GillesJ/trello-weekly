#!/usr/bin/env python3
"""
makeoverview.py
trelloweeklyoverview 
3/26/18
Copyright (c) Gilles Jacobs. All rights reserved.  
"""
import secrets
import string
from trello import TrelloClient
import pytz
from collections import OrderedDict
from isoweek import Week
from datetime import datetime
import os
import subprocess


def get_date(card):
    try:
        cdt = card.latestCardMove_date
        if not cdt:
            cdt = card.date_last_activity
    except Exception as e:
        print(e)
        cdt = card.date_last_activity
    if cdt is None:
        cdt = pytz.utc.localize(datetime.now())
    return cdt


client = TrelloClient(api_key=secrets.API_KEY, api_secret=secrets.API_SECRET,)

days = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]

# make the report
list = client.get_list(secrets.LIST_IDS[0])
cards_unsorted = list.list_cards()
cards = sorted(cards_unsorted, key=lambda x: get_date(x))
report = OrderedDict()
for c in cards:
    dt = get_date(c)
    weekday = days[dt.weekday()]
    week_nr = int(dt.strftime("%W"))+1
    start = Week(int(dt.strftime("%Y")), week_nr).monday().strftime("%d-%m-%Y")
    week_id = f"{week_nr} ({start})"
    label_str = ", ".join(set(l.name for l in c.labels)) if c.labels else ""

    if week_id not in report:
        report[week_id] = {}
    if weekday in report[week_id]:
        report[week_id][weekday].append(f"{label_str}: {c.name}")
    else:
        report[week_id][weekday] = [f"{label_str}: {c.name}"]

# print to data in report to a string
report_str = ""
for week_id, days in report.items():
    week_str = f"Activiteiten Week {week_id}"
    report_str += week_str
    for day, cards in days.items():
        report_str += os.linesep * 2 + f"{day}:"
        for card in cards:
            # add punctuation to sentence.
            if card[-1:] not in string.punctuation:
                card = card + "."
            card_str = f"\t• {card}"
            report_str += os.linesep + card_str
    report_str += os.linesep * 2

print(report_str)

# get issues to discuss
items = ""
list = client.get_list(secrets.LIST_IDS[1])
for c in list.list_cards():
    label_str = ", ".join(set(l.name for l in c.labels)) if c.labels else ""
    card_text = c.name
    if card_text[-1:] not in string.punctuation:
        card_text = card_text + "."
    item = f"\t• {label_str}{card_text}"
    items += os.linesep + item

print("Opening email client.")

if items:
    meeting_date = Week(int(dt.strftime("%Y")), week_nr+1).monday().strftime("%d-%m-%Y")
    body = f"""Dag Veronique,
Hier is mijn wekelijks activiteiten overzicht en punten voor onze komende weekelijkse supervisor vergadering.

Volgende vergadering items ({meeting_date}):{items}

{report_str}

Groetjes
Gilles
"""
else:
    body = f"""Dag Veronique,

Hier is mijn wekelijks activiteiten overzicht.

{report_str}

Groetjes
Gilles
"""

cmd = [
    "thunderbird",
    "-compose",
    f"subject='[𝐠𝐢𝐥𝐥𝐞𝐬𝐰𝐞𝐞𝐤𝐥𝐲] Gilles' week {week_id}',"
    f"to='veronique.hoste@ugent.be',"
    f"bcc='gilles.jacobs92@gmail.com',"
    f"body='{body}',"
    f"from='gillesm.jacobs@ugent.be'",
]
subprocess.Popen(cmd, close_fds=True)
