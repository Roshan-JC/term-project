class TransformData:

	def __init__(self):
		self._path = "/home/cloudera/Term_project/countries/"
		self.infile = open(self._path + "all.csv","r")
		self.outfile = open(self._path + "sorted.csv","w")
		self.__read_file()
       
	def __read_file(self):
   		for record in self.infile:
   			self.__process_data(record)
   			self.__write_file()

	def __write_file(self):
		writerec = self.country+","+self.year+","+self.participants+","+self.males+","+ self.females+","+self.sports+","+self.gold+","+self.silver+","+self.bronze+","+self.total+"\n"
		if self.year == "2012" or self.year == "2008" or self.year == "2004" or self.year == "2000" or self.year == "1996":
			self.outfile.write(writerec)
   			
	def __get_year(self, string):
		year = string.split(' ')
		return(year[0])

	def __process_data(self,record):
		strings = record.split(',')
		self.country = strings[0]
		self.year = (self.__get_year(strings[2]))
		self.participants = (strings[4])
		self.males =  (strings[5])
		self.females = (strings[6])
		self.sports = (strings[7])
		if strings[8] == "":
			self.gold = "0"
		else:
			self.gold = (strings[8])
		if strings[9] == "":
			self.silver = "0"
		else:
			self.silver = (strings[9])
		if strings[10] == "":
			self.bronze = "0"
		else:
			self.bronze = (strings[10])
		if strings[11] == "":
			self.total = "0"
		else:
			self.total = (strings[11]);
   		
