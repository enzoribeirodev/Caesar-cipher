# Caesar Cipher

A simple, efficient Python implementation of the Caesar Cipher!

## 📋 Features

- **Encode and Decode:** Easily switch between encryption and decryption modes.
- **Infinite Rotation:** Handles shift numbers larger than the alphabet size using modulo arithmetic.
- **Symbol Preservation:** Non-alphabetic characters (spaces, punctuation, numbers) remain unchanged.

## 🚀 Usage

### 1. Encoding
Set `encode=True` to shift the letters forward.

```python
from caesar import caesar_cipher

msg = "hello world"
encrypted = caesar_cipher(msg, turns=3, encode=True)
print(encrypted)
# Output: "khoor zruog"
```

### 2. Decoding
Set `encode=False` to shift the letters backward and reveal the original message.

```python
decrypted = caesar_cipher("khoor zruog", turns=3, encode=False)
print(decrypted)
# Output: "hello world"
```

## 🔧 Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `msg` | `str` | The text string you want to encrypt or decrypt. |
| `turns` | `int` | The number of positions to shift down the alphabet. |
| `encode` | `bool` | Set `True` to encrypt, `False` to decrypt. |

## 📚 What is the Caesar Cipher?

It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter a fixed number of positions down the alphabet. 

For example, with a left shift of 3:
- **D** becomes **A**
- **E** becomes **B**
- **F** becomes **C**

The method is named after **Julius Caesar**, who used it in his private correspondence to protect messages of military significance.
