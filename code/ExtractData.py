class ExtractData:
	def __init__(self):
		self._pwd = "/home/cloudera/Term_project/countries/"
		self.infile = open(self._pwd+"countries.csv","r")
		self.outfile = open(self._pwd+"all.csv","w")
		self.__read_infile()
		

	
	def __read_infile(self):
		for record in self.infile:
			data = record.split(',')
			self.datafile = data[0]
			self.country = data[1]
			self.__process_file()
				

	def __process_file(self):
		file = open(self._pwd + self.datafile)
		file.readline()
		file.readline()
		for record in file:
			data = self.country + "," +record
			self.outfile.write(data)
		self.outfile.write('\n')	
			
	