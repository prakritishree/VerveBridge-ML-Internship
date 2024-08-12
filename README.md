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

## Project Structure

CampusPlacementPrediction/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── SampleSubmission.csv
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── train.py
│   └── evaluate.py
│
├── notebooks/
│   └── EDA.ipynb
│
├── models/
│   └── model.pkl
│
├── logs/
│   └── app.log
│
├── tests/
│   ├── __init__.py
│   └── test_model.py
│
├── requirements.txt
└── README.md
