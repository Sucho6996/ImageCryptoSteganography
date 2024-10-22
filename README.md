# 🖼️🔐 ImageCryptoSteganography

A Python-based image steganography tool for *hiding* and *retrieving* secret messages within images using the *Least Significant Bit (LSB)* substitution method.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=flat&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-8.0+-yellow.svg?style=flat&logo=python&logoColor=white)

---

## 📜 *Table of Contents*
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Contributing](#contributing)
6. [License](#license)

---

## 📝 *Overview*

*ImageCryptoSteganography* is a command-line tool that allows users to embed secret messages into images and retrieve them later. It uses the *Least Significant Bit (LSB)* substitution method for *steganography*, making it a simple and effective solution for concealing information within image files.

---

## ⚙️ *Installation*

1. *Clone the repository*:
   bash
   git clone https://github.com/Sucho6996/ImageCryptoSteganography.git
   cd ImageCryptoSteganography
   

2. *Install the required dependencies*:
   bash
   pip install -r requirements.txt
   

---

## 🚀 *Usage*

### 🖼️ *Hide a Message*
bash
python hide.py -i input_image.png -m "Secret Message" -o output_image.png

- -i: The input image file (PNG).
- -m: The secret message to hide.
- -o: The output image file where the message is hidden.

### 🔍 *Retrieve a Message*
bash
python retrieve.py -i output_image.jpg

- -i: The image file containing the hidden message.

---

## 🌟 *Features*
- 🔑 *Hide and retrieve* text messages within images.
- 🖼️ Supports *PNG* formats.
- 🛠️ Utilizes the *Least Significant Bit (LSB)* substitution method for steganography.
- 💻 Simple *command-line interface* for ease of use.

---

## 🤝 *Contributing*

Contributions are welcome! Here's how you can contribute:
1. *Fork the repository* 🍴
2. *Create a feature branch* 🚀
   bash
   git checkout -b feature-branch
   
3. *Commit your changes* 💾
   bash
   git commit -m "Add new feature"
   
4. *Push to your branch* 📤
   bash
   git push origin feature-branch
   
5. *Open a pull request* 📬

---

## 📜 *License*

This project is licensed under the *MIT License*. For more information, refer to the LICENSE file.
