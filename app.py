from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

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

if __name__ == '__main__':
    app.debug = True
    app.run()    