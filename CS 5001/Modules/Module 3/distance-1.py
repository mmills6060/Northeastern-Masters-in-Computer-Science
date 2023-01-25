''' Align Online
    CS5001
    Sample code -- a function to determine the Euclidean
    distance between two points (don't forget to test it!)
'''

def euclidean(x1, y1, x2, y2):
    ''' Function euclidean
        Parameters: four floats, representing two points
        Returns: a float, the distance between the two points
    '''
    x_diff = (x2 - x1) ** 2
    y_diff = (y2 - y1) ** 2
    dist = (x_diff + y_diff) ** 0.5
    return dist

