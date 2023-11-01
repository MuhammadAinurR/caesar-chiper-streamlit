import streamlit as st
import string

char_num_map = {j: i for i, j in enumerate(string.ascii_lowercase + " ")}
num_char_map = {i: j for i, j in enumerate(string.ascii_lowercase + " ")}


def encrypt(text, key):
    encrypted = ""
    text = text.lower()
    for letter in text:
        letter_key = char_num_map[letter]
        rotation = (letter_key + key) % vocab_size
        encrypted += num_char_map[rotation]
    return encrypted


def decrypt(text, key):
    decrypted = ""
    text = text.lower()
    for letter in text:
        letter_key = char_num_map[letter]
        rotation = (letter_key - key) % vocab_size
        decrypted += num_char_map[rotation]
    return decrypted


vocab_size = len(string.ascii_lowercase + " ")


st.title("Caesar Cipher")

key = st.slider("Key", 0, 25, 3)
message = st.text_input("Message to encrypt/decrypt")

if st.button("Encrypt"):
    encrypted_message = encrypt(message, key)
    st.success("Encrypted message: {}".format(encrypted_message))

if st.button("Decrypt"):
    decrypted_message = decrypt(message, key)
    st.success("Decrypted message: {}".format(decrypted_message))
