# VerveBridge-ML-Internship
This is a collection all the solutions of all the tasks that are given in the Machine Learning Internship by VerveBridge

-----------------------------------------------------------------------TASK - 1 : BOOK RECOMMENDATION SYSTEM-------------------------------------------------------------------------------

Overview: This project is a book recommendation system that uses machine learning algorithms to suggest books to users based on their reading preferences. The system is built using Python and utilizes popular libraries such as Pandas, Matplotlib, Seaborn, and Scikit-learn for data analysis and visualization. The system is deployed using Flask, a lightweight web framework, and Flask-CORS for cross-origin resource sharing.

Workflow:
1) Data Exploration and Analysis (EDA)
2) Data Preprocessing
3) Model Building
4) Database Integration
5) API and Web Interface
6) Logging and Error Handling

Environment: To run this project, you need to create a Conda environment with the following specifications:

Environment File: environment.yml

Channels:

defaults
Dependencies:

python
pandas
matplotlib
seaborn
scikit-learn
flask
flask_cors
Prefix: C:\Users\PythonCoding\Anaconda3\envs\Book-Rec-env

How to Run: To run the project, follow these steps:

Create a new Conda environment using the environment.yml file: conda env create -f environment.yml
Activate the environment: conda activate Book-Rec-env
Navigate to the project directory: cd path/to/project/directory
Run the Flask application: python app.py
Open a web browser and navigate to http://localhost:5000 to access the book recommendation system.

Features: The book recommendation system provides the following features:
Book search and filtering
Personalized book recommendations based on user preferences
Visualization of user reading habits and book ratings

Dataset download link : https://gist.github.com/jaidevd/23aef12e9bf56c618c41

Contributing: If you'd like to contribute to this project, please fork the repository and submit a pull request. You can also report any issues or suggest new features by creating an issue in this repository.

-----------------------------------------------------------------------TASK - 2 : ML PRICE NEGOTIATOR CHATBOT SYSTEM-----------------------------------------------------------------------

Here's a concise overview and project structure for your `README.md` file:

---

# Price Negotiator Ecommerce Chatbot

The **Price Negotiator Ecommerce Chatbot** is an intelligent system designed to simulate real-world price negotiations in an e-commerce environment. Utilizing natural language processing (NLP), the chatbot engages with users, understanding their queries and bargaining intents, and provides a dynamic price adjustment experience. The system integrates various services, including a product catalog, order management, and price negotiation logic, all orchestrated to enhance the online shopping experience.

## Key Features
- **Natural Language Processing:** Understands user inputs to negotiate prices.
- **Dynamic Pricing:** Adjusts product prices based on negotiation strategies.
- **Product Catalog Management:** Maintains and queries available products.
- **Order Management:** Handles order placements and updates.
- **Modular Design:** Organized into independent services for scalability and ease of maintenance.

## Project Structure

Price-Negotiator-Ecommerce-Chatbot/
├── app.py                         # Main application entry point
├── nlp_service.py                 # Handles natural language processing tasks
├── price_negotiation_service.py   # Contains the logic for price negotiations
├── product_catalog_service.py     # Manages the product catalog
├── order_management_service.py    # Manages orders and transactions
├── database.py                    # Handles database connections and queries
├── models.py                      # Defines data models
├── tests.py                       # Unit and integration tests
├── product_catalog.csv            # CSV file with product data
├── database.db                    # SQLite database file
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation (this file)

---

This structure and description will help users quickly understand the purpose of your project and navigate the codebase.

----------------------------------------------------------------------------TASK - 3 : CAMPUS PLACEMENT PREDICTION ------------------------------------------------------------------------

Here's a comprehensive README overview for your GitHub repository:

---

# Campus Placement Prediction

## Overview

This project aims to predict whether a student will be placed in a campus recruitment drive based on various academic and extracurricular factors. Leveraging machine learning models, we developed a predictive system that assists in understanding the factors contributing to campus placements.

## Features

- **Multiple ML Models**: Logistic Regression, Decision Tree, and Random Forest models have been trained and evaluated.
- **Web Interface**: A user-friendly web application where users can input student data and receive placement predictions.
- **Feature Engineering**: Implemented advanced feature engineering techniques to enhance model performance.
- **Scalable and Modular Code**: The project follows a modular structure, making it easy to maintain and extend.

## Dataset

The dataset used for training includes the following columns:
- `sl_no`: Serial Number
- `gender`: Gender of the student (Male=0, Female=1)
- `ssc_p`: Secondary Education percentage (10th Grade)
- `ssc_b`: Board of Education (Central/State)
- `hsc_p`: Higher Secondary Education percentage (12th Grade)
- `hsc_b`: Board of Education (Central/State)
- `hsc_s`: Specialization in Higher Secondary Education
- `degree_p`: Degree Percentage
- `degree_t`: Type of Undergrad Degree (Science/Commerce/Others)
- `workex`: Work Experience (Yes/No)
- `etest_p`: E-test Percentage
- `specialisation`: Post Graduate Specialization (Marketing & HR/Finance)
- `mba_p`: MBA Percentage
- `status`: Placement Status (Placed/Not Placed)
- `salary`: Salary offered to the student

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/campus-placement-prediction.git
    cd campus-placement-prediction
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

## Usage

- **Web Interface**: Open your browser and navigate to `http://127.0.0.1:5000/`. Enter the required student details and hit "Predict" to see the placement prediction.
- **Model Evaluation**: The `evaluate.py` script can be used to evaluate the performance of the trained models.

## Project Structure

- `app.py`: Main application file for the Flask web server.
- `model.py`: Contains code for training and saving the ML models.
- `feature_engineering.py`: Script for feature engineering and preprocessing.
- `evaluate.py`: Script for evaluating the trained models.
- `templates/`: Contains the HTML templates for the web interface.
- `static/`: Contains the CSS files for styling the web interface.
- `requirements.txt`: Lists all the Python dependencies required to run the project.
