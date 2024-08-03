import json

def get_response(user_input, responses):
    # Get the response from JSON file or default message
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

def main():
    # Load the JSON file
    with open('responses.json', 'r') as file:
        responses = json.load(file)

    while True:
        # Get user input
        user_input = input("Type something (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        # Get and print the response
        response = get_response(user_input, responses)
        print(response)

if __name__ == "__main__":
    main()
