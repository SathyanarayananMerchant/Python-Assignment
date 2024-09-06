def compute_net_amount():
    balance = 0

    print("Enter transactions (D for deposit, W for withdrawal). Press Ctrl+D (or Ctrl+Z on Windows) to end input.")
    
    try:
        while True:
            line = input()
            if line.strip(): 
                transaction_type, amount = line.split()
                amount = int(amount)
                
                if transaction_type == 'D':
                    balance += amount
                elif transaction_type == 'W':
                    balance -= amount
                else:
                    print(f"Unknown transaction type: {transaction_type}")
    except EOFError:
        pass

    print(balance)

compute_net_amount()
