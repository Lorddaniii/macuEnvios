"""
Generador profesional de CSS para proyectos web
Autor: daniiibots
Fecha de generación automática: 
Lee variables y bloques desde JSON
"""

import datetime
import json

class CSSGenerator:
    def __init__(self, variables, blocks, minify=False):
        self.variables = variables
        self.blocks = blocks
        self.minify = minify
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generate_variables(self):
        css = ":root {\n"
        for k, v in self.variables.items():
            css += f"  --{k}: {v};\n"
        css += "}\n\n"
        return css

    def generate_blocks(self):
        css = ""
        for selector, rules in self.blocks.items():
            css += f"{selector} {{\n"
            for prop, val in rules.items():
                css += f"  {prop}: {val};\n"
            css += "}\n\n"
        return css

    def minify_css(self, css):
        # Simple minifier: remove newlines and extra spaces
        return ''.join(line.strip() for line in css.splitlines())

    def generate(self):
        header = f"/* CSS generado profesionalmente por Python - {self.timestamp} */\n"
        css_content = self.generate_variables() + self.generate_blocks()
        if self.minify:
            css_content = self.minify_css(css_content)
        return header + css_content

    def save(self, filename="css_profesional_generado.css"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.generate())
        print(f"¡CSS generado profesionalmente y guardado en {filename}!")

def cargar_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    # Carga variables y bloques desde archivos JSON
    variables = cargar_json("variables.json")
    blocks = cargar_json("bloques.json")
    # Cambia minify=True si quieres el CSS comprimido para producción
    generator = CSSGenerator(variables, blocks, minify=False)
    generator.save("css_profesional_generado.css")
