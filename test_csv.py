import pymongo
#import bson.json_util as json_util
import pandas as pd

myclient = pymongo.MongoClient("mongodb+srv://fdc-readonly-user:5cQgfxPO66oDDTGn@fdc-production.0nfd9.mongodb.net/")
#mydb = myclient["013aa734-0d5d-44ec-93e4-9732bbf93fa6"]
#mycol = mydb["batteries"]
count=0
for dbname in myclient.list_database_names():
	if dbname not in ['config', 'local', 'test']:
		db = myclient[dbname]
		cursor = db["chargingport"].find()
		df = pd.DataFrame(list(cursor))
		if '_id' in df:
			del df['_id']
		df.to_csv(f'C:/Users/Electriphi/Documents/charge_port_prod/{dbname}.csv', index=False)
		count+=1
		print("done for %s" % (dbname))
print("%d" % (count))