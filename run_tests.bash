coverage run --source=./src -m pytest tests/test.py
coverage report -m
coverage html -d tests/html_report
