#Flux Flow - AI-Powered Customer Churn Predictor (MVP)

## 🚀 Overview

The **Flux Flow AI-Powered Customer Churn Predictor** is a Minimum Viable Product (MVP) designed to demonstrate the core functionality of identifying customers at high risk of churning from e-commerce businesses. Built with Python, Scikit-learn, and Flask, this solution aims to empower Small and Medium E-commerce Businesses (SMEs) to proactively retain valuable customers, reduce acquisition costs, and boost Lifetime Value (LTV).

## ✨ Problem Solved

E-commerce SMEs often struggle with customer churn due to:
* Lack of specialized data analytics tools.
* Inability to predict customer behavior proactively.
* High costs associated with acquiring new customers vs. retaining existing ones.

Our solution addresses this by providing an affordable and easy-to-use platform that predicts churn, allowing businesses to implement targeted retention strategies before it's too late.

## 💡 Core Features (MVP)

* **Simulated E-commerce Data Generation:** Creates realistic customer purchase history data.
* **AI-Powered Churn Prediction:** Utilizes a trained Machine Learning model to calculate churn probability.
* **Simple Web Interface:** A Flask-based web application to input customer data and visualize predictions.
* **Clear Churn Status:** Provides "High Churn Risk" or "Low Churn Risk" status along with probability.

## 🏗️ Architecture & How It Works

The MVP follows a simple, yet effective architecture:

1.  **`data_simulator.py`**: Generates a synthetic dataset (`ecommerce_customer_data.csv`) mimicking key e-commerce metrics (Total Spent, Number of Orders, Recency, etc.) and labels customers as "churned" or "not churned."
2.  **`model_trainer.py`**: Loads the simulated data, preprocesses it (scaling numerical features, one-hot encoding categorical features), trains a Logistic Regression model to predict `is_churn`, and saves the trained model (`churn_model.pkl`).
3.  **Flask Web Application (`app.py`, `templates/index.html`, `static/style.css`)**:
    * Loads the pre-trained `churn_model.pkl`.
    * Serves a user-friendly HTML form (`index.html`) where users can input customer parameters.
    * Processes the input data, feeds it to the loaded ML model, and returns the churn prediction and probability to the web interface.
    * Styled with a modern and colorful CSS (`style.css`) for an enhanced user experience.

## 🛠️ Technologies Used

* **Python 3.x**
* **Pandas:** Data manipulation and analysis.
* **NumPy:** Numerical operations.
* **Scikit-learn:** Machine Learning model training (Logistic Regression, StandardScaler, OneHotEncoder, ColumnTransformer, Pipeline, train_test_split).
* **Flask:** Web framework for the application.
* **Joblib:** For saving and loading the ML model.
* **HTML, CSS, JavaScript:** For the user interface.

## 🚀 Getting Started (Installation & Setup)

Follow these steps to get the AI Churn Predictor MVP up and running on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone [Your-Repository-URL]
    cd [your-repository-name]
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install pandas numpy scikit-learn flask joblib
    ```

4.  **Generate Sample Data:**
    This script creates `ecommerce_customer_data.csv`.
    ```bash
    python data_simulator.py
    ```

5.  **Train the Machine Learning Model:**
    This script trains the model and saves it as `churn_model.pkl`.
    ```bash
    python model_trainer.py
    ```

6.  **Run the Flask Web Application:**
    ```bash
    python app.py
    ```

## 🌐 Usage

1.  After running `app.py`, open your web browser and navigate to:
    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```
2.  You will see a form. Fill in the customer details (you can use the default values or enter your own simulated data).
3.  Click the "Get Prediction" button.
4.  The "Prediction Results" section will update with the churn status (High/Low Risk) and the churn probability.

## 🛣️ Future Enhancements & Roadmap

This MVP is just the beginning. Our vision for [Your Company Name] includes:

* **Direct E-commerce Integrations:** Seamlessly connect with platforms like Shopify, WooCommerce, Magento via APIs.
* **Comprehensive Dashboard:** A full analytical dashboard showing overall churn rate, customer segments, and trends.
* **Automated Recommendations:** AI-driven suggestions for personalized retention campaigns.
* **CRM/Marketing Tool Integration:** Connect with popular CRM and marketing automation platforms.
* **Predictive LTV & Product Recommendations:** Expanding insights beyond churn.

## 📞 Contact

For any questions or collaborations, feel free to reach out:

* **[Pendela Vyshnavi**
* **Email:** [vyshnavipendela7gmail.com]
* **LinkedIn:** [https://www.linkedin.com/in/vyshnavi-pendela-b8a007328/]

---
