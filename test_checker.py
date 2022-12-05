import pymongo
import csv
import pandas

myclient = pymongo.MongoClient("mongodb+srv://electriphi-fmt-root:UH9rHUM4RWQG6aw@fleet-production-2.0nfd9.mongodb.net/")
#mydb = myclient["013aa734-0d5d-44ec-93e4-9732bbf93fa6"]
#mycol = mydb["batteries"]
for dbname in myclient.list_database_names():
	db = myclient[dbname]
	collection = db["settings"]
	df = pandas.DataFrame(list(collection.find()))
	df.to_csv('mycsvfile2.csv')