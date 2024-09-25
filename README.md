# Individual Project #1: Continuous Integration of Python Data Science Project

This project performs descriptive statistics and generates visualizations using both Pandas and Polars on an Olympic medals dataset. The CI/CD pipeline automates testing, formatting, and executing the Jupyter notebook, and commits any updates automatically.

## Features

1. Descriptive Statistics:

- Performed using both Pandas and Polars.
- Statistics include count, mean, median, standard deviation, min, max, and percentiles.

2. Data Visualization:

- A bar chart is generated for the total medals won by the top 50 countries.
3. CI/CD Pipeline:

- Automatically runs tests, linting, formatting, and Jupyter notebook execution.
- If changes are detected in the Jupyter notebook, it is automatically committed.

## Instructions

1. Clone the Repository:
    ```bash
    git clone <repo-url>
    cd <repo-directory>
    ```

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Running the Makefile Commands:
    ```bash
   make test    # Run all tests (notebook, script, and lib)
   make format  # Format code with Black
   make lint    # Lint code with Ruff
    ```

4. Running the Jupyter Notebook:
    ```bash
    jupyter notebook notebooks/descriptive_stats.ipynb
    ```

5. CI/CD Pipeline

The CI/CD pipeline automatically runs the notebook and commits any changes to the repository.
