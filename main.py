import cv2
import argparse


def to_ascii(image, chars):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (width, length))
    ascii_frame = ""

    for row in image:
        for pixel_value in row:
            index = int(pixel_value / 256 * len(chars))
            ascii_frame += chars[index]
        ascii_frame += "\n"

    return ascii_frame


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Super Duper Great Cool ASCII art maker!.")

    parser.add_argument("input_file", help="Path to the input file")

    parser.add_argument("-o", "--output_file", default="result.txt", help="Path to the output file")
    parser.add_argument("-w", "--width", type=int, default=300, help="Width of the ASCII art")
    parser.add_argument("-l", "--length", type=int, default=300, help="Height of the ASCII art")
    parser.add_argument("-c", "--chars", type=str, default="@#$%/&*()_+!", help="Characters to make the ASCII art")

    args = parser.parse_args()
    img_path = args.input_file
    img = cv2.imread(img_path)
    output_file = args.output_file
    width = args.width
    length = args.length
    chars = args.chars

    with open(output_file, 'w') as file:
        res = to_ascii(img, chars)
        file.write(res)
