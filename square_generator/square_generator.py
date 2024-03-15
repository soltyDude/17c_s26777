import math


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
            print("Error: End of the range must be greater than or equal to the start.")
            return None

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
