from flask import Flask, request, jsonify
from Marcher import Marcher
from PyPDF2 import PdfReader
from flask_cors import CORS
import json

marcher_list= []

marcherAPI = Flask(__name__)
CORS(marcherAPI)
@marcherAPI.route('/api/retrieveMarcher', methods=['POST'])
def retrieveMarcher():
    if 'pdfFile' not in request.files:
        return jsonify({'error': 'No PDF file uploaded'}), 400

    pdf_file = request.files['pdfFile']

    if pdf_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if pdf_file:
        try:
            # Read the uploaded PDF file
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[0]
            raw_text = page.extract_text()

            sheets = raw_text.split("Printed:")[:-1]

            marcher_objects = []

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

            
            return json.dumps(marcher_objects[0])
        except Exception as e:
            return jsonify({'error': 'Error processing PDF file'}), 500
        
if __name__ == '__main__':
    marcherAPI.run(debug=True)  