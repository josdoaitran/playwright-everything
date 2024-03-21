# Summary 
2 ways to setup
- Reference Document: https://playwright.dev/python/docs/intro

## Using local python
- Requirements:
    + We will use Python 3.
    + Update pip by this command: `pip install --upgrade pip` 
    + Install `pytest-playwright` by this command: `pip install pytest-playwright`.
    + Install `playwright` by this command: `pip install playwright`.
or We can install via requirement.txt: `pip install -r requirements.txt`
    + Install required browsers for Playwright: `playwright install`

## Using Python virtual environment

```
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Switch Python configuration on Pycharm
Thank to Pycharm Interpreter feature, we can configure the proper Python Interpreter easily.

## Check Playwright version after install on Python environment
- Run this command: ```playwright --version```
- Result:
```angular2html
❯ playwright --version
Version 1.42.0/
```
## Playwright install Browser:
To install Playwright Chromenium, WebKit
```angular2html
Playwright install
```
# Basic Python Playwright

## launch a browser with Synchronous and Asynchronous 
