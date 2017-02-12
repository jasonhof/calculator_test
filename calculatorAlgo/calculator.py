class simpleCalc(object):
    
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
    
    def set(self, in1, in2):
        self.input1 = in1
        self.input2 = in2

    def add(self, in1, in2):
        self.set(in1, in2)
        #self.add()
        result = self.input1 + self.input2
        #print(result)
        return result

    def subtract(self, in1, in2):
        self.set(in1, in2)
        #self.subtract()
        result = self.input1 - self.input2
        #print(result)
        return result
'''
    def add(self):
        result = self.input1 + self.input2
        print(result)
        return result

    def subtract(self):
        result = self.input1 - self.input2
        print(result)
        return result
'''