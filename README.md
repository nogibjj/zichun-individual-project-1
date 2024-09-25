# Individual Project #1: Continuous Integration of Python Data Science Project

This project demonstrates continuous integration (CI) using GitLab Actions, performing descriptive statistics with Polars and Pandas.

## Project Structure

- `notebooks/descriptive_stats.ipynb`: Jupyter Notebook for stats.
- `src/main.py`: Script for Polars and Pandas.
- `src/lib.py`: Shared code library.
- `tests/`: Contains test scripts.
- `Makefile`: Automates testing, formatting, and linting.

## Usage

1. Install dependencies:
    ```bash
    make install
    ```

2. Run tests:
    ```bash
    make test
    ```

3. Format code:
    ```bash
    make format
    ```

4. Lint code:
    ```bash
    make lint
    ```

## CI/CD Pipeline

The GitLab pipeline runs tests, formatting, and linting automatically.
