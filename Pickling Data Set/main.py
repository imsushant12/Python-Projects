import requests
import pickle

req = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# reading the data from url.
# print(req.content)

# writing the data into a text file.
open("dataSet.txt" , 'wb').write(req.content)

# an empty list to store data-sets
l1 = []

# opening file and converting it in form of
f = open("dataSet.txt" , 'r')
lines = iter(f.readlines())
while True:
     try:
        line = next(lines)
        l1.append(line)
     except StopIteration:
        break
f.close()

with open("iris.pkl" , "wb") as f:
    pickle.dump(l1 , f)

# # To read the pickled file:
# with open("iris.pkl" , "rb") as f:
#     print(pickle.load(f))
