# Python 3 program to print all
# possible strings of length k
     
# The method that prints all
# possible strings of length k.
# It is mainly a wrapper over
# recursive function printAllKLengthRec()
def printAllKLength(set, k):
 
    n = len(set)
    printAllKLengthRec(set, "", n, k)
 
# The main recursive method
# to print all possible
# strings of length k
list1=[]
dict = {}
def printAllKLengthRec(set, prefix, n, k):
     
    # Base case: k is 0,
    # print prefix
    
    if (k == 0) :
        
        print(prefix)
        list1.append(prefix)
        return
 
    # One by one add all characters
    # from set and recursively
    # call for k equals to k-1
    for i in range(n):
 
        # Next character of input added
        newPrefix = prefix + set[i]
         
        # k is decreased, because
        # we have added a new character
        printAllKLengthRec(set, newPrefix, n, k - 1)
 
# Driver Code
if __name__ == "__main__":
     
    print("First Test")
    set1 = ['A', 'G', 'C', 'T']
    k = 4
    printAllKLength(set1, k)
     
    # print("\nSecond Test")
    # set2 = ['a', 'b', 'c', 'd']
    # k = 1
    # printAllKLength(set2, k)
    list2=['20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2A', '2B', '2C', '2D', '2E', '2F', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3A', '3B', '3C', '3D', '3E', '3F', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4A', '4B', '4C', '4D', '4E', '4F', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5A', '5B', '5C', '5D', '5E', '5F', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6A', '6B', '6C', '6D', '6E', '6F', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A', '7B', '7C', '7D', '7E']
    for i in range(0, len(list2)):
        dict[list2[i]]=i
    print(dict)
 
# This code is contributed
# by ChitraNayal