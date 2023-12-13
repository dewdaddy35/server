import pymongo 
import certifi

me = {
        "first": "Eric",
        "last": "Wells",
        "email": "eric.wells41@gmail.com"
    }

con_str="mongodb+srv://FSDI:Test1234@fsdi.4arocgi.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("Jackson_Wear")
