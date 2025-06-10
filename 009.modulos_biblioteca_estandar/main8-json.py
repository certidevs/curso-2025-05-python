import json

json_string = '''{"widget": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": { 
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}}    '''


# 1. JSON a diccionario (deserialización)
json_dictionary = json.loads(json_string)
print(json_dictionary["widget"]["debug"])
print(json_dictionary["widget"]["window"]["title"])
print(json_dictionary["widget"]["text"]["data"])

# 2. Diccionario a JSON (serialización)
result_json_string = json.dumps(json_dictionary)
print(result_json_string)
print(len(result_json_string))

# En frameworks como FastAPI
# Se suele usar librerías como Pydantic que permite serializar y deserializar a JSON automáticamente
# el framework convierte de objeto python a json y de json a objeto python