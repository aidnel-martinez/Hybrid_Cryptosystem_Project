# Imports from pycryptodome for DES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import pandas as pd

# Define DES encryption and decryption functions
def des_encrypt(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(message.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def des_decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    return decrypted_text.decode()

# Rotor Machine class (already provided by user)
class RotorMachine: 
    def __init__(self):
        self.abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.rotors = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'BDFHJLCPRTXVZNYEIWGAKMUSQO']
        self.rotation_counters = [0, 0, 0]

    def rotate(self, index):
        self.rotors[index] = self.rotors[index][1:] + self.rotors[index][0]
        self.rotation_counters[index] += 1

        if (self.rotation_counters[0] == 26):
            self.rotation_counters[0] = 0
            self.rotate(1)
        elif (self.rotation_counters[1] == 26):
            self.rotation_counters[1] = 0
            self.rotate(2)
    
    def single_letter_encrypt(self, letter):
        for rotor in self.rotors:
            letter = rotor[self.abc.find(letter)]
        self.rotate(0)
        return letter
    
    def encrypt_message(self, message):
        encryption = ""
        for letter in message:
            if self.abc.find(letter.upper()) == -1:
                pass
            else: 
                encryption += self.single_letter_encrypt(letter.upper())
        return encryption
    
    def single_letter_decrypt(self, letter):
        for rotor in reversed(self.rotors):
            letter = self.abc[rotor.find(letter)]
        self.rotate(0)
        return letter
    
    def decrypt_message(self, message):
        decryption = ""
        for letter in message:
            if self.abc.find(letter.upper()) == -1:
                pass
            else: 
                decryption += self.single_letter_decrypt(letter.upper())
        return decryption

# Setup DES key and messages
key = get_random_bytes(8)  # DES key must be 8 bytes
messages = ["HOW ARE YOU", "HAPPY NEW YEAR", "WELCOME TO PUERTO RICO"]

# Hybrid encryption and decryption with rotor machine reset for each operation
results = []

# Hybrid process with rotor machine reinitialization for each message
for message in messages:
    # Step 1: Rotor Machine Encryption (E1)
    rotorMachine = RotorMachine()  # Initialize a fresh rotor machine for each message
    E1 = rotorMachine.encrypt_message(message)
    
    # Step 2: DES Encryption (E2)
    E2 = des_encrypt(E1, key)
    
    # Step 3: DES Decryption (D1)
    D1 = des_decrypt(E2, key)
    
    # Step 4: Rotor Machine Decryption (D2)
    rotorMachine = RotorMachine()  # Reinitialize rotor machine to initial state
    D2 = rotorMachine.decrypt_message(D1)
    
    # Append results to the list
    results.append((message, E1, E2.hex(), D1, D2))

# Display results in a table format
df = pd.DataFrame(results, columns=["Original Information (M)", "E1", "E2 (Hex)", "D1", "D2"])
print(df)