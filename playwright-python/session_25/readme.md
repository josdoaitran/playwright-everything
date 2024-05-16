# Optimization ways
- Filter resources
- Parallel executions
Install: pip install pytest-xdist
Run:
pytest --numprocesses auto
pytest -n 3 (Number of workers)