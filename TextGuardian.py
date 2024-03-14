# TextGuardian
# A tool that encodes and decodes text using a password in .txt files.
# Author - WireBits

import base64

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
    import argparse
    parser = argparse.ArgumentParser(description="TextGuardian")
    parser.add_argument("mode", choices=["e", "d"], help="Select mode: e for encode or d for decode")
    parser.add_argument("key", help="Key to encode/decode the text")
    parser.add_argument("input", help="Input string or text file")
    parser.add_argument("output_file", help="Output file to store the result")

    args = parser.parse_args()

    if args.mode == "e":
        if args.input.endswith('.txt'):
            with open(args.input, 'r') as file:
                message = file.read()
        else:
            message = args.input
        result = Encode(args.key, message)
    elif args.mode == "d":
        if args.input.endswith('.txt'):
            with open(args.input, 'r') as file:
                message = file.read()
        else:
            message = args.input
        result = Decode(args.key, message)

    with open(args.output_file, "w") as file:
        file.write(result)

    print(f"Text has been written to {args.output_file}!")
