from cubic_generator import CubicGenerator

def main():
    cubic_gen = CubicGenerator()

    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    try:
        squares = cubic_gen.generate_squares(start, end)
        print(f"List of squares from {start} to {end}:")
        print(squares)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
