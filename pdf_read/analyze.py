from flask import Flask, jsonify
from Marcher import Marcher

marcher_list= []

with open("text_output.txt") as f:
    raw = f.read()

sheets = raw.split("Printed:")[:-1]

for sheet in sheets:
    marcher_list.append(Marcher(sheet))

print(marcher_list[0].name)
print(marcher_list[0].counts)
print(marcher_list[0].x)
print(marcher_list[0].y)

marcherAPI = Flask(__name__)

@marcherAPI.route('/api/retrieveMarcher/<int:marcherNumber>', methods=['GET'])
def retrieveMarcher(marcherNumber):
    return jsonify({
        'name': marcher_list[marcherNumber].name,
        'counts': marcher_list[marcherNumber].counts,
        'x': marcher_list[marcherNumber].x,
        'y': marcher_list[marcherNumber].y,
    })

if __name__ == '__main__':
    marcherAPI.run(debug=True)

print(retrieveMarcher(0))