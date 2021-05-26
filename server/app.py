# app.py

# Required imports
import markdown
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
from ocrOnlyUpload import *
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
cors = CORS(app)

# Initialize Firestore DB


try:
    #app = firebase_admin.get_app()
    db = firestore.client()
    ticket_ref = db.collection('ticketreader')
except ValueError as e:
    cred = credentials.Certificate('config.json')
    default_app = initialize_app(cred)
    db = firestore.client()
    ticket_ref = db.collection('ticketreader')

"""
cred = credentials.Certificate('config.json')
default_app = initialize_app(cred)
db = firestore.client()
ticket_ref = db.collection('ticketreader')
"""


@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return md_template_string


@app.route('/add', methods=['GET', 'POST'])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        # id = request.json['id']
        # todo_ref.document(id).set(request.json)
        content = request.get_data()
        text = str(content, encoding="utf-8")
        rawText = r'{}'.format(text)

        print(content)

        extraerinformacion(rawText)

        return {"Success": True}, 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/listAll', methods=['GET'])
def readAll():
    """
        readAll() : Fetches all ticket documents 
        todo : Return document that matches query ID.
        all_todos : Return all documents.
    """
    try:
        all_tickets = [doc.to_dict() for doc in ticket_ref.stream()]
        # return jsonify(all_tickets[0]['tickets'])
        return jsonify(all_tickets)
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/listWeek', methods=['GET'])
def readWeek():
    """
        read() : Fetches documents from Firestore collection as JSON.
        todo : Return document that matches query ID.
        all_todos : Return all documents.

    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    """

    return jsonify({"weeklyTickets": True}), 200


@app.route('/netValue', methods=['GET'])
def readNetValue():
    """
        readAll() : Fetches all ticket documents 
        todo : Return document that matches query ID.
        all_todos : Return all documents.
    """
    try:
        # all_tickets = [doc.to_dict() for doc in ticket_ref.stream()]
        # value = all_tickets[0]['netValue']
        value = 0
        docs = ticket_ref.get()
        for doc in docs:
            auxDict = doc.to_dict()

            # clean data
            data = auxDict['Coste'].split()[0]

            # add new value
            value = value + float(data)

        return jsonify({"netValue": value}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
