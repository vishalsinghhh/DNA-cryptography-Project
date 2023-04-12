import time
import random
from PIL import Image


# Mapping scheme for DNA sequence
dna_map = {
    '00': 'AT',
    '01': 'AG',
    '10': 'TA',
    '11': 'CG'
}

# Function to convert binary data to DNA sequence
def binary_to_dna(binary_data):
    dna_sequence = ''
    for i in range(0, len(binary_data), 2):
        dna_sequence += dna_map[binary_data[i:i+2]]
    return dna_sequence


# Function to convert DNA sequence to binary data
def dna_to_binary(dna_sequence):
    binary_data = ''
    for i in range(0, len(dna_sequence), 2):
        for key, value in dna_map.items():
            if dna_sequence[i:i+2] == value:
                binary_data += key
                break
    return binary_data


def encrypt_image(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()

    binary_data = ''
    for byte in image_data:
        binary_data += format(byte, '08b')

    dna_sequence = binary_to_dna(binary_data)

    with open('Encrypted_DNA.txt', 'w') as f:
        f.write(dna_sequence)


def decrypt_image(file_path):

    with open(file_path, 'r') as f:
        dna_sequence = f.read()
    binary_data = dna_to_binary(dna_sequence)

    image_data = b''
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        image_data += int(byte, 2).to_bytes(1, 'big')

    with open('Decrypted_image.jpg', 'wb') as f:
        f.write(image_data)

# Example usage
encrypt_image('kat.jpg')
decrypt_image('Encrypted_DNA.txt')

end = time.time()
print(end - start)