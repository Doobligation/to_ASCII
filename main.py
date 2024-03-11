import cv2
import argparse
from PIL import Image, ImageDraw, ImageFont


def parse_args():
    parser = argparse.ArgumentParser(description="Super Duper Great Cool ASCII art maker!.")
    parser.add_argument("input_file", help="Path to the input file")

    parser.add_argument("-o", "--output_file", default="result.txt", help="Path to the output file")
    parser.add_argument("-w", "--width", type=int, default=300, help="Width of the ASCII art")
    parser.add_argument("-l", "--length", type=int, default=300, help="Height of the ASCII art")
    parser.add_argument("-c", "--chars", type=str, default="@#$%/&*()_+!", help="Characters to make the ASCII art")
    parser.add_argument("-s", "--font_size", type=int, default=1, help="Size of the font")

    return parser.parse_args()


def main():
    args = parse_args()

    img_path = args.input_file
    file = cv2.imread(img_path)

    output_file = args.output_file
    width = args.width
    length = args.length
    chars = args.chars
    size = args.font_size

    to_ascii(file, output_file, chars, width, length,size)


def to_ascii(file, output, chars, width, length, size):
    file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
    file = cv2.resize(file, (width, length))
    ascii_frame = ""

    for row in file:
        for pixel_value in row:
            index = int(pixel_value / 256 * len(chars))
            ascii_frame += chars[index]
        ascii_frame += "\n"

    if str(output).split(".")[-1] == "jpg":
        return to_jpg(ascii_frame, output, width, length, size)
    elif str(output).split(".")[-1] == "txt":
        with open(output, 'w') as file:
            file.write(ascii_frame)


def to_jpg(txt, output, width, length, size):
    im = Image.new("1", (width, length), color="white")
    im.convert("L")

    draw = ImageDraw.Draw(im)

    x, y = 0, 0
    font_size = size
    font = ImageFont.truetype("arial.ttf", font_size)
    char_width = font_size
    char_height = font_size

    for char in txt:
        draw.text((x, y), char, fill='black', font=font)
        x += char_width
        if x + char_width > width + 1:
            x = 0
            y += char_height

    im.save(output)


if __name__ == "__main__":
    main()


