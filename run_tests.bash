coverage run --source=./src -m pytest tests/test_files_search.py
coverage report -m
coverage html -d tests/html_report
