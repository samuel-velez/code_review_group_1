# Advanced function(s)
## Code Attribution: Code snippets taken and adapted from https://towardsdatascience.com/how-to-be-pythonic-and-why-you-should-care-188d63a5037e

def even_value_doubler(array_to_double = [1,2,3,5,6,7,9,10,12]):
    """ 
    IM PRETTY SURE I BROKE IT MORE 
    This function allegedly takes an list array of numbers and doubles the value of every even value in the list.
    """

    arr = array_to_double
    empt = []
	length = len(array_to_double)

	for i in range(0, length):
	    empt[i] = arr[i]*2
        
	return empt

def here_is_a_challenge(bar=[]): # bar is optional and defaults to [] if not specified
    """
    What is wrong with this function!? 
    Hint: Try running this a few times

    Attribution: Code taken directly from: https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make
    """ 
	bar.append("baz")
	return bar