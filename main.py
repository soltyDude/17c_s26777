from Square_Generator import square_generator

def main():
    square_gen = square_generator()

    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    squares = square_gen.generate_squares(start, end)
    if squares is not None:
        print(f"List of squares from {start} to {end}:")
        print(squares)

        square_roots = square_gen.calculate_square_roots(squares)
        print("Square roots of each number:")
        print(square_roots)

if __name__ == "__main__":
    main()
