#Imports from library pycryptodome
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Define a function for DES encryption
def des_encrypt(message, key):
    # Initialize a DES cipher object in ECB(Electronic CodeBook)mode with the provided key
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Pad the message to make its length a multiple of the block size (8 bytes for DES)
    padded_text = pad(message.encode(), DES.block_size)
    
    # Encrypt the padded message
    encrypted_text = cipher.encrypt(padded_text)
    
    return encrypted_text

# Define a function for DES decryption
def des_decrypt(encrypted_text, key):
    # Initialize a DES cipher object in ECB(Electronic CodeBook) mode with the same key
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Decrypt the encrypted message and then remove the padding
    decrypted_text = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    
    # Decode the decrypted text from bytes to a string
    return decrypted_text.decode()

# Using an 8-byte key for DES (DES keys must be strictly 8 bytes)
key = get_random_bytes(8)  # Generating a random 8-byte key for encryption and decryption

# Initial messages
messages = ["HOPE", "HELLO", "NEW YEAR"]

# Creating a list to store results
results = []

# Encrypt and decrypt each message
for message in messages:
    # Encrypt the message
    encrypted_text = des_encrypt(message, key)
    
    # Decrypt the message to verify the encryption process
    decrypted_text = des_decrypt(encrypted_text, key)
    
    # Append the results as a tuple (original message, encrypted text, decrypted text)
    results.append((message, encrypted_text, decrypted_text))

# Displaying the results
import pandas as pd  # We use pandas to display results in a table format

# Creating a DataFrame to organize results in a structured format with columns
df = pd.DataFrame(results, columns=["Initial Information", "Encrypted Text", "Decrypted Text"])

# Printing the DataFrame to display the original message, encrypted text, and decrypted text
print(df)