def generate_squares(start, end):
    """
    Generate a list of squares for a given range of numbers.

    Parameters:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Returns:
        list: A list of squares for the given range of numbers.
    """
    squares = [x**2 for x in range(start, end + 1)]
    return squares

def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    squares = generate_squares(start, end)
    print(f"List of squares from {start} to {end}:")
    print(squares)

if __name__ == "__main__":
    main()
