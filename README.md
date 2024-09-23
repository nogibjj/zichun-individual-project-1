
# Zichun individual Project 1

## Project Overview

This project demonstrates Continuous Integration (CI) with GitLab Actions. It includes:
- A Python Data Science project using Polars or Pandas for descriptive statistics.
- Automated testing of the Jupyter Notebook using `nbval`.
- CI pipeline for linting, formatting, and testing.

## Project Structure

The repository contains the following key files:
- **Jupyter Notebook**: A notebook performing descriptive statistics using Polars or Pandas.
- **Makefile**: Automates tasks such as testing, linting, formatting, and installing dependencies.
- **test_script.py**: Contains unit tests for the Python script.
- **test_lib.py**: Contains tests for any library used in the project.
- **requirements.txt**: Contains the pinned dependencies for the project.
- **GitLab Actions**: The CI pipeline is configured to:
   - Run tests.
   - Format code using `black`.
   - Lint code using `Ruff`.


## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/chun77/zichun-individual-project-1.git
cd zichun-individual-project-1
```

### 2. Install Dependencies

You can install the required Python dependencies by running:

```bash
make setup
```

This will install all the packages listed in `requirements.txt`.

### 3. Running the Linter

To ensure your code follows proper Python style guidelines, run:

```bash
make lint
```

This will run `pylint` on the `src/main.py` file.

### 4. Running Tests

To run the unit tests using `pytest`, use the following command:

```bash
make test
```

The `Makefile` is set up to run the tests in the `tests/` directory.

## Usage Instructions

The project contains a simple `add` function and a main script. You can run the main script as follows:

```bash
python src/main.py
```

The `main.py` file will print "Hello, world!" when executed.

## CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration (CI). The workflow is defined in the `.github/workflows/ci.yml` file and runs automatically on every push to the main branch. The CI performs the following actions:
- Linting with `pylint`
- Running unit tests with `pytest`

## Development Environment with Devcontainer

A development container is included to ensure consistency in development environments. The `.devcontainer` folder contains a `Dockerfile` and `devcontainer.json` file for setting up the containerized development environment in tools like Visual Studio Code.
