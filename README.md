# Image to ASCII

This is a Python script that converts an image to ASCII art. The script uses the Python Imaging Library (PIL) to open an image file, convert it to grayscale, and then map the pixel intensities to ASCII characters. The ASCII art is saved to a text file.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies by running the following command: `pip install Pillow`
4. Run the script using Python, for example: `python image_to_ascii.py`
5. The script will open a file dialog to allow you to select an image file. Once an image file is selected, the script will convert it to ASCII art and save the output to a text file named "output_text.txt" in the same directory as the script.
6. You can adjust the ASCII characters used for drawing by modifying the `ascii_chars` list in the script to your preference.
7. Enjoy the generated ASCII art!

## GUI

The script also includes a graphical user interface (GUI) using Tkinter. The GUI allows you to open a custom image file using a file dialog and save the ASCII art to a text file with ease.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
