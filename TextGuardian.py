# TextGuardian
# A tool that encodes and decodes text using a password in .txt files.
# Author - WireBits

import base64
import argparse

def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="TextGuardian", description="A tool that encodes and decodes text using a password in .txt files.", epilog="Developed by WireBits")
    parser.add_argument("-e", "--encode", action="store_true", help="Encode the input text")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode the input text")
    parser.add_argument("-p", "--key", required=True, help="Key to encode/decode the text")
    parser.add_argument("-i", "--input", required=True, help="Input string or text file")
    parser.add_argument("-o", "--output", required=True, help="Output file to store the result")

    args = parser.parse_args()

    if args.encode:
        if args.input.endswith('.txt'):
            with open(args.input, 'r') as file:
                message = file.read()
        else:
            message = args.input
        result = Encode(args.key, message)
    elif args.decode:
        if args.input.endswith('.txt'):
            with open(args.input, 'r') as file:
                message = file.read()
        else:
            message = args.input
        result = Decode(args.key, message)

    with open(args.output, "w") as file:
        file.write(result)
    print(f"Text has been written to {args.output}!")