from flask import Flask, request
from config import me,db
from mock_data import catalog
import json

#flask is helping us create the APIs

app = Flask(__name__)#name of the folder (Server)

@app.get("/")
def home():
    return "Hello from Flack!"

@app.get("/test")
def test():
    return "This is a test page!"

######################################
############ API - Products ##########
######################################


@app.get("/api/about")
def about():
    return json.dumps({"version": 1.03, "name": 'stables3'})

@app.get("/api/about/me")
def about_me():
    
    return json.dumps(me)



@app.get("/api/product")
def get_products():
    return json.dumps(catalog)


@app.post("/api/product")#add data 
def save_products():
    product = request.get_json()
    #save to database 
    db.products.insert_one(product)
    print(product)
    return json.dumps(product)

@app.get("/api/product/count")
def product_count():
    total = len(catalog)
    return json.dumps({"total": total})

@app.get("/api/reports/total")
def get_total():
    total = 0
    for product in catalog:
        total += product["price"]
    
    return json.dumps({"value": total})#subtotal of all products ordered
#get /api/catagories
# should return a list of the catagories
@app.get("/api/categories")
def get_categories():
    count = []
    for product in catalog:
       category = product["category"]
      
       if category  not in count:
           count.append(category)
    return json.dumps(count)

# get /api/product/category/shoes
# return a list of products for given category
@app.get("/api/product/category/<category>")
def product_by_category(category):

    items = []

    for product in catalog:
        if product["category"].lower() == category.lower():
            items.append(product)
        
    return json.dumps(items)
   

#get /api/product/search/items
@app.get("/api/product/search/<term>")
def product_search(term):

    search = []
    for product in catalog:
        if term.lower() in product["title"].lower():
            search.append(product)

    return json.dumps(search)




app.run(debug=True)#applying the changes to the code