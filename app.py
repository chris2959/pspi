
from flask import Flask,jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT
from flask import request


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])



@app.route("/search",methods=["GET"])
def search():
    query=mongo.db.products.find({"name":request.args.get("name")})
    data=[]
    for element in query:
        element['_id']=str(element['_id'])
        data.append(element)
    return jsonify(data)

@app.route("/add-product", methods=["POST"])
def addproduct():
    product = {
        "_id": str(request.args.get("id")),
        "name": request.args.get("name"),
        "production_year": int(request.args.get("production_year")),
        "price": int(request.args.get("price")),
        "color":int( request.args.get("color")),  # Use a string value for color
        "size":int( request.args.get("size")),    # Use a string value for size
    }
    mongo.db.products.insert_one(product)
    return jsonify(product)


#@app.route("/content-based-filtering", methods=["POST"])
#def content_based_filtering():
    # BEGIN CODE HERE
 #   return ""
    # END CODE HERE


#@app.route("/crawler", methods=["GET"])
#def crawler():
    # BEGIN CODE HERE
  #  return ""
    # END CODE HERE

if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
  

    app.run()