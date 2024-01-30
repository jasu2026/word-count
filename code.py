def get_user_input():
    # Function to get user input for a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")
    return user_input

def count_words(text):
    # Function to count the number of words in the input text
    words = text.split()
    return len(words)

def display_output(word_count):
    # Function to display the word count to the console
    print(f"Word count: {word_count}")

def word_counter():
    try:
        # Attempt to execute the following code
        input_text = get_user_input()

        # Check if the input is empty and raise a ValueError if true
        if not input_text:
            raise ValueError("Input cannot be empty.")

        # Count words in the input text
        word_count = count_words(input_text)

        # Display the word count
        display_output(word_count)

    except ValueError as e:
        # Handle ValueError by printing an error message
        print(f"Error: {e}")

if __name__ == "__main__":
    # Execute the word_counter function if the script is run
    word_counter()
