class calcMax(object):
    def __init__(self):
        self.input = []
    
    def set(self, array):
        self.input = array
    
    def findMax(self, array):
        #i = 0
        print(array)
        max = array[0]
        for i in range(len(array)):
            if array[i] > max:
                max = array[i]
        return max