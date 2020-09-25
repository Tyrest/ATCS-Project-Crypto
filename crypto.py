ascii_A = ord('A')
ascii_Z = ord('Z')
import random
import math

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypted = ""
    offset = offset % 26
    for ch in plaintext:
        ascii_ch = ord(ch)
        if ascii_A <= ascii_ch <= ascii_Z:
            ascii_ch += offset
            if ascii_ch > ascii_Z:
                ascii_ch -= 26
        encrypted += chr(ascii_ch)
    return encrypted

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    return encrypt_caesar(ciphertext, -(offset))

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encrypted = ''
    key = (len(plaintext)//len(keyword) + 1)*keyword
    key = key[:len(plaintext)]

    for i in range(len(plaintext)):
        encrypted += encrypt_caesar(plaintext[i], ord(key[i]) - ascii_A)
    
    return encrypted

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    new_keyword = ''
    for char in keyword:
        new_keyword += chr(ascii_Z-ord(char)+ascii_A+1)
    return encrypt_vigenere(ciphertext, new_keyword)

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    W = [random.randint(1, 10)]
    for i in range(n):
        W.append(random.randint(sum(W) + 1, sum(W) * 2))
    Q = random.randint(sum(W) + 1, sum(W) * 2)
    R = random.randint(2, Q-1)
    while math.gcd(R, Q) != 1:
        R = random.randint(2, Q-1)
    return (tuple(W), Q, R)

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: B - a length-n tuple of integers
def create_public_key(private_key):
    W, Q, R = private_key
    B = []
    for i in W:
        B.append(R*i%Q)
    return tuple(B)

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, B):
    encrypted = []

    for ch in plaintext:
        A = list(bin(ord(ch))[2:])
        A = (len(B) - len(A)) * [0] + A
        C = []
        for i in range(len(A)):
            C.append(int(A[i]) * int(B[i]))
        encrypted.append(sum(C))
    
    return encrypted

# Returns modular inverse of r mod m using Euclidean Algorithm.
def mod_inverse(r, m):
    r_seq = [r,m]
    s_seq = [1,0]
    while r_seq[len(r_seq)-1] != 0:
        i = len(r_seq)-1
        q_i = int(r_seq[i-1]/r_seq[i])
        r_seq.append(r_seq[i-1]%r_seq[i])
        s_seq.append(s_seq[i-1]-q_i*s_seq[i])
    return s_seq[len(s_seq)-2] % m
    
# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    W, Q, R = private_key
    S = mod_inverse(R,Q)


def main():
    # print(encrypt_caesar('PYTHON!*(@#&!$(!()$    . . .. . ', 55))
    # print(decrypt_caesar('SBWKRQ!*(@#&!$(!()$    . . .. .', 55))
    # print(encrypt_vigenere('ATTACKATDAWN', 'LEMON'))
    # print(decrypt_vigenere('LXFOPVEFRNHR', 'LEMON'))
    private_key = generate_private_key()
    print(private_key)
    public_key = create_public_key(private_key)
    print(public_key)
    encrypted = encrypt_mhkc("HELLO", public_key)
    print(encrypted)
    print(mod_inverse(3,29))
    # Testing code here

if __name__ == '__main__':
    main()
