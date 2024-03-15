from Square_Generator import square_generator


class CubicGenerator(square_generator):
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
            raise ValueError("End of the range must be greater than or equal to the start.")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares
