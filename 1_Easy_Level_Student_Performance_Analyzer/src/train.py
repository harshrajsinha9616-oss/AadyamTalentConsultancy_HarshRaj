import os
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

def get_path(filename, folder):
    """
    Returns the absolute path for outputs relative to project root.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, folder)
    os.makedirs(target_dir, exist_ok=True)
    return os.path.join(target_dir, filename)

def train_predictor_model(df):
    """
    Trains a Ridge regression model to predict the average_score of a student
    using categorical demo features. Saves model to models/ and metrics to outputs/.
    """
    print("\nStarting Machine Learning Model Pipeline Training...")
    
    # Define features and target
    features = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
    target = 'average_score'
    
    X = df[features]
    y = df[target]
    
    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Dataset split: {len(X_train)} training samples, {len(X_test)} testing samples.")
    
    # Preprocessor using OneHotEncoder
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), features)
        ]
    )
    
    # Create training pipeline
    model_pipeline = Pipeline(
        steps=[
            ('preprocessor', preprocessor),
            ('regressor', Ridge(alpha=1.0))
        ]
    )
    
    # Train model
    model_pipeline.fit(X_train, y_train)
    print("Model pipeline fitted successfully.")
    
    # Evaluate model
    y_pred = model_pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    metrics = {
        "mean_squared_error": float(mse),
        "r2_score": float(r2),
        "training_samples": len(X_train),
        "testing_samples": len(X_test)
    }
    
    print("Model Evaluation Metrics:")
    print(f" - Mean Squared Error (MSE): {mse:.4f}")
    print(f" - R-squared (R2): {r2:.4f}")
    
    # Save model pipeline
    model_path = get_path("student_performance_model.pkl", "models")
    joblib.dump(model_pipeline, model_path)
    print(f"Trained model saved to: {model_path}")
    
    # Save evaluation metrics
    metrics_path = get_path("evaluation_metrics.json", "outputs")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=4)
    print(f"Evaluation metrics saved to: {metrics_path}")
    
    return model_pipeline
