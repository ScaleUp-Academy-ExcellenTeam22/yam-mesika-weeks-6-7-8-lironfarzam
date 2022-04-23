from PIL import Image


def get_an_encrypted_message_from_the_image(image_path: str) -> str:
    """
    function gets a path to file and returns the message encrypted within it by the position of black pixels.
    :param image_path:The path of the encryption image.
    :return:The encrypted message.
    """
    the_message = ''
    image = Image.open(image_path, 'r')
    pixels = image.load()
    width, height = image.size
    black_pixels = [row for col in range(width) for row in range(height) if pixels[col, row] == 1]
    return the_message.join(chr(pixel) for pixel in black_pixels)


if __name__ == '__main__':

    file_path = "code.png"
    print(get_an_encrypted_message_from_the_image(file_path))
