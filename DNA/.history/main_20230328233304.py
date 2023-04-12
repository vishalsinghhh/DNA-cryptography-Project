# set variable with input text
original_str = input("What would you like to convert? ")

def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 

DNA_encoding = {
    "00": "A",
    "01": "G",
    "10": "C",
    "11": "T"
} 
# DNA_list = []

# for num in binary_list:
#     for key in list(DNA_encoding.keys()):
#         if num == key:
#             DNA_list.append(DNA_encoding.get(key))

# DNA_str = "".join(DNA_list)


# # print input text, binary code and DNA sequence
# print("\nThe original string is :" + "\n" + original_str + "\n")
# print("The string after binary conversion is :" + "\n" + binary_str + "\n")
# print("The string represented by single-letter codes is :" + "\n" + DNA_str + "\n")