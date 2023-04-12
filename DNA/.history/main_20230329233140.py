original_str = input("What would you like to convert? ")

ascii_list = []
for i in original_str:
    ascii_list.append(ord(i))

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}
hex_list = []

for i in ascii_list:
    hexadecimal = ''
    while(i > 0):
        remainder = i % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        i = i // 16
    hex_list.append(hexadecimal)
print(hex_list)

DNA_encoding = {
    '20', '21', '22', '23', '24', '25', '26', '27, '28':'AACA', '29':'AACG', '2A':'AACC', '2B':'AACT', '2C':'AATA', '2D':'AATG', '2E':'AATC', '2F':'AATT', '30':'AGAA', '31':'AGAG', '32':'AGAC', '33':'AGAT', '34':'AGGA', '35':'AGGT', '36':'AGCA', '37', '38', '39', '3A', '3B', '3C', '3D', '3E', '3F', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4A', '4B', '4C', '4D', '4E', '4F', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5A', '5B', '5C', '5D', '5E', '5F', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6A', '6B', '6C', '6D', '6E', '6F', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A', '7B', '7C', '7D', '7E'
}
