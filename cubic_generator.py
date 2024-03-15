from Square_Generator import square_generator


class RangeError(Exception):
    """Custom exception for invalid range."""
    pass


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
            raise RangeError("End of the range must be greater than or equal to the start.")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares


def main():
    cubic_gen = CubicGenerator()

    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    try:
        squares = cubic_gen.generate_squares(start, end)
        print(f"List of squares from {start} to {end}:")
        print(squares)

    except RangeError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
