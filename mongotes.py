import pymongo


client = pymongo.MongoClient("mongodb://Ravisharad:THEgunner@ac-g0prr1s-shard-00-00.bjs2svw.mongodb.net:27017,ac-g0prr1s-shard-00-01.bjs2svw.mongodb.net:27017,ac-g0prr1s-shard-00-02.bjs2svw.mongodb.net:27017/?ssl=true&replicaSet=atlas-pvwxc4-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotes']
coll = db1['test']
coll.insert_one(d )
