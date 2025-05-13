import pandas as pd
class READ_DATA:
    def __init__(self,file_path):
        self.file_path = file_path
    
    def read_data(self):
        data = pd.read_csv(self.file_path)
        return(data)
        
if __name__ == "__main__":
    obj = READ_DATA("C:\\Users\\swaga\\NareshIT\\Sessions\\Visadataset.csv")
    data = obj.read_data()
    print(data)