from square_generator import SquareGenerator, RangeError

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
