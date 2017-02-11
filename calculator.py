class jasonCalc:
    input1 = 0
    input2 = 0
    
    def set(self, in1, in2):
        self.input1 = in1
        self.input2 = in2
        
    def add(self, in1, in2):
        self.set(in1, in2)
        self.add()
    
    def add(self):
        result = self.input1 + self.input2
        print(result)
        return result
    
    def subtract(self, in1, in2):
        self.set(in1, in2)
        self.subtract()
    
    def subtract(self):
        result = self.input1 - self.input2
        print(result)
        return result