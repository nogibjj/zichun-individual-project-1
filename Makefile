install:
    pip install -r requirements.txt

test:
    pytest --nbval notebooks/descriptive_stats.ipynb
    pytest tests/test_script.py tests/test_lib.py

format:
    black src/

lint:
    ruff check src/ tests/
