# Medical Data Visualizer

A Python-based project that provides a simple and intuitive interface for
visualizing medical data. This is one of the projects used in the Data Analysis course on Free Code Camp. 

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Requirements](#requirements)
4. [Project Structure](#project-structure)
5. [Usage](#usage)

## Introduction

This project is designed to help medical professionals visualize and
analyze medical data. It provides a simple and intuitive interface for
visualizing data in the form of heatmaps and categorical plots.

## Getting Started

To get started with this project, follow these steps:

1. Install the required dependencies by running `pip install -r
requirements.txt` in the project directory.
2. Create a virtual environment using `python -m venv venv` in the project
directory.
3. Activate the virtual environment using `source venv/bin/activate` on
Linux/Mac or `venv\Scripts\activate` on Windows.
4. Clone the repository or download the files manually.
5. Run the script using `python main.py` to start the application.

## Requirements

The following dependencies are required to run this project:

* Python 3.8+
* NumPy
* Pandas
* Matplotlib
* Seaborn

## Project Structure

The project is structured as follows:

* `examples`: A folder containing example usage of the application.
* `main.py`: The main script that runs the application.
* `medical_data_visualizer.py`: The script that contains the data
visualizer functionality.
* `medical_examination.csv`: A sample dataset used to demonstrate the
application.
* `requirements.txt`: A file listing the dependencies required to run the
project.
* `test_module.py`: A test script used to test the application.
* `venv`: A virtual environment directory.

## Usage

To use this project, follow these steps:

1. Run `python main.py` to start the application.
2. The application will display a prompt asking for the file path of the
CSV file to be visualized.
3. Enter the file path and click "Load" to load the data.
4. The application will display a heatmap and categorical plot based on
the data.
5. The user can interact with the plot by zooming, panning, and hovering
over the data points.