import functions as fn
import classes as c
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import inspect as imp

d = c.dynamic()
d.name = "jon"
print(d.__dict__)

#classes
myclass = c.Student("Jon",1)
myclass.identifier = 37     #change property value
myclass.age = 18
for v in myclass.__slots__:
    if v.isalpha():
        print(v)

print(myclass.__slots__)
#print(myclass.__dict__.values)     #doesnt work - potentially slots

print(c.Student2.age)       #age is a public property, cant view name as private
myclass2 = c.Student2("Jon","JB")
attrs = vars(myclass2)      #doesnt include age (public)
print (', '.join("%s: %s" % item for item in attrs.items()) )
mylist= []
for prop in myclass2.__dict__.values():
    mylist.append(prop)
print(mylist)
#print(myclass.__slots__)
print(c.Student.__dict__)

a = c.A(1,2)
for prop in a.__dict__.values():
    print(prop)



#dictionary
mydict = {"jon":38,"aidan":34}
print(mydict["jon"])

#numpy practice
myArr = np.array([(1,2,3),(4,4,5)])
print(np.mean(myArr,axis = 0)) #average columns
print(np.mean(myArr,axis = 1)) #average rows
print(myArr.shape)
myArr2 = myArr.reshape(3,2)
print(myArr2)

arr = np.array([[1, 2, 3],
                [4, 2, 5]])

#characteristics
print("Array is of type: ", type(arr))
print("No. of dimensions: ", arr.ndim)
print("Shape of array: ", arr.shape)
print("Size of array: ", arr.size)
print("Array stores elements of type: ", arr.dtype)

#iterate over numpy array
for x in np.nditer(myArr):
    print(x)

#battery algo
mydict = {}
mydict2 = {}
num_batteries = 8
for x in range(0,num_batteries):
    mydict[x] = False
    mydict2[x] = False

for x in range(0, num_batteries):
    if mydict[x] == False:
        for y in range(x+1,num_batteries):
            if fn.light(x,y) == True:
                mydict[x] = True
                mydict[y] = True

#alternative
xit = False
while xit == False:
    for y in range(0, num_batteries):
         if fn.light(x, y) == True:
             mydict2[x] = True
             mydict2[y] = True
             xit = True

print(mydict2)
print(mydict)

#map and filter
mylist = [0,1,3,5,6]
newlist = list(map(lambda x: x * 2,mylist))
newlist1 = list(filter(lambda x: x % 2 == 0,mylist))

print(newlist)
print(newlist1)

#len vs count
if len(mylist) == 5:
    print(mylist.count(1))

my_list = []
for i in range(5):
    my_list.append(i)

print(my_list[0])
print(list(map(lambda x:x**2,my_list)))

#function as a variable
myfunc = fn.light(1,2)
#x = myfunc(1,2)
print(myfunc)

#pandas - load data
path = 'C:/Users/John/PycharmProjects/'
airports = pd.read_csv(path + 'airports.csv')
airport_freq = pd.read_csv(path + 'airport-frequencies.csv')
#runways = pd.read_csv(path + 'data/runways.csv')

print(airports.head(5))
mx = airports.id.max()
single_col = airports['id'] #or airports.id
distinct_col = airports.type.unique()
print(distinct_col[0]) #can also use head(3)
select_cols = airports[['ident', 'name', 'municipality']]
where_clause = airports[(airports.iso_region == 'US-CA') & (airports.type == 'seaplane_base')]

#merge & groupby
freq_subset = airport_freq.groupby(['airport_ident'])['frequency_mhz'].sum()
print(freq_subset.head(5))
final = airports.groupby(['iso_country']).size().head(5)
merge_ = pd.merge(freq_subset, airports[['ident','id']], left_on='airport_ident', right_on='ident')
print(merge_.head(5))
#print(airports.groupby(['iso_country', 'type'])['Number'].sum())
#to_frame adds size header, reset_index provides a new frame and row numbers
#print(airports.groupby(['iso_country', 'type']).size().to_frame('size').reset_index())

#matplotlib
plt.plot(final)
#plt.show()





