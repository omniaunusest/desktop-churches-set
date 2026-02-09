# %%
from PIL import Image  # (Python Imaging Library) Adds image processing capabilities.

import os  # Enables portable path handling across different operating systems and execution environments.

import time # Controls the timing (delay) between character output, essential for creating a rhythmic text effect.
import sys  # Provides direct control over standard output, allowing characters to be displayed immediately.

            # Together, 'time' and 'sys' emulate the character-by-character text display of early computer terminals,
            # where each character appeared sequentially due to hardware limitations and slower processing speeds.


class IconCongregator:
    def __init__(self):
        
        self.default_size = (256, 256) # Important: Default size for icons

    def print_slow(self, text, delay=0.05, line_delay=0.5):
   
        for line in text.split('\n'):
            for c in line:
                sys.stdout.write(c)  # Print step by step
                sys.stdout.flush()  # Force immediate display
                time.sleep(delay)
            print()                 # New line after each line
            time.sleep(line_delay)  # Pause between lines

    def congregate_icon(self, input_path, output_path):
   
        try:
            with Image.open(input_path) as imagen:
                imagen = imagen.resize(self.default_size, Image.LANCZOS)  # Resize image
                imagen.save(output_path, format = 'ICO')  # Save as .ICO

                print(f"\nYour icon has been congregated here: {os.path.abspath(output_path)}") 
                return True
            
        except Exception as e:
            print(f"\nError during congregation: {e}") 
            return False
        

    def get_file_name(self, prompt, default_extension = ""):
     
        while True:

            name = input(prompt).strip()  # Get file name
                                          # if there is no extension, add the default extension (.png)
            if not os.path.splitext(name)[1] and default_extension: #splitext enables to handle extension itself as a separate item
                name += default_extension
            # If it's an output file (.ico) or the input file exists, return it

            if name.lower() == 'exit':
                return None
            # aquí hay que mejorar la condición que permita la salida

            if default_extension in ('.png', '.jpg', '.jpeg') and not os.path.exists(name):
                print(f"File '{name}' not found. Try again.")
                continue
            return name
        
    #Runs the main program:
    def run(self):
    

       
        print("""
                                p r e s e n t s
                ░█▀█░█▄█░█▀█░▀█▀░█▀█░░░█░█░█▀█░█░█░█▀▀░░░█▀▀░█▀▀░▀█▀
                ░█░█░█░█░█░█░░█░░█▀█░░░█░█░█░█░█░█░▀▀█░░░█▀▀░▀▀█░░█░
                ░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░░▀░
        """)
        
        self.print_slow("""
                         .ICO EXTENSION IS OUR ONLY FAITH
        """, delay=0.01, line_delay=0.05)

        
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
   wwwww =|==|==||==|==|==|=||::::::::::::www::::::||=|==|==|==||==|==|= wwwwwwwwwww  www
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
        """
# ASCI ART is a modified version based of an original from Joan G. Stark: The Pearly Gates.

        self.print_slow(ascii_art, delay=0.01, line_delay=0)

        self.print_slow(
            "               W E L C O M E   T O   T H E   C O N V E R S I O N   P R O G R A M",
            delay=0.05, line_delay=0.10
        )

        self.print_slow("Please:\nGather in my destiny (folder) the wayward file you want to turn into an icon.\n\nTake all the time you need.\n\nTime is all we have.",
    delay=0.05, line_delay=0.8)

       
        while True:
            
            input_path = self.get_file_name(
                "\n> What is the name of the file you wish to join our faith? (e.g., image.png): ",
                '.png')
            if input_path is None:  # If user typed 'exit'
                break

            output_path = self.get_file_name(
                "\n> How shall we baptize your icon?", '.ico')
            if output_path is None:
                break
           
            if self.congregate_icon(input_path, output_path):
                print("Conversion successful!")

            onemoretime = input("> Do you wish to join another icon? (Y/N): ").strip().lower()  
            if onemoretime == 'n':
                self.print_slow("\nTime is all we have.\n\nUse it wisely... or don't.\n\nIt's not like we're counting.", delay=0.05, line_delay=0.8)
                break
                                                                            # ¿añadir internamente un contador de conversiones a pesar de lo emitido en el mensaje?

# Entry point
if __name__ == "__main__":
    congregator = IconCongregator()  
    congregator.run()  # Ejecuta el programa



