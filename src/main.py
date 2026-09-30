"""Main application module.

Provides a simple data‑processing function used by the test suite.
"""

def process_data(data):
    """Process a list of numbers and return their sum.

    Args:
        data (list[int]): List of integers to sum.

    Returns:
        int: The sum of the provided numbers.
    """
    # Ensure we are working with an iterable of numbers
    if not isinstance(data, (list, tuple)):
        raise TypeError("data must be a list or tuple of numbers")
    return sum(data)

if __name__ == "__main__":
    # Simple manual test when the module is executed directly
    sample = [1, 2, 3]
    print(f"Sum of {sample} is {process_data(sample)}")
