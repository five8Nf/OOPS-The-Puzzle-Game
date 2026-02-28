from inputimeout import inputimeout, TimeoutOccurred

try:
    user_input = inputimeout(prompt='You have 5 seconds to enter something: ', timeout=5)
    print(f'Input received: {user_input}')
except TimeoutOccurred:
    print('Timeout occurred: No input received within the time limit.')
    user_input = None # Assign a default value or handle the timeout case
