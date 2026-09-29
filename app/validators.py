"""Simple input validation functions."""


def get_non_empty_text(prompt):
    """Keep asking until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This value cannot be blank. Please try again.")


def get_menu_choice(prompt, minimum, maximum):
    """Return a whole number within the given inclusive range."""
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if minimum <= number <= maximum:
                return number
            print(f"Enter a number from {minimum} to {maximum}.")
        except ValueError:
            print("Please enter a whole number.")

