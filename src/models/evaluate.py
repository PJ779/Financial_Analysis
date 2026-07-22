from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
)

def classification_metrics(y_true, y_pred, y_prob):

    """
    Calculate classification evaluation metrics.

    Parameters
    ----------
    y_true : array-like
    y_pred : array-like
    y_prob : array-like, optional
        Predicted probabilities for the positive class.

    Returns
    -------
    dict
    """

    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1_score": f1_score(y_true, y_pred),
        "confusion_matrix": confusion_matrix(y_true, y_pred),
    }

    if y_prob is not None:
        metrics["roc_auc"] = roc_auc_score(y_true, y_prob)

    return metrics