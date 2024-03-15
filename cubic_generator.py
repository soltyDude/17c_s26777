from Square_Generator import square_generator

class CubicGenerator(square_generator):
    def generate_cubes(self, start, end):
        """
        Generate a list of cubes for a given range of numbers.

        Parameters:
            start (int): The starting number of the range (inclusive).
            end (int): The ending number of the range (inclusive).

        Returns:
            list: A list of cubes for the given range of numbers.
        """
        cubes = [x**3 for x in range(start, end + 1)]
        return cubes

def main():
    cubic_gen = CubicGenerator()

    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    squares = cubic_gen.generate_squares(start, end)
    print(f"List of squares from {start} to {end}:")
    print(squares)

    square_roots = cubic_gen.calculate_square_roots(squares)
    print("Square roots of each number:")
    print(square_roots)

    cubes = cubic_gen.generate_cubes(start, end)
    print(f"List of cubes from {start} to {end}:")
    print(cubes)

if __name__ == "__main__":
    main()
