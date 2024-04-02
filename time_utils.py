from time import time
from functools import wraps


def format_seconds_to_hms(seconds):
    """Converts seconds to a formatted string in hours:minutes:seconds."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours)}:{int(minutes):02d}:{int(seconds):02d}"


def formatted_runtime(start_time, end_time):
    """Prints the total elapsed runtime in a human-readable format."""
    total_time = end_time - start_time
    formatted_time = format_seconds_to_hms(total_time)
    print("\n** Total Elapsed Runtime:", formatted_time)


def print_elapsed_time(func):
    """Decorator to measure the execution time of a function."""

    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)  # Call the original function
        end_time = time()
        formatted_runtime(start_time, end_time)
        return result

    return wrapper
