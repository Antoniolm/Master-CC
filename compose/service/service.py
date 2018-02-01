from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from pymongo import MongoClient
import pymongo
import os
import sys
import json
from bson import BSON
from bson import json_util

app = Flask(__name__)
client = MongoClient('mongo:27017')

@app.route("/")
def getRoot():
    return render_template('index.html',error=None)

###################################################################

@app.route("/object3d", methods=['GET', 'POST'])
def objects3d():
    db=client.object3D
    collection = db['collection']

    if request.method == 'GET':
        objects = collection.find({}, {'_id': False})
        return json.dumps({'results': list(objects)}, default = json_util.default, indent = 4)

    if request.method == 'POST':
        content= request.get_json()
        fileName = content.get('object')
        info = content.get('info')

        object3D = {"object": fileName,
            "information": info}

        collection.insert(object3D)

        return jsonify(addObjec3D="success")

    return jsonify(error="DontMethodDetected")

###################################################################

@app.route("/object3d/<fileName>", methods=['GET', 'POST' , 'DELETE'])
def object3d(fileName):
    db=client.object3D
    collection = db['collection']

    if request.method == 'GET':
        object3dInfo=collection.find_one({"object": fileName}, {'_id': False})
        return json.dumps(object3dInfo)

    if request.method == 'POST':
        content= request.get_json()
        newFileName = content.get('object')
        info = content.get('info')

        result = collection.replace_one(
            {"object": fileName},
            {"object": newFileName, "information": info}
        )
        return jsonify(updateObject3D="success")


    if request.method == 'DELETE':
        collection.delete_one({"object": fileName})
        return jsonify(removeObject3D="success")

    return jsonify(error="DontMethodDetected")

###################################################################

@app.route("/status")
def getStatus():
    return jsonify(
        status="OK",
    )

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
