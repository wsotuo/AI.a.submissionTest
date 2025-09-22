def main():
    first_name = input("Enter your first name: ")
    reversed_name = first_name[::-1]
    print(f"Your name in reverse is: {reversed_name}")
    count()

def count():
    print("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    print("Great")

if __name__ == "__main__":
    main()