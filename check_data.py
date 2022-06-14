# let's create a function to check the data


def check_data(data):
    # printing the head of the data
    print(data.head())
    # printing the tail of the data
    print(data.tail())


def info(data):
    # printing the info of the data
    print(data.info())


def shape(data):
    # printing the shape of the data using a statement
    print(f"The data has {data.shape[0]} rows and {data.shape[1]} columns")


def describe(data):
    # describing the data
    print(data.describe())


def unique(data):
    # printing the data types of the data
    print(data.dtypes)


# let's create a class to habour the functions above
class DataCheck:
    def __init__(self, data):
        self.data = data

    def check_data(self):
        check_data(self.data)

    def info(self):
        info(self.data)

    def shape(self):
        shape(self.data)

    def describe(self):
        describe(self.data)

    def unique(self):
        unique(self.data)
