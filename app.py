import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

def main():
    # Custom CSS
    st.markdown("""
    <style>
    .main {
        background-color:#460278;
        color: white; /* Cambiado a blanco */
    }
    .stApp {
        background-color: #140b80;
    }
    h1, h2, h3 {
        color: white !important; /* Asegurando que los encabezados sean blancos */
    }
    .stButton>button {
        color: #00264d;
        background-color: white;
        width: 100%;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    """
    # { ¡Bienvenido al Futuro! }
    """

    # Main content with image on the right
    col1, col2 = st.columns([2, 1])

    with col1:
        colored_header(label="NotebookLM en 90 Minutos", description="", color_name="violet-70")
        # st.markdown("<h2>NotebookLM en 90''</h2>", unsafe_allow_html=True)
        st.write("<span style='color: white;'>Imagina un asistente inteligente que te ayuda a sintetizar la información de múltiples fuentes y que genera de inmediato nuevas ideas y rutas de aprendizaje.</span>", unsafe_allow_html=True)
        st.markdown("<h3>¡Eso es <b>NotebookLM<b> de Google!</h3>", unsafe_allow_html=True)
        
        

    with col2:
        st.image("image.webp", use_column_width=False, width=300)  # Asegúrate de que la imagen esté en el directorio correcto

    st.markdown("""
    <div class='card' style='color: white; background-color: #6569db;'>
    <h3>Clase de 90 Minutos, Sin Costo</h3>
    <p>Te invitamos a una charla gratuita de 90 minutos en donde conocerás cómo esta herramienta de Google, impulsada por inteligencia artificial (Gemini 1.5) puede transformar la forma en la que organizas y aprovechas la información.</p>
    <p>Dirigido a TODOS los interesados en la tecnología, productividad y creatividad.</p>
    </div>
    """, unsafe_allow_html=True)

    # Date and time
    colored_header(label="{ Fecha y Hora }", description="", color_name="violet-70")
    st.write("<span style='color: white;'>La clase se impartirá por **:orange[Meet de Google]** de las **:orange[19:00 a las 20:30]** horas del **:orange[martes 29 de Octubre]** de 2024.</span>", unsafe_allow_html=True)

    # Registration instructions
    colored_header(label="{ Instrucciones Para Inscribirse a la Clase Gratuita }", description="", color_name="violet-70")
    st.write("<span style='color: white;'>Para tomar la clase manda un correo electrónico a randradedev@gmail.com con los siguientes datos:</span>", unsafe_allow_html=True)
    st.write("<span style='color: white;'>1. Nombre completo,</span>", unsafe_allow_html=True)
    st.write("<span style='color: white;'>2. Correo electrónico,</span>", unsafe_allow_html=True)
    st.write("<span style='color: white;'>3. Máximo nivel de estudios,</span>", unsafe_allow_html=True)
    st.write("<span style='color: white;'>4. Experiencia con la Inteligencia Artificial Generativa.</span>", unsafe_allow_html=True)
    st.write("<span style='color: white;'>En pocas horas te enviarán la invitación y el vínculo para unirte al evento el 29 de octubre de 2024.</span>", unsafe_allow_html=True)
 
    

    # What you'll learn
    st.markdown("<h2 style='text-align: center; color: white;'>¿Qué Aprenderás?</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='card' style='height: 250px; color: white;'>
        <h3>Fundamentos de AI y GenAI</h3>
        <p>Revisaremos los conceptos de Inteligencia Artificial e Inteligencia Artificial Generativa.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card' style='height: 250px; color: white;'>
        <h3>Aplicaciones Prácticas</h3>
        <p>Conocerás Casos de Uso de <b>NotebookLM</b> de Google en escenarios educativos y productivos.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='card' style='height: 250px; color: white;'>
        <h3>Ética en la AI</h3>
        <p>Platicaremos sobre las consideraciones éticas y el uso responsable de la GenAI.</p>
        </div>
        """, unsafe_allow_html=True)

    # Class agenda
    st.markdown("""
    <div class='card' style='height: 330px; background-color:#6569db; color: white;'>
    <h3>Agenda de la Clase</h3>
    <p>• Inteligencia Artificial e Inteligencia Artificial Generativa</p>
    <p>• ¿Qué es <b>NotebookLM de Google</b>?</p>
    <p>• Casos de Uso Generales</p>
    <p>• Demostración para un Caso de Marketing</p>
    <p>• Limitaciones y Consideraciones Éticas</p>
    <p>• Conclusiones</p>
    </div>
    """, unsafe_allow_html=True)


    # Community section

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h2 style='text-align: center; color: white;'>Únete a Nuestra Comunidad</h2>", unsafe_allow_html=True)
        st.write("<span style='color: white;'>Conecta con otros estudiantes y expertos de la industria en nuestra vibrante comunidad GenAI.</span>", unsafe_allow_html=True)
    with col2:
        st.image("mundo_genai.webp", width=300)

    st.markdown("""
        <div style='text-align: center;'>
        <p>
                    
        <span style='color: #c0e6ed;'>*Plática impartida por Roberto Andrade F.*</span>
        <p style='color: #c0e6ed;'>Profesor de la UNAM, Analista de Datos y DBA.</p>
        <p style='color: #c0e6ed;'>randradedev@gmail.com</p>
        </div>
    """, unsafe_allow_html=True)
if __name__ == "__main__":
    main()
