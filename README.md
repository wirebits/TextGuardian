# TextGuardian
A simple tool that encodes and decodes text using a password in .txt files.

# Key Features
- It can encode and decode text.
- It can work with text and `.txt` files.
- It lock/unlock the text with a password.

# Setup
- Make sure that the latest python is installed on your system (Windows/Linux/MacOS).

# Parameters
| Parameter | Usage                                    |
|-----------|------------------------------------------|
| -e        | Set the tool to encode the input.        |
| -d        | Set the tool to decode the input.        |
| -p        | Password of text or `.txt` files.        |
| -i        | Text or `.txt` file to encode or decode. |
| -o        | The `.txt` file that stores output.      |
| -h        | Show help message and exit from tool.    |

# Note
- While using text as input, put your text inside `""`.
- Give any name you want to the output `.txt` file.

# Install
1. Download or Clone the Repository.
2. Open the folder.
3. Open CMD/Powershell (Windows) or Terminal (Linux/MacOS) in that folder.

# Run
- It supports both text and `.txt` files.
## With Text
### Encode the text

```
python TextGuardian.py -e -p <PASSWORD> -i "Text" -o <ENCRYPTED-OUTPUT-FILE>.txt
```
### Decode the text

```
python TextGuardian.py -d -p <PASSWORD> -i <ENCRYPTED-OUTPUT-FILE>.txt -o <DECRYPTED-OUTPUT-FILE>.txt
```
## With `.txt` file
### Encode the `.txt` file

```
python TextGuardian.py -e -p <PASSWORD> -i <ORIGINAL-TXT-FILE>.txt -o <ENCRYPTED-OUTPUT-TXT-FILE>.txt
```
### Decode the `.txt` file

```
python TextGuardian.py -d -p <PASSWORD> -i <ENCRYPTED-OUTPUT-TXT-FILE>.txt -o <DECRYPTED-OUTPUT-TXT-FILE>.txt
```
