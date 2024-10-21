ImageCryptoSteganography

A Python-based image steganography tool for hiding and retrieving secret messages within images.

Table of Contents

1. #overview
2. #installation
3. #usage
4. #features
5. #contributing
6. #license

Overview

ImageCryptoSteganography is a command-line tool that utilizes the Least Significant Bit (LSB) substitution method to embed and extract hidden messages within images.

Installation


bash
git clone (link unavailable)
cd ImageCryptoSteganography
pip install -r requirements.txt


Usage

Hide Message


bash
python (link unavailable) -i input_image.jpg -m "Secret Message" -o output_image.jpg


Retrieve Message


bash
python (link unavailable) -i output_image.jpg


Features

- Hide and retrieve text messages within images
- Supports JPEG, PNG, and BMP formats
- Utilizes LSB substitution method for steganography
- Command-line interface

Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit changes with descriptive messages.
4. Push changes to your fork.
5. Open a pull request.

License

LICENSE

Analysis Findings:

1. Code organization: Well-structured, with separate files for hiding and retrieving messages.
2. Programming languages: Python 3.x.
3. Dependencies: Pillow library.
4. Build and deployment: Not applicable.
5. Testing: Basic testing would be beneficial.
6. Licensing: MIT License.
