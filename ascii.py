from PIL import Image


def ascii(filename) :
    #gets the data of the image
    img = Image.open(filename)
    #ratio to resize image
    img = img.resize((int(img.width / 2), int(img.height / 5)))
    width, height = img.size

    #ascii setup
    ascii_chars = "@#%$?|!*+=~-:,.` "
    ascii_art = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            brightness = sum(pixel) / 3 / 255
            
            # Determine ASCII character based on brightness
            ascii_index = min(int(round(brightness * (len(ascii_chars) - 1))), len(ascii_chars) - 1)
            ascii_char = ascii_chars[ascii_index]
            
            ascii_art += ascii_char
        ascii_art += "\n"

    #PRINTS TO CONSOLE
    #print(ascii_art)
        
    #PRINTS TO TXT
    with open("output.txt", "w") as f:
        f.write(ascii_art)

def main():
    # Get the filename from the user
    filename = input("Enter the filename of the image: ")
    
    # Call the ascii function to convert the image to ASCII art
    ascii(filename)

if __name__ == "__main__":
    # If this script is run directly, call the main function
    main()
