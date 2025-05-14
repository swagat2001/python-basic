import pandas as pd
class FREQUENCY_TABLE:
    def __init__(self,file_path,col):
        self.file_path = file_path
        self.col = col
 
 
    def csv_read(self):
        data = pd.read_csv(self.file_path)
        return(data)
    def table_creation(self):    
        data = pd.read_csv(self.file_path)
        keys = data[self.col].value_counts().keys()
        valuess = data[self.col].value_counts().values
        df = pd.DataFrame(zip(keys,valuess),columns=['Labels','Count'])
        df.to_csv(f'{self.col}_df.csv',index = False)
        
if __name__ == "__main__":
    obj = FREQUENCY_TABLE("C:\\Users\\swaga\\NareshIT\\Sessions\\Visadataset.csv",'continent')
    obj.table_creation()