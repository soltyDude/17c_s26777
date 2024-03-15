def generate_squares():
    # Generate a list of squares using list comprehension
    squares = [x**2 for x in range(1, 11)]
    return squares

def main():
    squares = generate_squares()
    # Print the list of squares
    print("List of squares from 1 to 10:")
    print(squares)

if __name__ == "__main__":
    main()