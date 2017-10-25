""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
	import numpy

	np_array = numpy.array(arr)

	min = np_array.min()
	max = np_array.max()

	return (np_array - min)/float(max - min)

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)

