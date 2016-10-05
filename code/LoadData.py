import csv
import json
import pymongo
from pymongo import MongoClient


class LoadData:
	def __init__(self):
		self._path = "/home/cloudera/Term_project/countries/"
		self.infile = open(self._path + "sorted.csv","r")
		self.outfile = open(self._path + "Olympicsdata.json","w")
		self.__connect_database()
		self.__csvtojson()
		self.__LoadtoMongo()

	def __connect_database(self):
		connection=MongoClient()
		self.db=connection.olympics
		self.collection=self.db.data

	def __csvtojson(self):
		fieldnames = ("country","year","participants","male","female","sports","gold","silver","bronze","total")
		reader = csv.DictReader( self.infile, fieldnames)
		out = json.dumps( [ row for row in reader ] )
		self.outfile.write(out)
		self.outfile.close();

	def __LoadtoMongo(self):
		jsonfile=open(self._path + "Olympicsdata.json",'r')
		jsonarray=json.loads(jsonfile.read())
		for document in jsonarray:
		   self.collection.insert(document) 
	


 