from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        """
        Generate a list of squares for a given range of numbers.

        Parameters:
            start (int): The starting number of the range (inclusive).
            end (int): The ending number of the range (inclusive).

        Returns:
            list: A list of squares for the given range of numbers.
        """
        pass

    def calculate_square_roots(self, numbers):
        """
        Calculate the square roots of each number in the list.

        Parameters:
            numbers (list): List of numbers.

        Returns:
            list: List of square roots of each number.
        """
        square_roots = [num**0.5 for num in numbers]
        return square_roots
