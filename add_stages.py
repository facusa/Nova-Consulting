import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

stages = [
    ("1. Selección del Caso", "Presentación del equipo y de la PyME textil \"Full Basics\", identificando su modelo de negocio y sus problemas actuales de gestión manual."),
    ("2. Diagnóstico Organizacional", "Análisis de la cultura y madurez de la empresa, definiendo y priorizando los requerimientos clave mediante Historias de Usuario."),
    ("3. Análisis de la Arquitectura Empresarial Actual", "Mapeo de cómo funciona la empresa hoy en día, detallando bajo el marco TOGAF sus procesos, bases de datos, aplicaciones y tecnología base."),
    ("4. Innovación para la Transformación", "Propuesta de soluciones tecnológicas innovadoras y de bajo costo (IA, Trello, Google Docs) para resolver los problemas operativos sin reemplazar los sistemas actuales."),
    ("5. Arquitectura Empresarial Destino", "Diseño de cómo será la empresa en el futuro ideal, una vez que se implementen las nuevas automatizaciones e integraciones."),
    ("6. Matriz de Brechas y Escenarios", "Identificación de las piezas que faltan para llegar a esa arquitectura futura y elección de la mejor forma de implementarlo (en la nube y por etapas modulares)."),
    ("7. Revisión del alcance del Proyecto", "Definición estricta de los límites del trabajo de consultoría (qué se va a hacer y qué no), detallando el cronograma y los actores involucrados."),
    ("8. Análisis de Mercado (RFI)", "Búsqueda de plataformas reales en el mercado y preselección de los dos finalistas para el proyecto: Chatwoot y HubSpot Service Hub."),
    ("9. Creación de la Matriz RFP", "Creación de una planilla en Excel para puntuar de manera matemática y objetiva a los dos proveedores finalistas según criterios funcionales, técnicos y económicos."),
    ("10. Evaluación Económica", "Análisis financiero de los costos iniciales y a 3 años, cruzando la información con los puntajes para declarar a Chatwoot como ganador por ser más económico."),
    ("11. Conclusiones de la Selección", "Defensa final de la elección de Chatwoot frente al cliente, explicando cómo van a mitigar las brechas (puntos débiles) de la herramienta elegida.")
]

stages_html = """
                                <div class="stages-container" style="width: 100%; margin: 10px 0;">
                                    <div class="ma-badge" style="margin-bottom: 20px;">LAS ETAPAS DEL PROYECTO</div>
                                    <div class="stages-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">"""

for title, desc in stages:
    stages_html += f"""
                                        <div class="stage-card" style="padding: 20px; background: rgba(0,0,0,0.02); border-left: 3px solid var(--primary-color); border-radius: 0 8px 8px 0; transition: transform 0.3s ease;">
                                            <h4 style="font-size: 15px; margin-bottom: 8px; color: var(--text-main); font-weight: 700;">{title}</h4>
                                            <p style="font-size: 14px; color: var(--text-muted); margin: 0; line-height: 1.5;">{desc}</p>
                                        </div>"""

stages_html += """
                                    </div>
                                </div>
"""

# Replace the specific target
target = """                                    <p style="margin-top: 10px; color: var(--text-light);">Full
                                        Basics enfrentaba cuellos de botella en su cadena de valor, falta de visibilidad
                                        en el inventario y una gestión de clientes fragmentada.</p>
                                </div>"""

# Ensure it's replaced exactly by splitting and joining if whitespace varies
import textwrap

# We will just inject it before <div class="ma-right" style="width: 100%;">
new_content = re.sub(
    r'(<div class="ma-right" style="width: 100%;">)',
    lambda m: stages_html + "\n                                " + m.group(1),
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated stages successfully")
