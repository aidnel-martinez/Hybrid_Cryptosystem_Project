class RotorMachine: 

    # Initialize the Rotor Machine
    def __init__(self):
        self.abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.rotors = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'BDFHJLCPRTXVZNYEIWGAKMUSQO']
        self.rotation_counters = [0, 0, 0]

    # Handling rotors rotations
    def rotate(self, index):
        self.rotors[index] = self.rotors[index][1:] + self.rotors[index][0]
        self.rotation_counters[index] += 1

        if (self.rotation_counters[0]==26):
            self.rotation_counters[0] = 0
            self.rotate(1)
        elif (self.rotation_counters[1] == 26):
            self.rotation_counters[1] = 0
            self.rotate(2)
    
    # Encrypt a single letter
    def single_letter_encrypt(self, letter):
        for rotor in self.rotors:
            letter = rotor[self.abc.find(letter)]

        self.rotate(0)
        return letter
    
    # Call Single letter encryption for every char in the message
    def encrypt_message(self, message):
        encryption = ""
        for letter in message:
            if (self.abc.find(letter.upper()) == -1):
                pass
            else: 
                encryption += self.single_letter_encrypt(letter.upper())
        
        return encryption
    
    # Decrypt a single letter
    def single_letter_decrypt(self, letter):
        for rotor in reversed(self.rotors):
            letter = self.abc[rotor.find(letter)]

        self.rotate(0)
        return letter
    
    # Call single letter decryption for every char in the message
    def decrypt_message(self, message):
        decryption = ""
        for letter in message:
            if (self.abc.find(letter.upper()) == -1):
                pass
            else: 
                decryption += self.single_letter_decrypt(letter.upper())
        
        return decryption


# Run code
message = input("Enter some text: ")
rotorMachine = RotorMachine()
encrypted_msg = rotorMachine.encrypt_message(message)

rotorMachine = RotorMachine() # Have to re-initialize the rotor machine for effective decryption
decrypted_msg = rotorMachine.decrypt_message(encrypted_msg)
print("Encrypted Message: ", encrypted_msg)
print("")
print("Decrypted Message: ", decrypted_msg)