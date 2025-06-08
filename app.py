from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Esto permite que tu JS hable con este servidor

# Esta es la función donde pondrás tu lógica de Python
def update_villager_positions(villagers):
    for v in villagers:
        v['x'] += v['vx']
        v['y'] += v['vy']

        # Lógica de rebote simple (puedes hacerla más compleja)
        if v['x'] <= 0 or v['x'] >= 800 - 16: # 800 es el ancho del canvas
            v['vx'] *= -1
        if v['y'] <= 50 or v['y'] >= 600 - 100: # 600 es la altura del canvas
            v['vy'] *= -1
    return villagers

# Esta es la "puerta de entrada" a nuestra cocina
@app.route('/update_movement', methods=['POST'])
def update_movement():
    # 1. Recibe los datos del juego (los aldeanos) desde JavaScript
    data = request.json
    villagers = data.get('villagers', [])

    # 2. Usa tu lógica de Python para actualizar las posiciones
    updated_villagers = update_villager_positions(villagers)

    # 3. Devuelve los datos actualizados a JavaScript
    return jsonify({'villagers': updated_villagers})

if __name__ == '__main__':
    app.run(debug=True, port=5000)