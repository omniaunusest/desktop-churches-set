# %%
from PIL import Image
import numpy as np
import os
import sys
import time 


def print_slow(text, delay=0.05, line_delay=0.5):
   
    for line in text.split('\n'):
        for c in line:
            sys.stdout.write(c)  # Print step by step
            sys.stdout.flush()  # Force immediate display
            time.sleep(delay)
        print()                 # New line after each line
        time.sleep(line_delay)  # Pause between lines


def distorted_wave(img, amplitude, wavelength):

# Apply a sine wave distortion to the input image.

    img = Image.open(img)
    img_array = np.array(img)
    height, width, channels = img_array.shape

    # Create coordinate grids
    x = np.tile(np.arange(width), (height, 1))
    y = np.tile(np.arange(height).reshape(-1, 1), (1, width))

    # Apply distortion
    y_distorted = y + amplitude * np.sin(2 * np.pi * x / wavelength)

    # Build the new image
    new_image = np.zeros_like(img_array)

    for h in range(height):


        for w in range(width):
            y_pos = int(y_distorted[h, w]) % height
            new_image[h, w] = img_array[y_pos, w]

        return Image.fromarray(new_image)

def get_file_name(prompt, default_extension = ""):
     
    while True:

        name = input(prompt).strip()  # Get file name
                                          # if there is no extension, add the default extension (.png)

        if name.lower() == 'exit':
                return None
            # aquí hay que mejorar la condición que permita la salida, por ejemplo que no la haga accidental

        if not os.path.splitext(name)[1] and default_extension: 
            name += default_extension
            # If it's an output file (.ico) or the input file exists, return it

        if default_extension not in ('.png', '.jpg', '.jpeg') and name not in os.path.exists(name):
            print(f"File '{name}' not found. Try again or write 'exit' to leave.")
            continue
    return name

def get_int_input(prompt, default=None):
# Prompt the user for an INT input, with optional default.
    while True:
        try:
            value = input(prompt).strip()
            if not value and default is not None:
                return default
            return int(value)
        except ValueError:
                print("Please, write a valid answer for the gospel.")


def run(): # aquí falta mucho ASCII y mucha chicha 
    print("=== Church of the New Wave: Distortion's gospel ===")
    
    while True:
        image_name = get_file_name("\n> Write the name of the image you are offering to the Wave: ", '.png')

        if image_name is None:
            break

        amplitude = get_int_input("\n> Summon your wave intensity (write a number): ", 10)
        wavelength = get_int_input("\n> Summon your wave frequency (write another number): ", 20)

        output_path = get_file_name("\n> How shall we baptize your distortion?", '.png')

        if output_path is None:
            break

        try:
            wave_img = distorted_wave(image_name, amplitude, wavelength)
            wave_img.save(output_path)
            print(f"\nAn image has been saved! You can join the distortion here: '{output_path}'")

        except Exception as e:
            print(f"\n Error: {e}. The gospel has failed.")
            continue

        onemoretime = input("\nDo you wish to join another image? (Y/N): ").strip().lower()  
        if onemoretime == 'n':
            print_slow(
                    "\nThe Church of the New Wave is always open.\n\n" \
                    "" \
                    "Thanks for coming!",
                    delay=0.05,
                    line_delay=0.8)
            break


run()
# hay que pensar si aquí procede meter a bailar una API


