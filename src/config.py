from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DATA = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"
VISUALIZATION_DATA = PROJECT_ROOT / "data" / "processed_signal"
MODELS = PROJECT_ROOT / "models"
REPORTS = PROJECT_ROOT / "reports"
FIGURES = REPORTS / "figures"
LOG_COLUMNS = [
    "Volume",
    "ADX",
]
YEO_COLUMNS = [
    'upper_shadow_ratio', 'lower_shadow_ratio', 'VROC',
]