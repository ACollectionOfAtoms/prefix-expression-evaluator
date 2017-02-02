# Solved with Python 2.7.10
## Installation
`pip2 install -r requirements.txt`
(for pytest and argparser)
## Usage
`python2 app.py -file {path to file}`
### Example (included):
`python2 app.py -file test/test_file.txt`
## Testing
`pytest test`
## Assumptions:
- We assume we will always be given a valid prefix expression:
	>"You are given a prefix expression".

- We assume only a small subset of possible operators will be used:
`*`, `/` and `+`
