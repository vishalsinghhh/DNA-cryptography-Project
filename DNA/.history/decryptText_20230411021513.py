original_str = str(input("What would you like to convert? "))

n = 4
chunks = [original_str[i:i+n] for i in range(0, len(original_str), n)]
