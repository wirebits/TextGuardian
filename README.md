# TextGuardian
A tool that encodes and decodes text using a password in .txt files.

<h1>Setup</h1>
Make sure the python is installed on your system (Windows/Linux/MacOS).<br>

<h1>Tested Systems</h1>
The tool is currently tested on : <br>
1. Windows (10)<br>
The testing is going on different systems.

# Parameters
There are 5 parameters after command ```python``` (windows) or ```python3``` (Linux) : <br>
1. TextGuardian.py - The tool file.<br>
2. <b>e</b> / <b>d</b> - <b>e</b> for Encode and <b>d</b> for Decode.<br>
3. key - The password set on the text.<br>
4. "Text" / test.txt - The string / .txt file want to encode / decode.<br>
5. output_file.txt - The encoded / decoded text is store in that .txt file.<br>
While using string, put your text inside "".<br>
For example, if you want to encode ```Hello``` then, ```"Hello"```.<br>
Give any name you want to that output_file.<br>

<h1>Install and Run</h1>
1. Download or Clone the Repository.<br>
2. Open the folder.<br>
3. Open CMD/Powershell (Windows) or Terminal (Linux) in that folder.<br>
4. It can use by giving input in two ways : <br>

```String``` and ```.txt``` files.

5. To use with string : <br>
## Encode the text<br>

```
python TextGuardian.py e key "Text" encrypted_text.txt
```
## Decode the text<br>

```
python TextGuardian.py d key encrypted_text.txt decrypted_text.txt
```
6. To use with .txt files : <br>
The original_text.txt is that file which contain original text whant to encode.<br>
## Encode the text<br>

```
python TextGuardian.py e key original_text.txt encrypted_text.txt
```
## Decode the text<br>

```
python TextGuardian.py d key encrypted_text.txt decrypted_text.txt
```

<h1>Key Features</h1>
<b>1. It can encode and decode text.</b><br>
<b>2. It can work with string and .txt files.</b><br>
<b>3. It lock/unlock the text with a password.<br>
