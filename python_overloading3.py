class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks> other.marks
    def __le__(self,other):
        return self.marks<=other.marks

s=student("dibya",100)
s1=student("ravi",80)
print(s>s1)
print(s<s1)

print("*************************************************")

class dibya:
    def __init__(self,roll,marks):
        self.roll=roll
        self.marks=marks
    def __ipow__(self,other):
        return self.roll**other.marks
    def __imod__(self,other):
        return self.roll% other.marks
d=dibya(2000,100)
d2=dibya(3000,200)
print(d**d2)
print(" i want to lear a lot")
