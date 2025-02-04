# Project 0: Setup, Numpy Exercises, Tutorial on Common Packages

## Introduction

The purpose of this project is to set up Python environment for working on Unit 0 part on MITx 6.86x Machine Learning with Python-From Linear Models to Deep Learning.

## Setup Instructions

Follow these steps to set up your Python environment:

### 1. Install Python 3.11 using `pyenv`

First, ensure you have `pyenv` installed. Then, run:

```sh
pyenv install 3.11
```

This command installs Python 3.11 on your system.

### 2. Create a new project directory

Navigate to a suitable location and create a new directory for this unit:

```sh
mkdir project0
cd project0/
```

This directory will serve as your working space for the project.

### 3. Set the Python version for the project

Inside the newly created directory, set the Python version using:

```sh
pyenv local 3.11
```

This ensures that Python 3.11 is used within this directory.

### 4. Initialize the project using Poetry

Poetry is a dependency management tool for Python projects. Initialize it by running:

```sh
poetry init
```

You will be prompted to enter details such as:

- Package name
- Version
- Description
- Author name
- License
- Compatible Python versions

For simplicity, you can accept the defaults by pressing _Enter_ or modify them as needed. When prompted about defining dependencies interactively, choose `n` (no).

### 5. Confirm the project setup

Once the details are entered, Poetry will generate a `pyproject.toml` file. Confirm the generation by selecting `yes`.

### 6. Create and activate a virtual environment

Run the following command to set up a virtual environment using the Python version specified in `pyenv`:

```sh
poetry env use $(pyenv which python)
```

This ensures that Poetry creates and manages an isolated environment for your project.

### 7. Add a custom package source

You will be working with PyTorch, so you need to add a custom source for installation. Run:

```sh
poetry source add --priority supplemental torch_cu118 https://download.pytorch.org/whl/cu118/
```

This adds the PyTorch package source with CUDA 11.8 support.

### 8. Install dependencies

Now, install the required dependencies for this project:

```sh
poetry add torch
poetry add numpy matplotlib scipy tqdm scikit-learn
```

These packages will be used throughout the course for numerical computing, machine learning, and data visualization.

## Conclusion

Your Python environment is now set up! You have successfully installed Python 3.11, created a virtual environment, and installed the necessary dependencies using Poetry. You are now ready to start working on the assignments for this course.

If you encounter any issues, refer to the documentation for `pyenv`, `poetry`, and the respective Python libraries for troubleshooting.
