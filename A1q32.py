def convert_to_uppercase():
    print("Enter your text. Press Ctrl+D (or Ctrl+Z on Windows) to end input.")
    lines = []
    try:
        
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    for line in lines:
        print(line.upper())

convert_to_uppercase()
