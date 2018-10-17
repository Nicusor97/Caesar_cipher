import argparse

#Function to encode a file
def encode(plaintext, key):
    """Function to encode a file, with a provided key"""
    key %= 26
    encrypted = ""
    file_to_encode = open(plaintext)
    while True:
        i = file_to_encode.read(1)
        if not i:
            break
        if not i.isalpha(): #if i is not a letter(i.e punctuation)
            encrypted += i
            continue
        elif 65 <= ord(i) <= 90:
            if key + ord(i) <= 90:
                encrypted += chr(ord(i) + key)
            elif key + ord(i) > 90:
                encrypted += chr(ord(i) + key - 26)
        elif 97 <= ord(i) <= 122:
            if key + ord(i) <= 122:
                encrypted += chr(ord(i) + key)
            elif key + ord(i) > 122:
                encrypted += chr(ord(i) + key - 26)
    return encrypted

#Function to decode a file
def decode(ciphertext):
    """Function to decode a file, giving all possible options"""
    file_to_decode = open(ciphertext, 'r')
    decrypted = ""
    decrypted += 'Original encoding is:\n' +  file_to_decode.read()
    decrypted += '\n'
    file_to_decode.seek(0)
    for key in range(1, 26):
        decrypted += '*** Number of shifts: ' + str(key) +  ' ***\n'
        while True:
            i = file_to_decode.read(1)
            if not i:
                break
            elif not i.isalpha():
                decrypted += i
                continue
            if 65 <= ord(i) <= 90: #i is between A and Z
                if key + ord(i) <= 90:
                    decrypted += chr(key + ord(i))
                elif key + ord(i) > 90:
                    decrypted += chr(key + ord(i) - 26)
            elif 97 <= ord(i) <= 122: #i is between a and z
                if key + ord(i) <= 122:
                    decrypted += chr(ord(i) + key)
                elif key + ord(i) > 122:
                    decrypted += chr(ord(i) + key - 26)
            else:
                continue
        file_to_decode.seek(0)
    return decrypted

def main():
    """main function"""
    parser = argparse.ArgumentParser(description='Caesar Cipher program')
    group = parser.add_mutually_exclusive_group(required=True)
    #add encode option
    group.add_argument('-e', dest='encode', action='store_true', help='Give a file to encode.')
    #add decode option
    group.add_argument('-d', dest='decode', action='store_true', help='Give a file to decode.')
    #add key option
    parser.add_argument('key', type=int, nargs='?', help='Key for encoding')
    #pass filename
    parser.add_argument('filename', type=str, help='The file to decode or encode')

    args = parser.parse_args()
    if args.encode:
        integer_key = int(args.key)
        if (integer_key < 0):
            print "Key must be > 0"
            exit(1)
        encrypted_file = open('encrypted.txt', 'w')
        encrypted_file.write(encode(args.filename, integer_key))
        print "encrypted.txt file created"
    elif args.decode:
        decoded_file = open('decrypted.txt', 'w')
        decoded_file.write(decode(args.filename))
        print "decrypted.txt file created"

    exit()

if __name__ == "__main__":
    main()