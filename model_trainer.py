import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib # for saving and loading the model

def train_churn_model(data_path='ecommerce_customer_data.csv', model_path='churn_model.pkl'):
    df = pd.read_csv(data_path)

    # Define features (X) and target (y)
    # Features that are good indicators of churn (based on typical RFM analysis)
    numerical_features = ['total_spent', 'num_orders', 'recency_days', 'avg_order_value']
    # Categorical features
    categorical_features = ['product_category_pref', 'marketing_channel']
    target = 'is_churn'

    X = df[numerical_features + categorical_features]
    y = df[target]

    # Preprocessing pipelines for numerical and categorical features
    numerical_transformer = StandardScaler() # Scale numerical features
    categorical_transformer = OneHotEncoder(handle_unknown='ignore') # Convert categorical to numerical

    # Create a preprocessor using ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Create the full pipeline: Preprocessing + Model
    model_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                     ('classifier', LogisticRegression(solver='liblinear', random_state=42))])

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Train the model
    print("Training model...")
    model_pipeline.fit(X_train, y_train)
    print("Model training complete.")

    # Evaluate the model (for your internal checks)
    accuracy = model_pipeline.score(X_test, y_test)
    print(f"Model Accuracy on test set: {accuracy:.2f}")

    # Save the trained model
    joblib.dump(model_pipeline, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_churn_model()