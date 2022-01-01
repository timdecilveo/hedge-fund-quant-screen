import pandas as pd

class Directory:
    def __init__(self, directory):
        self.directory = directory

    def files(self):
        file_list = []

        for file in self.directory:
            dataframe = pd.read_csv(f"../data-files/{file}", parse_dates=["Date"], index_col="Date")
            file_list.append(dataframe)
        return file_list

    def benchmark(self):
        file_list = []

        for file in self.directory:
            dataframe = pd.read_csv(f"../benchmarks/{file}", parse_dates=["Date"], index_col="Date")
            file_list.append(dataframe)
        return file_list
