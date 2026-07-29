import os
import sys
import time
from pathlib import Path
from PIL import Image
import numpy as np
import streamlit as st

# Configuración inicial de Streamlit
st.set_page_config(
    page_title="The Great Censor",
    page_icon="🖼️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

class ImageCensor:
    def __init__(self):
        self.default_size = None

    def censor_object(self, input_path, color=(0, 0, 0), factor_pixelado=8, umbral=240):
        try:
            input_path = Path(input_path)
            output_dir = Path("output")
            output_dir.mkdir(exist_ok=True)
            output_path = output_dir / f"{input_path.stem}_censored.png"

            with Image.open(input_path) as imagen:
                imagen = imagen.convert("RGB")
                img_array = np.array(imagen)
                img_gray = np.mean(img_array, axis=2).astype(np.uint8)
                mascara_fondo = img_gray > umbral
                mascara_objeto = ~mascara_fondo
                altura, ancho, _ = img_array.shape

                for i in range(0, altura, factor_pixelado):
                    for j in range(0, ancho, factor_pixelado):
                        mascara_bloque = mascara_objeto[i:i + factor_pixelado, j:j + factor_pixelado]
                        if np.any(mascara_bloque):
                            img_array[i:i + factor_pixelado, j:j + factor_pixelado] = color

                imagen_censurada = Image.fromarray(img_array)
                imagen_censurada.save(output_path)
                return True, output_path

        except Exception as e:
            return False, str(e)

    def run(self):
        # CSS personalizado para el diseño
        st.markdown("""
        <style>
            * {
                font-family: 'Courier New', Courier, monospace !important;
            }
            html, body, [class*="css"] {
                background-color: #121212 !important;
                color: #e0e0e0 !important;
            }
            .stApp {
                background-color: #121212 !important;
                color: #e0e0e0 !important;
            }
            /* Estilo para la cabecera ASCII Art */
            .header-ascii {
                font-family: 'Courier New', Courier, monospace !important;
                white-space: pre;
                color: #aaaaaa !important;
                text-align: center !important;
                font-size: 12px !important;
                line-height: 1 !important;
                letter-spacing: 1px !important;
                margin: 30px 0 5px 0 !important;
            }
            /* Estilo para el ASCII Art grande */
            .big-ascii-art {
                font-family: 'Courier New', Courier, monospace !important;
                white-space: pre;
                color: #888888 !important;
                text-align: center !important;
                font-size: 12px !important;
                line-height: 1.5 !important;
                letter-spacing: 0.5px !important;
                margin: 6px 0 !important;
            }
            /* Estilo para los botones y widgets */
            .stButton>button {
                background-color: #83A13F !important;
                color: #aaaaaa !important;
                border: 1px solid #555555 !important;
                border-radius: 1px !important;
                padding: 8px 20px !important;
                font-family: 'Courier New', Courier, monospace !important;
            }
            .stFileUploader>div>div>div>div {
                background-color: #83A13F !important;
                border: 1px solid #555555 !important;
                border-radius: 1px !important;
                color: #aaaaaa !important;
            }
            .stSelectbox>div>div>select {
                background-color: #83A13F !important;
                color: #aaaaaa !important;
                border: 1px solid #555555 !important;
                border-radius: 2px !important;
            }
            .stMarkdown {
                text-align: center !important;
                margin: 0 auto !important;
            }
            /* Estilo para el texto general */
            p {
                font-size: 16px !important;
                line-height: 1.6 !important;
                color: #83A13F !important;
            }
        </style>
        """, unsafe_allow_html=True)

        # Cabecera con tu ASCII Art
        st.markdown("""
        <div class="header-ascii">
            ░█▀█░█▄█░█▀█░▀█▀░█▀█░░░█░█░█▀█░█░█░█▀▀░░░█▀▀░█▀▀░▀█▀
            ░█░█░█░█░█░█░░█░░█▀█░░░█░█░█░█░█░█░▀▀█░░░█▀▀░▀▀█░░█░
            ░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░░▀░
                                                 p r e s e n t s
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<h4 style='text-align: center; color: #aaaaaa;'>NEED INSTANT CENSORSHIP?\n\nWe have an Instant Church for you!</h4>", unsafe_allow_html=True)
        st.markdown("---")

        # ASCII Art grande
        st.markdown("""
        <div class="big-ascii-art">
                .                  .             * ·                  *
        ·           .                                               .        ·
    .                      .                    .
  .              ##                   * .     .         *            ##         .
                #####             =                                 #####      
         .    ############################################################
            ################################################################
            ###################################################$############
            ################################################################
            ################################################################
             ==============================================================
            ################################################################
            ###########################         ############################
            #########################             ##########################
            ###   ##################               ###################   ###
            ##     ################                 #################     ##
             #     ================                 =================     #
            ##     ################                 #################     ##
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<p>Please:<br>Present into The Great Censor the image you want to put under a veil.<br><br>Take all the time you need. Time is all we have.</p>", unsafe_allow_html=True)
        st.markdown("---")

        # Subir archivo
        uploaded_file = st.file_uploader(
            label="Type the name of your image:",
            type=["jpg", "jpeg", "png"],
            key="file_uploader",
            label_visibility="collapsed"
        )

        if uploaded_file is not None:
            temp_path = f"temp_{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            colors = {
                "1 - Azul palo de helado": (49, 25, 205),
                "2 - Strawberry": (225, 16, 72),
                "3 - Lemon": (203, 203, 15),
                "4 - Lime": (158, 184, 44),
                "5 - Orange": (181, 101, 43),
                "6 - Empty bag": (20, 19, 30),
            }

            chosen_color_name = st.selectbox(
                label="Choose a color for your Summer of Censorship era:",
                options=list(colors.keys()),
                key="color_select",
                label_visibility="collapsed"
            )
            chosen_color = colors[chosen_color_name]

            if st.button("Apply Censorship", key="apply_button"):
                success, result = self.censor_object(temp_path, color=chosen_color)
                if success:
                    st.success("You've been granted Instant Censorship! Congratulations!")
                    st.image(Image.open(result), caption="Censored Image", use_column_width=True)
                    with open(result, "rb") as f:
                        st.download_button(
                            label="Download Censored Image",
                            data=f,
                            file_name=os.path.basename(result),
                            mime="image/png",
                            key="download_button"
                        )
                else:
                    st.error(f"Your censorship has been a fraud! Please, check yourself... {result}")

            os.remove(temp_path)

if __name__ == "__main__":
    censor = ImageCensor()
    censor.run()