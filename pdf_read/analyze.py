from flask import Flask, request
from Marcher import Marcher
from PyPDF2 import PdfReader
import json

marcher_list= []

marcherAPI = Flask(__name__)

@marcherAPI.route('/api/retrieveMarcher', methods=['POST'])
def retrieveMarcher():
    if request.method == 'POST':
        marcher_objects= []

        raw = request.form.get('key')
        reader = PdfReader("raw")
        page = reader.pages[0]
        rawtext = page.extract_text()

        sheets = rawtext.split("Printed:")[:-1]

        for sheet in sheets:
            marcher_list.append(Marcher(sheet))
            marcher_index = sheets.index(sheet)
            marcher_dict = {
            'name': marcher_list[marcher_index].name,
            'counts': marcher_list[marcher_index].counts,
            'x': marcher_list[marcher_index].x,
            'y': marcher_list[marcher_index].y,
            }
            marcher_objects.append(marcher_dict)

    return json.dumps(marcher_objects,indent = 6)

if __name__ == '__main__':
    marcherAPI.run(debug=True)  