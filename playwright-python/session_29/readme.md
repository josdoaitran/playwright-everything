# Report HTML Allure Report
https://allurereport.org/

# Install Allure on your computer
- Window: https://allurereport.org/docs/install-for-windows/
- Mac: https://allurereport.org/docs/install-for-macos/

# Install Python library
```angular2html
pip install allure-pytest
```

# Generate report allure when run pytest
```angular2html
pytest -v -s --alluredir=./allure-results
allure generate
allure serve allure-results
```

## More parametters:

--clean-alluredir
If set, the directory specified by --alluredir will be cleaned before generating new test results.
```angular2html
pytest -v -s --alluredir=./allure-results --clean-alluredir
```
--clean:
to generate new allure-report
``````
allure generate --clean