original_str = input("What would you like to convert? ")

ascii_list = []
for i in original_str:
    ascii_list.append(ord(i))

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}
hex_list=[]

for i in hex_list:
   while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16