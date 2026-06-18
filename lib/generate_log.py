from datetime import datetime

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("data must be a list")
