def is_disk_usage_high(used_percent: int, threshold: int = 80) -> bool:
    if not isinstance(used_percent, int):
        raise ValueError("used_percent must be int")

    if used_percent < 0 or used_percent > 100:
        raise ValueError("used_percent must be between 0 and 100")

    return used_percent >= threshold
