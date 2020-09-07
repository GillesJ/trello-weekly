#!/usr/bin/env python3
"""
Contains Trello API keys and board + list IDs.
You can obtain an API key from https://trello.com/app-key.
You can obtain the id of your board and list by browsing to the desired board and appending .json to the url.
This will return a json with all board (meta)data.
e.g. `https://trello.com/b/N0taR34lHsh/my-board` > `https://trello.com/b/N0taR34lHsh/my-board.json`

secrets.example.py
trelloweeklyoverview 
2/5/20
Copyright (c) Gilles Jacobs. All rights reserved.  
"""
API_KEY = "UR-API-KEY-N0taR34lHsh"
API_SECRET = "UR-API-SECRET-N0taR34lHsh"

LIST_IDS = [
    "UR-LIST-ID-1",
    "UR-LIST-ID-2",
]

EMAIL_FROM = "your.address-to-send-from@domain.tld" # address from which to send email
EMAIL_TO = "reciptient.address@domain.tld" # address of recipient
EMAIL_BCC = "bcc.address@ugent.be" # bcc address