# Effect of Music on Mental Health

![music and mental Health](music_and_mental_health.gif)

## Introduction

> This project aims to investigate the relationship between music and mental health. We will be looking at how different types of music can affect an individual's mood and overall psychological well-being. The dataset from [Kaggle](https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results)
>
> The ultimate goal is to gain a better understanding of the ways in which music can be used as a tool to promote mental health and well-being. We hope that the insights gained from this project will be useful for individuals looking to incorporate music into their self-care routines, as well as for professionals working in the field of mental health.

## Hypothesis

> Music can have an effect on mental health

## Project Objectives

1. Determine whether music has effect on mental health

2. Collect and clean data using `siuba` and `pandas`

3. Manipulate the data the R way with `siuba`

4. Visualize the result with `seaborn` and `Plotly`

5. Build a dashboard to tell the story in the data with `h2o_wave`

## Project Description

### Step 1: Get data from Kaggle

In this step, we will be downloading the data for our project from Kaggle, which is a website that hosts a wide variety of datasets for machine learning and data analysis. Depending on the specific data that we are using for our project, we may need to create a Kaggle account and accept any relevant terms and conditions before being able to access the data.

### Step 2: Clean data(available in the `music_effect_on_mental.ipynb` file)

After downloading the data, the next step will be to clean it up and prepare it for analysis. This may involve tasks such as removing duplicates, filling in missing values, and ensuring that all of the data is in a consistent format. We will be using the siuba and pandas libraries to perform these tasks, which are both popular libraries for data manipulation and analysis in Python.

### Step 3: Manipulate and analyze the data using `siuba` and `pandas` (available in the `music_effect_on_mental.ipynb` file)

Once the data is cleaned and ready to go, we will start manipulating and analyzing it using the same libraries (siuba and pandas) that we used in step 2. This may involve tasks such as filtering the data to only include certain rows or columns, calculating summary statistics, or creating new columns based on existing data. We

### Step 4: Visualize the result with `seaborn` and `Plotly` (available in the `music_effect_on_mental.ipynb` file)

After analyzing the data, we will use the seaborn and Plotly libraries to create visualizations of the results. These visualizations will help us to better understand the patterns and trends in the data, and will also be useful for presenting our findings to others.

### Step 5: Build a dashboard to present your finds using `h2o_wave` (available in the `src` folder)

In the final step of the project, we will use the h2o_wave library to build a dashboard to present our findings. A dashboard is a user-friendly interface that allows users to interact with and explore the data and results of our analysis. We will be using [h2o_wave](https://wave.h2o.ai/), which is a fast and simple dashboard tool for Python created by [h2o.ai](https://h2o.ai/)

## Running the project(Dashbord)

Once we have completed all of the above steps and built the dashboard, we will be ready to run the project and share our findings with others. To run the dashboard, do the following:

1. create a virtual environment with the command:

```bash
python3 -m venv .myenv
```

2. Activate the virtual environment

```bash
source .myenv/bin/activate
```

3. Navigate to the `src` folder and run:

```bash
wave run app_grid.py
```

4. Point your browser to `http://localhost:10101` to view the app.
