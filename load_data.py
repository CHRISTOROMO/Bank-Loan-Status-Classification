 # import library to read data from file
import pandas as pd


class Data:
  
    def __init__(self, url):
        self.url = url
        self.data = pd.read_csv(self.url, sep = ",")
      

    def loading_data(self):
      return self.data

    def data_shape(self):
      return f'The dataset has {self.data.shape[0]} rows and {self.data.shape[1]} columns'

    def data_types(self):
      return self.data.dtypes

    def data_info(self):
      return self.data.info()

    def data_describe(self):
      return self.data.describe()

    def data_head(self):
      return self.data.head()

    def data_tail(self):
      return self.data.tail()

    def data_columns(self):
      return self.data.columns

    def print_results(self):
      print('Loading the data...')
      print('='*50)
      print('Top part of the data...')
      print(self.data_head())
      print('='*50)
      print('Bottom part of the data...')
      print(self.data_tail())
      print('='*50)
      print('Shape of the data...')
      print(self.data_shape())
      print('='*50)
      print('What about the data...')
      print(self.data_info())
      print('='*50)
      print('Column datatypes...')
      print(self.data_types())
  




      

