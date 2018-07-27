#클레스 상속과 오버라이딩
class Cal():
    def __init__(self, value):
        self.value = value

    def result(self):
        print(self.value)

    def add(self, input_value):
        self.value += input_value # += : self.value + input_value

    def sub(self, input_value):
        self.value - inut_value

    def mul(self, input_value):
        self.value *= input_value

    def div(self, input_value):
        self.value /= input_value

class SafeCal(Cal):
    def __init__(self, value):
        self.value = value

    def div(self, input_value):
        if (input_value ==0):
            self.value = 0
        else:
            self.value /= input_value    
                     

cal1 = Cal(0)
cal1.add(10)
cal1.result()

cal2 = SafeCal(0)
cal2.add(10)
cal2.result()
cal2.div(0)
cal2.result()
