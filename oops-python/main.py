from data_read import DATA_READ

obj = DATA_READ("C:\\Users\\swaga\\NareshIT\\Sessions\\Visadataset.csv")
data = obj.read_data()
print(data.shape) 