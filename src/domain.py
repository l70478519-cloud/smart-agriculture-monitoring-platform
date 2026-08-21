def evaluate(value: float, threshold: float = 50.0) -> dict:
    if value < 0 or threshold <= 0: raise ValueError("invalid values")
    ratio=round(value/threshold,3)
    return {"ratio":ratio,"flagged":value>=threshold,"reason":"threshold reached" if value>=threshold else "within expected range"}
