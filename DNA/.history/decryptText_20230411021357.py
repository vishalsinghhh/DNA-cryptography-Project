original_str = input("What would you like to convert? ")

n = 3
chunks = [original_str[i:i+n] for i in range(0, len(str), n)]