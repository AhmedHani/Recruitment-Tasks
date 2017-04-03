___author__ = 'Ahmed Hani Ibrahim'
from reader import DataReader
from analysis import Analyzer

file_path = './data/data_science_dataset_wuzzuf.csv'

reader = DataReader(file_path)
data = reader.read_data()
analyzer = Analyzer(data)

analyzer.trending_category()

x = 0