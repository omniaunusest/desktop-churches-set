from PIL import Image
import os
import time
import sys

def print_slow(text, delay=0.05, line_delay=0.5):
    for line in text.split('\n'):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # Salto de línea al final de cada línea
        time.sleep(line_delay)  # Pausa entre líneas



print("""   
                                p r e s e n t a
                ░█▀█░█▄█░█▀█░▀█▀░█▀█░░░█░█░█▀█░█░█░█▀▀░░░█▀▀░█▀▀░▀█▀
                ░█░█░█░█░█░█░░█░░█▀█░░░█░█░█░█░█░█░▀▀█░░░█▀▀░▀▀█░░█░
                ░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░░▀░""")
print_slow(""""""
    "\n                      AQUÍ SOLO CREEMOS EN LA EXTENSIÓN .ICO",
    delay=0.04, line_delay=0.10
)

ascii_art = r"""
    .                     .                    .
  .                                 *                .      .         *
                        =        .             =
            .         <^\O|^                 ^|O/^>          *
     .         *      \/  ||                 \|  \|                .        .     *
                       /__|      .  '  .      |__\     *
           =            ll    .     |     .    ll            =
        <^\O|^       i__\|       '  |  '       \|__i      ^|O/^>      .         *
        \/  |/    i__|| ||  .  '  \ |   '  .   |_I\__i    \|  \/
  .      /__|     |I_||_||      -== + ==-      ||_|\_I     |__|
         __ll   i|||--|-||  '  .   |.\   .  '  |-|--|\\i    ll__
        {    } |I| |  | ||       .  |  .       || |  | \I\ {    }
         |__|I|||  |  | ||    '     |     '    || |  |  |\\I|__|
         |  |I| |  |  | ||       '  .  '    *  || |  |  | \I|  |
        {_ __}  |  |  | ||                     || |  |  |  {____}
     _i__|= ||  |  |  | ||   *      +          || |  |  |  ||  |__i_
     _I__|  ||__|__|__|_||          A          ||_|__|__|__||- |__I_
     -|--|- ||--|--|--|-||       _ /_\__  *    ||-|--|--|--||= |--|-
      |  |  ||  |  |  | ||      /|-'O'-|\      || |  |  |  ||  |  |
      |  |= ||  |  |  | ||     _||-----||_     || |  |  |  ||= |  |
      |  |- ||  |  |  | ||     /||=====||\     || |  |  |  ||- |  |
      |  |- ||  |  |  | ||  __|I_I_[_]_I_I|__  || |  |  |  ||= |  |
     _|__|  ||__|__|__|_||:::::::::::::::::::::||_|__|__|__||  |__|_
www  -|--|= ||--|--|--|-||::::::::::::::::www::||-|--|--|--||- |--|-
  wwww|  |- ||  |  |  | ||::::::::::::www::::::|| |  |  |  ||= |  | wwwwwwwwwww  www
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
"""
print_slow(ascii_art, delay=0.9, line_delay=0)

print_slow(
    "\n    B I E N V E N I D A  A L  P R O G R A M A  D E  C O N V E R S I Ó N",
    delay=0.05, line_delay=0.10
)

print_slow(
    "\nPor favor:\nreune en mi destino la imagen descarriada que quieres convertir en un icono para Windows. Tómate el tiempo que quieras.",
    delay=0.05, line_delay=0.10
)

def conversor(start, output, size=(256, 256)):
    try:
        imagen = Image.open(start)
        imagen = imagen.resize(size, Image.LANCZOS)
        imagen.save(output, format='ICO')
        print(f"\n¡Has creado un nuevo icono! Lo encontrarás congregado en {os.path.abspath(output)}")
    except Exception as e:
        print(f"\nError: {e}")

entrada = input("\n> ¿Cómo se llama el archivo que quieres entregar? (ej: imagen.png): ")
salida = input("> ¿Cómo lo quieres bautizar? (ej: icono.ico): ")

conversor(entrada, salida)
