class Indexer:

    def __init__(self):
        self.data = [1,2,3,4,5,6,7,8,9,10]
    def __getitem__(self, item):

        return self.data[item]


    def __setitem__(self, key, value):
        print(key,value)
        self.data[key] = value

x = Indexer()
x[1:10] = [1000]*9

print(x[::])