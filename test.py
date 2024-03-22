import math
#calculates the mean
def mean(data):
    total = 0
    for i in data:
        total += i
    return total/len(data)

# data is sorted into an array of tuple (time, variable)
def trend(data):
    
    times = []
    data = []
    
    #separating the data into its relative times and data
    for i in data:
        times.append(i[0])
        data.append(i[1])
    
    #calculates mean
    meantime = mean(times)
    meandata = mean(data)

    timestemp = []
    datatemp = []

    #x - x(mean)
    for x in times:
        timestemp.append(x-meantime)
    
    #y - y(mean)
    for y in data:
        datatemp.append(y-meandata)

    #sum of (x-x(mean)) * (y - y(mean)) as well as (x - x(mean)) and (y - y(mean))
    sumxy = 0
    sumx_sqr = 0
    sumy_sqr = 0
    for i in range(len(times)):
        sumxy += timestemp[i] * datatemp[i]
        sumx_sqr = timestemp[i] ** 2
        sumy_sqr = timestemp[i] ** 2

    return sumxy / math.sqrt(sumx_sqr * sumy_sqr)