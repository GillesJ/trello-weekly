# Trello weekly report
Python script for generating a nice weekly report of your activity cards in Trello.
Opens Thunderbird email-client with the email ready, if you have it installed.

## Requirements and install
- Trello API keys and the identifiers of the specific board and lists to report should be place in `secrets.py`.
  - You can obtain an API key from https://trello.com/app-key.
  - You can obtain the id of your board and list by browsing to the desired board and appending `.json` to the Trello.com url.
 This will return a json with all board (meta)data, e.g. `https://trello.com/b/N0taR34lHsh/my-board > https://trello.com/b/N0taR34lHsh/my-board.json`. The board id is the value for the top-level "id" key. The list ids can be found in the top-level "lists" key where the "id" key contains contains the value for each lists, manually select the relevant lists to report.
  - Paste your API key + board and list ids in `secrets.py.template`, and email info for the relevant variables, then rename `secrets.py.template` > `secrets.py`.
- Python >3.6 + packages:
  - install with `pipenv install -r requirements.txt` or `pip install -r requirements.txt`
    - pytrello
    - isoweek 
- Thunderbird email client (optional)

## Usage and output
`python makeoverview.py`

```
Activities Week <WEEK-NR> (START-DATE-WEEK)

Mon:
	• Label1: Item 1.
	• Label2: Item 2.

...

Fri:
	• Label1: Item 3.
	• Label3: Item 4.
```

### TODO
- [ ] Add language options for flavour text.
- [ ] Add command-line interface with argument options.