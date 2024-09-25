test-notebook:
  pytest --nbval descriptive_stats.ipynb

lint:
  ruff check src/ tests/

format:
  black src/ tests/

install:
  pip install -r requirements.txt

test-all:
  pytest tests/ test_script.py test_lib.py --nbval descriptive_stats.ipynb
