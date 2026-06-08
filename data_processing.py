def process_data(values):
    """Normalize and summarize a list of numeric values."""
    cleaned_values = []
    for value in values:
        if value is None:
            continue
        if isinstance(value, bool):
            raise TypeError("Boolean values are not supported")
        if isinstance(value, (int, float)):
            cleaned_values.append(float(value))
            continue
        raise TypeError(f"Unsupported value type: {type(value).__name__}")

    if not cleaned_values:
        return {"count": 0, "sum": 0.0, "average": 0.0}

    total = sum(cleaned_values)
    return {
        "count": len(cleaned_values),
        "sum": total,
        "average": total / len(cleaned_values),
    }
