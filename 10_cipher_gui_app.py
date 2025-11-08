# Cipher GUI App:
# This Python Tkinter-based application allows users to encrypt and decrypt text
# using Caesar and Playfair ciphers. It has input fields for the text and key,
# and buttons to perform encryption or decryption.

# Name : yosef 
import tkinter as tk 
from tkinter import messagebox

def caesar_encrypt(text,key) :
    import string

    az=string.ascii_lowercase
    AZ = string.ascii_uppercase

    cipher_text =''


    for letter in text :

        if letter in az :

            orgenil_letter = az.index(letter)
            location_letter =((orgenil_letter+key)%26)
            encrypted_letter = az[location_letter]
            cipher_text+=encrypted_letter

        elif letter in AZ :

            orgenil_letter = AZ.index(letter)
            location_letter =((orgenil_letter+key)%26)
            encrypted_letter = AZ[location_letter]
            cipher_text+=encrypted_letter

        else :
            cipher_text+= letter

    return cipher_text

def caesar_decrypt(text,key) :
    return caesar_encrypt(text=text,key=-key)# Cipher GUI App:
# This Python Tkinter-based application allows users to encrypt and decrypt text
# using Caesar and Playfair ciphers. It has input fields for the text and key,
# and buttons to perform encryption or decryption.

# Name : yosef 
import tkinter as tk 
from tkinter import messagebox

def caesar_encrypt(text,key) :
    import string

    az=string.ascii_lowercase
    AZ = string.ascii_uppercase

    cipher_text =''


    for letter in text :

        if letter in az :

            orgenil_letter = az.index(letter)
            location_letter =((orgenil_letter+key)%26)
            encrypted_letter = az[location_letter]
            cipher_text+=encrypted_letter

        elif letter in AZ :

            orgenil_letter = AZ.index(letter)
            location_letter =((orgenil_letter+key)%26)
            encrypted_letter = AZ[location_letter]
            cipher_text+=encrypted_letter

        else :
            cipher_text+= letter

    return cipher_text

def caesar_decrypt(text,key) :
    return caesar_encrypt(text=text,key=-key)


def generate_matrix (key) :
    key = key.replace('J','I').upper()
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix =''
    for char in key : 
        if char not in matrix and char in alphabet :
            matrix += char 
    
    for char in alphabet :
        if char not in matrix : 
            matrix +=  char 
    return matrix
    
def playfair_encrypt(text,key) : 
    matrix = generate_matrix(key) 
    result = ''
    text = text.upper().replace("J","I") 
    text_pairs = [text[i:i+2] for i in range(0,len(text),2)]
    if len(text_pairs[-1]) == 1 :
        text_pairs[-1] += 'X'
    for pair in text_pairs : 
        row1, col1 = divmod(matrix.index(pair[0]),5)
        row2, col2 = divmod(matrix.index(pair[1]),5) 
        if row1 == row2 : 
            result += matrix [row1 * 5 + (col1 + 1) % 5]
            result += matrix [row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2 :
            result += matrix[((row1 + 1 ) % 5 ) * 5 + col1]
            result += matrix[((row2 + 1 ) % 5 ) * 5 + col2]
        else : 
            result += matrix[row1 * 5 + col2]
            result += matrix[row2 * 5 + col1]
    return result


def playfair_decrypt (text,key) :
    matrix = generate_matrix(key) 
    result = ''
    text = text.upper()
    text_pairs = [text [i:i+2 ] for i in range (0,len(text),2)]
    for pair in text_pairs : 
        row1, col1 = divmod(matrix.index(pair[0]),5)
        row2, col2 = divmod(matrix.index(pair[1]),5) 
        if row1 == row2 : 
            result += matrix[row1 * 5 + (col1 - 1 ) % 5]
            result += matrix[row2 * 5 + (col2 - 2 ) % 5 ]
        elif col1 ==col2 : 
            result += matrix [((row1 - 1) % 5 ) * 5 + col1]
            result += matrix [((row2 - 1) % 5 ) * 5 +col2 ]
        else : 
            result += matrix [row1 * 5 + col2]
            result += matrix [row2 * 5 + col1]
    return result
    

def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()

    extended_key = (key * (len(text) // len(key) + 1))[:len(text)]

    ciphertext = []

    for p_char, k_char in zip(text, extended_key):
        if p_char.isalpha():
            encrypted_char = chr(((ord(p_char) - ord('A') + ord(k_char) - ord('A')) % 26) + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(p_char) 


    return ''.join(ciphertext)


#App;ication
class ChipherApp :
    def __init__(self,root):

        root.title('Cipher App')
        root.geometry('500x500')
        root.resizable(False,False)

        

        self.mode_labal = tk.Label(root,text='select Mode :')
        self.mode_labal.pack()

        self.mode = tk.StringVar(value="Caesar")
        self.caesar_radio = tk.Radiobutton(root,text="Caesar Cipher",variable=self.mode,value="Caesar")
        self.caesar_radio.pack()
        self.playfair_radio = tk.Radiobutton(root,text="Playfair Cipher",variable=self.mode,value="Playfair")
        self.playfair_radio.pack()

        self.key_label = tk.Label(root,text=' Enter Key :')
        self.key_label.pack()
        self.key_entry = tk.Entry(root)
        self.key_entry.pack()

        self.text_label = tk.Label(root,text='Enter Text :')
        self.text_label.pack()
        self.text_entry = tk.Entry(root)
        self.text_entry.pack()

        self.result_label = tk.Label(root,text="Result:")
        self.result_label.pack()
        self.result_text = tk.Text(root,height=5,width=40)
        self.result_text.pack()

        self.encrypt_btn = tk.Button(root,text='Encrypt',command=self.encrypt)
        self.encrypt_btn.pack()
        self.decrypt_btn = tk.Button(root,text='Decrypt',command=self.decrypt)
        self.decrypt_btn.pack()

      


    def encrypt(self):
        text = self.text_entry.get()
        key = self.key_entry.get()
        mode =self.mode.get()
        result = ""
        if mode =="Caesar" :
            try:
                key = int(key)
                result = caesar_encrypt(text,key)
            except ValueError :
                messagebox.showerror("Invalid Key","key must be an integer for Caesar Cipher.")
                return 
        elif mode =="Playfair" :
            result = playfair_encrypt(text,key)
        self.result_text.delete(1.0,tk.END)
        self.result_text.insert(tk.END,result)
                                
    def decrypt (self) :
        text =self.text_entry.get()
        key = self.key_entry.get()
        mode = self.mode.get()
        result=""
        if mode == "Caesar" :
            try :
                key =int(key)
                result = caesar_decrypt(text,key)
            except ValueError :
                messagebox.showerror("InvaliD Key","Key must be an integer for Caesar Cipher.")
                return
        elif mode =="Playfair" :
            result = playfair_decrypt(text,key)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)


if __name__=="__main__" :
    root= tk.Tk()
    app = ChipherApp(root)
    root.mainloop()



