class BMI:
    def __init__(self,name,age,weight,high):
        self.name = name
        self.age = age 
        self.weight =weight
        self.high = high
    def print_bmi1(self):
        getBMI=self.weight/(self.high*self.high)
        print("{x}的BMI是".format(x=self.name))
    
        if getBMI<18.5:
            print("偏瘦")
        elif getBMI< 24:
            print("正常")
        elif getBMI<30:
            print("偏胖")
        else:
            print("肥胖")
                 