import pandas as pd
class DATA_READ():
    def __init__(self,file_path):
        self.file_path = file_path
    def read_data(self):
        data = pd.read_csv(self.file_path)
        return(data)
    
if __name__ == "__main__":
    path = "C:\\Users\\swaga\\NareshIT\\Sessions\\Visadataset.csv" 
    obj = DATA_READ(path)
    data = obj.read_data()
    print(data)