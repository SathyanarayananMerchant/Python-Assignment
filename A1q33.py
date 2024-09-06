def process_numbers():
    input_string = input("Enter a sequence of comma-separated numbers: ")
    
    numbers = input_string.split(',')
    
    numbers_tuple = tuple(numbers)
    
    print(numbers)
    print(numbers_tuple)

process_numbers()
