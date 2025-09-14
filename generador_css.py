# Generador profesional de CSS usando Python

variables = {
    "color-principal": "#6c47ff",
    "color-secundario": "#ffb84d",
    "color-blanco": "#fff",
    "color-oscuro": "#232339",
    "color-shadow": "#6c47ff33",
    "border-radius": "16px",
    "shadow": "0 6px 24px #6c47ff33"
}

bloques = {
    "body": {
        "font-family": "'Roboto', Arial, sans-serif",
        "background": "linear-gradient(120deg, #f9f9fc 0%, #f0eeff 100%)",
        "color": variables["color-oscuro"],
        "margin": "0",
        "min-height": "100vh"
    },
    "header": {
        "background": f"linear-gradient(90deg, {variables['color-principal']} 70%, {variables['color-secundario']} 100%)",
        "color": variables["color-blanco"],
        "box-shadow": variables["shadow"]
    }
    # Puedes agregar más bloques aquí...
}

def generar_variables_css(vars_dict):
    salida = ":root {\n"
    for k, v in vars_dict.items():
        salida += f"  --{k}: {v};\n"
    salida += "}\n\n"
    return salida

def generar_reglas_css(bloques_dict):
    salida = ""
    for selector, reglas in bloques_dict.items():
        salida += f"{selector} {{\n"
        for propiedad, valor in reglas.items():
            salida += f"  {propiedad}: {valor};\n"
        salida += "}\n\n"
    return salida

css = generar_variables_css(variables) + generar_reglas_css(bloques)
with open("css_profesional_generado.css", "w") as f:
    f.write(css)

print("¡CSS generado profesionalmente con Python!")
