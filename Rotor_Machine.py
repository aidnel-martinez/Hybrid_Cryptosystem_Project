class RotorMachine: 
    def __init__(self):
        self.abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.rotors = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'BDFHJLCPRTXVZNYEIWGAKMUSQO']
        self.rotation_counters = [0, 0, 0]

    def rotate(self, index):
        self.rotors[index] = self.rotors[index][1:] + self.rotors[index][0]
        self.rotation_counters[index] += 1

        if (self.rotation_counters[0]==26):
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
    
    def encrypt_whole_message(self, message):
        encryption = ""
        for letter in message:
            if (self.abc.find(letter.upper()) == -1):
                pass
            else: 
                encryption += self.single_letter_encrypt(letter.upper())
        
        return encryption

    def decrypt_message(self, message):
        pass


# Run code

message1 = "Hello World"
rotorMachine = RotorMachine()

print("Encrypted Message: ", rotorMachine.encrypt_whole_message(message1))
        