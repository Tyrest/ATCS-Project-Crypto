ascii_a = ord('a')
ascii_z = ord('z')
ascii_A = ord('A')
ascii_Z = ord('Z')

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypted = ""
    offset = offset % 26
    for ch in plaintext:
        ascii_ch = ord(ch)
        if ascii_a < ascii_ch < ascii_z:
            ascii_ch += offset
            if ascii_ch > ascii_z:
                ascii_ch -= 26
        if ascii_A < ascii_ch < ascii_Z:
            ascii_ch += offset
            if ascii_ch > ascii_Z:
                ascii_ch -= 26
        encrypted += chr(ascii_ch)
    return encrypted

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    return encrypt_caesar(ciphertext, 26 - (offset))

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encrypted = ''
    key = (len(plaintext)//len(keyword) + 1)*keyword
    key = key[:len(plaintext)]

    for i in range(len(plaintext)):
        encrypt_caesar(plaintext[i], ord(key[i]) - ascii_A) 



# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    print(encrypt_caesar('pytHON!*(@#&!$(!()$    . . .. . ', 55))
    print(decrypt_caesar('sbwKRQ!*(@#&!$(!()$    . . .. .', 55))
    # Testing code here
    pass

if __name__ == '__main__':
    main()
