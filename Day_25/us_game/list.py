import pandas

class Data(pandas):
    def __init__(self):
        super().__init__()
        self.pandas.read_csv("50_states.csv")