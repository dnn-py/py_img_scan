import pymongo
from pymongo import MongoClient

def drop_files():
	global db
	db.drop_collection('files')

def ins(file):
    global files
    files.insert_one(file)


def list_ext():
    global files
    # result = files.aggregate([{$group: {_id: "$ext", "count": {$sum: 1}}}])
    result = files.aggregate([{'$group':{'_id': '$ext', 'total': { '$sum': 1} } } ] )
    #     db.files.aggregate([{$group:  {_id: '$ext', count: {$sum: 1}}}])
    return result


# client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client.dnn
files = db.files
