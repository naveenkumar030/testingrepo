# src/app.py

def process_data(data):
    """Process the input data and return the transformed result.

    Args:
        data (list[int]): A list of integers to be processed.

    Returns:
        list[int]: A new list where each element is doubled.
    """
    # Simple example transformation: double each number
    return [item * 2 for item in data]

if __name__ == "__main__":
    sample = [1, 2, 3]
    print(process_data(sample))
