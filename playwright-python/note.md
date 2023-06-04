- Reference Document: https://playwright.dev/python/docs/intro
- Requirements:
    + We will use Python 3.
    + Install `pytest-playwright` by this command: `pip install pytest-playwright`.
 (If we use `pypenv`, we should follow these command:
 
 - `brew install pyenv`
 - Install Python version that we want to work: `pyenv install 3.6.6`
 - Create a virtual python environment, and set the name: demo-env: `pyenv virtualenv 3.6.6 demo-env`
 - We go to our project and run this command: `cd ~/playwright-python` and `pyenv local demo-env`
 - We can test: `$ python --version` # Test the new env
=> result: Python 3.6.6 # Bingo`
 - We can install via requirement.txt: `pip install -r requirements.txt` 
 )   
    + Install required browsers for Playwright: `playwright install`