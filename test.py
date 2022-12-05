import pymongo
import bson.json_util as json_util
import pandas

myclient = pymongo.MongoClient("mongodb+srv://fdc-readonly-user:5cQgfxPO66oDDTGn@fdc-production.0nfd9.mongodb.net/")
#mydb = myclient["013aa734-0d5d-44ec-93e4-9732bbf93fa6"]
#mycol = mydb["batteries"]
alist = []
for temp in myclient.list_databases():
	print(temp)
'''
with open("alle.json", "w") as outfile:
	for dbname in myclient.list_database_names():
		db = myclient[dbname]
		for r in db["vehicles"].find({"isDeleted" : False}):
			outfile.write(json_util.dumps(r))
			outfile.write(','+'\n')

'''
	#print("________________________________________________________________________")
	#print("________________________________________________________________________")
#jsonString = json.dumps(alist)
#jsonFile = open("data.json", "w")
#jsonFile.write(jsonString)
#jsonFile.close()