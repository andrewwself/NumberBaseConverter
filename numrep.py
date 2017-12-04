'''
Created on Feb 17, 2017

@author: Andrew Self
'''

def get_num():
    num= input('Enter a number: ')
    return num

def get_base():
    base= input('Enter starting base: ')
    return int(base)

def get_new():
    new=input('Enter desired base: ')
    return int(new)

def convert_to_decimal(num,base):
    nums=[int(element) for element in num]
    nums.reverse()
    decimal=0
    for exp,i in enumerate(nums, 0):
        #print(i,base, exp)
        decimal+= i*(base**exp)
    return decimal

            
def new_base(num,base,exp):       
    highest_num = 0
    highest_val= 0
    cur_exp = -1
    highest_exp = 0
    while True:
        #print("DEBUG")
        cur_exp +=1
        for i in range(0,base):
            val = i*(base**cur_exp)
            if (val < num) and (val > (highest_val)):
                highest_num = i
                highest_val = val
                highest_exp = cur_exp
            if val == num:
                zeroes = buildStr(exp-cur_exp-1)
                moreZeroes = buildStr(cur_exp)
                return zeroes+str(i)+moreZeroes
            if val > num:
                new = num - highest_val
                zeroes = buildStr(exp - cur_exp-1)
                return  zeroes + str(highest_num) + new_base(new, base, highest_exp)
            
def buildStr(num: int) -> str:
    string = ""
    for i in range(num):
        string += "0"
    return string
            
if __name__ == '__main__':
    num=get_num()
    base=get_base()
    new=get_new()
    x=convert_to_decimal(num,base)
    y=new_base(x,new,0)
    print(y)
