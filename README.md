# ENCRYPTOR
#### Video Demo:  https://youtu.be/oLn3HzOKcZ4
#### Description:
This web application allows encrypting and decrypting user entries based on a key(an integer).

##Distibution code

It's a **Flask** web app so I have an ***app.py*** file and a templates folder that have two html files: **index.htlm** and **decrypt.html**

###app.py
First I import the library:
```
from flask import Flask, render_template, request, jsonify
```
**I didn't use jsonify (lack of knowledge)**
After importing, I have to dynamically open each html files and wrote each page's functionality

###for index.html (/)

This code checks the request method first:
if it's 'POST':
>check the key enter by the user
>we will check each character of the input submitted by the user
>if the character is alphabetic we will add k to is ASCII number
>we will do all this carefully so it will always return a letter and respect the capitalization
if it's 'GET':
>return index.html

```
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":

        text = request.form.get("plaintext")
        key = request.form.get("key")
        k = int(key)
        encrypted = ""
        for i in range(len(text)):
            val = text[i]
            dup = k
            if val.isalpha():
                if ord(val)>=65 and ord(val)<=90:
                    if ord(val) + k > 90:
                        k -= (90- ord(val))
                        k = k % 26
                        encrypted += chr(64 + k)
                    else:
                        encrypted += chr(ord(val) + k)
                elif ord(val)>=97  and ord(val)<=122:
                    if ord(val) + k > 122:
                        k -= (122- ord(val))
                        k = k % 26
                        encrypted += chr(96 + k)
                    else:
                        encrypted += chr(ord(val) + k)
            else:
                encrypted += val
            k = dup

        return render_template('index.html', encrypted=encrypted)

    else:
        return render_template('index.html')
```


###for decrypt.html (/decrypt)

This code checks the request method first:
if it's 'POST'
>check the key enter by the user
>we will check each character of the input submitted by the user
>if the character is alphabetic we will remove k to is ASCII number
>we will do all this carefully so it will always return a letter and respect the capitalization
if it's 'GET':
>return decrypt.html

```
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():

    if request.method == "POST":

        text = request.form.get("plaintext_e")
        key = request.form.get("key")
        k = int(key)

        decrypted = ""
        for i in range(len(text)):
            val = text[i]
            dup = k
            if text[i].isalpha():
                if ord(val)>=65 and ord(val)<=90:
                    if ord(val) - k < 65:
                        k = (65- (ord(val) - k))
                        # k = k % 26
                        decrypted += chr(91 - k)
                    else:
                        decrypted += chr(ord(val) - k)
                elif ord(val)>=97  and ord(val)<=122:
                    if ord(val) - k < 97:
                        k = (97 - (ord(val) - k))
                        # k = k % 26
                        decrypted += chr(123 - k)
                    else:
                        decrypted += chr(ord(val) - k)
            else:
                decrypted += text[i]
            k = dup

        return render_template('decrypt.html', decrypted=decrypted)

    else:
        return render_template('decrypt.html')
```

At the and we will return the main
