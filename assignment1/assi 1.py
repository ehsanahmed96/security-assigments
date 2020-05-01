import re
import sys
class  ClassicalCiphers :
    plainText =[]
    cipherText = []
    def __init__(self ,  cipherName ,  typeOperation , inputFile , outputFile , keys):
       self.cipherName = cipherName

       self.typeOperation = typeOperation
       self.inputFile = \
           inputFile
       self.outputFile = outputFile
       self.keys = keys
    def writeCipher(self):
        i = 0

        with open('output.txt', 'w') as f:

                f.write(''.join(self.cipherText))




    def readPlainText(self):
        with open(self.inputFile) as f:

          lines = f.read().split("\n")

          self.plainText = []
        for i in range(len(lines)):
           self.plainText .extend(re.split("\s+|_+|,+" ,lines[i] ))
        return self.plainText
    def encrShift(self):
        self.readPlainText()
        for i in range(len(self.plainText)):
            resultc = ""

            text = self. plainText[i]
            for j in range(len(text)):
               char = text[j]
               if(char.isupper()):

                   resultc += chr((ord(char) + int(self.keys[0]) - 65) % 26 + 65)
               else :
                   resultc += chr((ord(char) + int(self.keys[0] )- 97) % 26 + 97)
            self.cipherText.extend(resultc + " ")

        self.writeCipher()

    def decrShift(self):
        self.readPlainText()
        for i in range(len(self.plainText)):


            resultc = ""

            text = self.plainText[i]
            for j in range(len(text)):
                char = text[j]
                if (char.isupper()):

                    resultc += chr((ord(char) - int(self.keys[0]) - 65) % 26 + 65)
                else:
                    resultc += chr((ord(char) -int( self.keys[0]) - 97) % 26 + 97)
            self.cipherText.extend(resultc + " ")

        self.writeCipher()

    def  encrAffineCp(self):
        self.readPlainText()
        for i in range(len(self.plainText)):

            text = self.plainText[i].upper()
            cipher = ''.join(chr(((int(self.keys[0]) * (ord(t) - ord('A')) + int(self.keys[1])) % 26)
                                + ord('A')) for t in text.upper())



            if(not self.plainText[i].isupper()):
              self.cipherText.extend(cipher.lower() + " ")
            else:
                self.cipherText.extend(cipher + " ")

        self.writeCipher()

    def egcd(self , a, b ):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y

    def modinv(self,a ):
        gcd, x, y = self.egcd(a, 26)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % 26

    def affine_decrypt(  self):
        self.readPlainText()
        for i in range(len(self.plainText)):

          text = self.plainText[i].upper()

          cipher = ''.join([chr(((self.modinv(int(self.keys[0])) * (ord(c) - ord('A') -int( self.keys[1])))
                             % 26) + ord('A')) for c in text])
          if (not self.plainText[i].isupper()):
              self.cipherText.extend(cipher.lower() + " ")
          else:
              self.cipherText.extend(cipher + " ")
        self.writeCipher()

    def generateKey(self ,text, key):
        key = list(key)
        if len(text) == len(key):
            return (key)
        else:
            for i in range(len(text) -
                           len(key)):
                key.append(key[i % len(key)])
        return ("".join(key))

        # This function returns the

    # encrypted text generated
    # with the help of the key
    def vigenereEnc(self, key):
        self.readPlainText()
        self.cipherText = []
        for i in range(len(self.plainText)):
          text = self.plainText[i]

          key = self.generateKey(text , key)

          cipher_text = []
          for i in range(len(text)):
            x = (ord(text[i]) +
                 ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
          cipher = ("".join(cipher_text))
          self.cipherText.extend(cipher)

        self.writeCipher()

    def vigenereDE(self ,  key):
        self.plain_text = []
        self.readPlainText()
        for i in range(len(self.plainText)):
            text = self.plainText[i].upper()
            key = self.generateKey(text, key)

            orig_text = []
            for i in range(len(text)):
              x = (ord(text[i]) -
                 ord(key[i]) + 26) % 26
              x += ord('A')
              orig_text.append(chr(x))
            plain =  ("".join(orig_text))
            self.cipherText.extend(plain)
        self.writeCipher()


if __name__ == "__main__":
    print("when you especify the type of cipher type  s  for shift-cipher  and type a for affine and type v for vigenere")
    cipherName = sys.argv[1]
    typeOperation = sys.argv[2]
    inputFile = sys.argv[3]
    outputFile = sys.argv[4]
     # b = sys.argv[6]


    keys = []
    if cipherName == 's':
        keys = []
        a = sys.argv[5]
        keys.extend(a)
        keys = keys
        #keys.append(a)
        p = ClassicalCiphers(cipherName, typeOperation, inputFile, outputFile, keys)

        if (typeOperation == 'e'):
            p.encrShift()
        else:
            p.decrShift()
    elif cipherName =='a':
        a = sys.argv[5]
        b = sys.argv[6]
        keys.extend(a)
        keys.extend(b)
        #keys.append(a)
        #keys.append(b)
        p = ClassicalCiphers(cipherName, typeOperation, inputFile, outputFile, keys)

        if (typeOperation == 'e'):
            p.encrAffineCp()
        else:
            p.affine_decrypt()
    else:
        key = sys.argv[5]
        keys = []
        keys.extend(key)
        p = ClassicalCiphers(cipherName, typeOperation, inputFile, outputFile, keys)
        if (typeOperation == 'e'):
            p.vigenereEnc()
        else:
            p.vigenereDE()



    #p.readPlainText()
    p.vigenereDE(keys[0])


