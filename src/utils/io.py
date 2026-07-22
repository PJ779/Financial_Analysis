import joblib
import pandas as pd
from pathlib import Path

def save_model(model, filepath: str | Path = "models/model.joblib",) -> Path:
    """Saves a trained model object to disk."""
    # Ensure directory exists
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, filepath)
    print(f"Model saved to {filepath}")
    return filepath

def load_model(filepath: str | Path = "models/model.joblib"):
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"No model found at {filepath}")
    model = joblib.load(filepath)

    return model

def save_predictions(predictions, filepath: str | Path = "models/model.joblib") -> Path:
    """Saves model predictions to CSV or Parquet."""
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert list/array to DataFrame if necessary
    if not isinstance(predictions, pd.DataFrame):
        df = pd.DataFrame({"prediction": predictions})
    else:
        df = predictions
        
    df.to_csv(filepath, index=False)
    return filepath

def load_predictions(filepath: str | Path = "models/model.joblib") -> pd.DataFrame:
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"No predictions found at {filepath}")

    return pd.read_csv(filepath)