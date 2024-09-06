import numpy
def Average(lst):
    avg = numpy.average(lst)
    return(avg)


lst = [15, 9, 55, 41, 35, 20, 62, 49]

print("Average of the list =", round(Average(lst), 2))
