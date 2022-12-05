from ast import literal_eval
import pymongo
import os
#import bson.json_util as json_util
import pandas as pd

myclient = pymongo.MongoClient("mongodb+srv://fdc-readonly-user:5cQgfxPO66oDDTGn@fdc-production.0nfd9.mongodb.net/")
#mydb = myclient["013aa734-0d5d-44ec-93e4-9732bbf93fa6"]
#mycol = mydb["batteries"]
pipeline = [
    {"$project":{"source": {"$cond": {"if": { "$eq": ['$reportedBy', 'Automatic'] },"then": 'central_server',"else": 'ui'}},"createdAt":1,"portId":1,"vehicleId":1,"title":1,"description":1,"reportedBy":1}},
	{"$lookup":{"from": "vehicles","localField": "vehicleId","foreignField": "_id","as": "vehicle"}},
	{"$lookup":{"from": "chargingport","localField": "portId","foreignField": "_id","as": "port"}}
]

res = []
headerFlag = False
for dbname in myclient.list_database_names():
	if dbname not in ['config', 'local', 'test']:
		db = myclient[dbname]
		cursor = db["faults"].aggregate(pipeline)
		#res.extend(list(cursor))
		df = pd.DataFrame(list(cursor))	
		if '_id' in df:
			del df['_id']
		#df1 = pd.json_normalize(db, 'trackTime')
		#df.to_csv(f'C:/Users/Electriphi/Documents/faults_prod/{dbname}.csv', index=False)
		output_path='C:/Users/Electriphi/Documents/faults_prod/exxample.csv'
		#df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))
		if(headerFlag == False):
			df.to_csv('C:/Users/Electriphi/Documents/faults_prod/exxample.csv', mode='a', index=False, header=True)
			headerFlag = True
		else:
			df.to_csv('C:/Users/Electriphi/Documents/faults_prod/exxample.csv', mode='a', index=False, header=False)
		print("done for %s" % (dbname))

#df = pd.DataFrame(res)
#df.to_csv(f'C:/Users/Electriphi/Documents/faults_prod/{dbname}.csv', index=False)
print("done")
		