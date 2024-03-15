import math


class RangeError(Exception):
    """Custom exception for invalid range."""
    pass


class SquareGenerator:
    def generate_squares(self, start, end):
        """
        Generate a list of squares for a given range of numbers.

        Parameters:
            start (int): The starting number of the range (inclusive).
            end (int): The ending number of the range (inclusive).

        Returns:
            list: A list of squares for the given range of numbers.
        """
        if end < start:
            raise RangeError("End of the range must be greater than or equal to the start.")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):
        """
        Calculate the square roots of each number in the list.

        Parameters:
            numbers (list): List of numbers.

        Returns:
            list: List of square roots of each number.
        """
        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots


def main():
    square_gen = SquareGenerator()

    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    try:
        squares = square_gen.generate_squares(start, end)
        print(f"List of squares from {start} to {end}:")
        print(squares)

        square_roots = square_gen.calculate_square_roots(squares)
        print("Square roots of each number:")
        print(square_roots)

    except RangeError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
