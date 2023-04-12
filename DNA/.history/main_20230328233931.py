
# set variable with input text
original_str = input("What would you like to convert? ")

# convert text to binary values
binary_str = ''.join(format(x, '08b') for x in bytearray(original_str, 'utf-8'))

binary_list = [binary_str[i: i+2] for i in range(0, len(binary_str), 2)]