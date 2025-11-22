# %%
from PIL import Image  # (Python Imaging Library) Adds image processing capabilities.

import os  # Enables portable path handling across different operating systems and execution environments.

import time # Controls the timing (delay) between character output, essential for creating a rhythmic text effect.
import sys  # Provides direct control over standard output, allowing characters to be displayed immediately.

            # Together, 'time' and 'sys' emulate the character-by-character text display of early computer terminals,
            # where each character appeared sequentially due to hardware limitations and slower processing speeds.


class IconCongregator:
    def __init__(self):
        
        self.default_size = (256, 256) # Default size for icons

    def print_slow(self, text, delay=0.05, line_delay=0.5):
   
        for line in text.split('\n'):
            for char in line:
                sys.stdout.write(char)  # Print step by step
                sys.stdout.flush()  # Force immediate display
                time.sleep(delay)
            print()                 # New line after each line
            time.sleep(line_delay)  # Pause between lines

    def congregate_icon(self, input_path, output_path):
   
        try:
            imagen = Image.open(input_path)  # Open image
            imagen = imagen.resize(self.default_size, Image.LANCZOS)  # Resize image
            imagen.save(output_path, format='ICO')  # Save as .ICO
            print(f"\nYour icon has been congregated here: {os.path.abspath(output_path)}") 
            return True
        except Exception as e:
            print(f"\nError during congregation: {e}") 
            return False

    def get_file_name(self, prompt, default_extension=""):
     
    
        while True:
            name = input(prompt).strip()  # Get file name
                                          # if there is no extension, add the default extension (.png)
            if not os.path.splitext(name)[1] and default_extension:
                name += default_extension
            # If it's an output file (.ico) or the input file exists, return it
            if default_extension == ".ico" or os.path.exists(name):
                return name
            print(f"File '{name}' not found. Try again.")  # Error if not found.
            if name.lower() == 'exit':
                return None
        # aquí hay que mejorar la condición que permita la salida (si no pedirá un nombre hasta el infinito)

    def run(self):

        #Runs the main program:
        # displays ASCII art, prompts the user for files and performs the conversion.

       
        print("""
                                p r e s e n t s
                ░█▀█░█▄█░█▀█░▀█▀░█▀█░░░█░█░█▀█░█░█░█▀▀░░░█▀▀░█▀▀░▀█▀
                ░█░█░█░█░█░█░░█░░█▀█░░░█░█░█░█░█░█░▀▀█░░░█▀▀░▀▀█░░█░
                ░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░░▀░
        """)
        
        self.print_slow("""
                        .ICO EXTENSION IS OUR ONLY FAITH
        """, delay=0.04, line_delay=0.10)

        
        ascii_art = r"""
    .                     .                    .
  .                                 *                .      .         *
                         =        .            =                   
            .         <^\O|^                 ^|O/^>          *
     .         *      \/  |/                 \|  \|                .        .     *
                       /__|      .  '  .      |__\     *
            =           ll     .    |          ll           =                     
         <^\O|^     ¡__/||       '  |  '       ||\__¡     ^|O/^>      .         *  ·
         \/  |/   ¡_/_| ||  .  '  \ | / '  .   || |_\_¡   \|  \/
  .       /__|  ¡_||_||_||      -== + ==-      ||_||_||_¡  |__\    .       ·
         ..ll   //-|--|-||  '  .  / . \  .  '  ||-|--|-\\   ll..
        (____) /|  |  | ||       .  |  .       || |  |  |\ (____)              
         |  |¡//|  |  | ||    '     |     '    || |  |  |\\¡| -|          .  ·
         | -|¡  |  |  | ||       '  .  '       || |  |  | \¡|  |
         |  ||  |  |  | ||                     || |  |  |  || -|
    ¡_¡__|- ||  |  |  | ||   *      +          || |  |  |  ||  |__¡_¡
    ¡_|__|__||__|__|__|_||          A          ||_|__|__|__||__|__|_¡
    ·-|--|--||--|--|--|-||       _ /_\__  *    ||-|--|--|--||--|--|-·
      |  |  ||  |  |  | ||      /|-'O'-|\      || |  |  |  || -|  |
      |  |- ||  |  |  | ||     _||-----||_     || |  |  |  ||  |  |
      |  |  ||  |  |  | ||     /||=====||\     || |  |  |  ||- |  |
      |  | -||  |  |  | ||  __|I_I_[_]_I_I|__  || |  |  |  ||  |  |
     _|__|__||__|__|__|_||:::::::::::::::::::::||_|__|__|__||__|__|_
www  -|--|--||--|--|--|-||::::::::::::::::www::||-|--|--|--||--|--|-  www   wwwwwww
  ww =|==|==||==|==|==|=||::::::::::::www::::::||=|==|==|==||==|==|= wwwwwwwwwww  www
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww]
        """

        self.print_slow(ascii_art, delay=0.01, line_delay=0)

        self.print_slow(
            "                 W E L C O M E   T O   T H E   C O N V E R S I O N   P R O G R A M",
            delay=0.04, line_delay=0.10
        )

        self.print_slow("Please:\nGather in my destiny the wayward image you want to turn into an icon. Take all the time you need. Time is all we have.",
    delay=0.05, line_delay=0.10)

       
        while True:
            
            input_path = self.get_file_name(
                "\n> What is the name of the file you wish to join in our faith? (e.g., image.png): ",
                ".png"
            )
            
            if input_path is None:  # If user typed 'exit'
                break

            output_path = self.get_file_name(
                "\n> How shall we baptize your icon?")

           
            if self.congregate_icon(input_path, output_path):
                print("X")

            
            if input("Do you wish to join another icon? (Y/N): ").strip().lower() != 'y':
                print("Time is all we got. Use it wisely... or don't. It's not like we're counting.")
                break

# Entry point: runs only when the script is executed directly, not when imported as a module.
if __name__ == "__main__":
    congregator = IconCongregator()  
    congregator.run()  # Ejecuta el programa



