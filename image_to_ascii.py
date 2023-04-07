from PIL import Image
from tkinter import Tk, filedialog

def open_file_dialog():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    root.destroy()
    return file_path

def draw_image_to_text(image_path, text_file):
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    width, height = image.size
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']  # ASCII characters for drawing
    text = ''

    for y in range(0, height, 10):  # Step by 10 pixels vertically
        for x in range(0, width, 5):  # Step by 5 pixels horizontally
            pixel = image.getpixel((x, y))
            ascii_index = int(pixel / 25)  # Map pixel intensity to ASCII character
            text += ascii_chars[ascii_index]  # Append ASCII character to text

        text += '\n'  # Add line break at the end of each row

    with open(text_file, 'w') as f:
        f.write(text)

def main():
    # Open file dialog to get image file path
    image_path = open_file_dialog()

    if image_path:
        output_file = 'output_text.txt'  # Output text file name
        draw_image_to_text(image_path, output_file)
        print(f'Success! ASCII art has been generated and saved to {output_file}.')
    else:
        print('No image file selected. Exiting...')

if __name__ == '__main__':
    main()
