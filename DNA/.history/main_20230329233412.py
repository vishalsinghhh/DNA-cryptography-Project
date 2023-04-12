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

DNA_encoding = {'20': 'AAAA', '21': 'AAAG', '22': 'AAAC', '23': 'AAAT', '24': 'AAGA', '25': 'AAGG', '26': 'AAGC', '27': 'AAGT', '28': 'AACA', '29': 'AACG', '2A': 'AACC', '2B': 'AACT', '2C': 'AATA', '2D': 'AATG', '2E': 'AATC', '2F': 'AATT', '30': 'AGAA', '31': 'AGAG', '32': 'AGAC', '33': 'AGAT', '34': 'AGGA', '35': 'AGGG', '36': 'AGGC', '37': 'AGGT', '38': 'AGCA', '39': 'AGCG', '3A': 'AGCC', '3B': 'AGCT', '3C': 'AGTA', '3D': 'AGTG', '3E': 'AGTC', '3F': 'AGTT', '40': 'ACAA', '41': 'ACAG', '42': 'ACAC', '43': 'ACAT', '44': 'ACGA', '45': 'ACGG', '46': 'ACGC', '47': 'ACGT', '48': 'ACCA', '49': 'ACCG', '4A': 'ACCC', '4B': 'ACCT', '4C': 'ACTA', '4D': 'ACTG', '4E': 'ACTC', '4F': 'ACTT', '50': 'ATAA', '51': 'ATAG', '52': 'ATAC', '53': 'ATAT', '54': 'ATGA', '55': 'ATGG', '56': 'ATGC', '57': 'ATGT', '58': 'ATCA', '59': 'ATCG', '5A': 'ATCC', '5B': 'ATCT', '5C': 'ATTA', '5D': 'ATTG', '5E': 'ATTC', '5F': 'ATTT', '60': 'GAAA', '61': 'GAAG', '62': 'GAAC', '63': 'GAAT', '64': 'GAGA', '65': 'GAGG', '66': 'GAGC', '67': 'GAGT', '68': 'GACA', '69': 'GACG', '6A': 'GACC', '6B': 'GACT', '6C': 'GATA', '6D': 'GATG', '6E': 'GATC', '6F': 'GATT', '70': 'GGAA', '71': 'GGAG', '72': 'GGAC', '73': 'GGAT', '74': 'GGGA', '75': 'GGGG', '76': 'GGGC', '77': 'GGGT', '78': 'GGCA', '79': 'GGCG', '7A': 'GGCC', '7B': 'GGCT', '7C': 'GGTA', '7D': 'GGTG', '7E': 'GGTC'}
