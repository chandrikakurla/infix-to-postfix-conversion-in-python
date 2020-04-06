#class for converting
class Converter:
    def __init__(self):
        self.top=-1
        self.stack=[]
        self.output=[]
        self.precedence_order={'+':1,'-':1,'*':2,'/':2,'^':3}
    #function for checking stack is empty or not
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            False
    #function for finding top of stack
    def peek(self):
        return self.stack[-1]
    #function for popping elements from stack
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.stack.pop()
    #function for pushing elements into stack
    def push(self,operator):
        self.top+=1
        self.stack.append(operator)
    #function for checking given character is operand
    def isOperand(self,cha):
        return cha.isalpha()
    #checking precedence order
    def less_Precedence(self,i):
        try:
            a=self.precedence_order[i]
            b=self.precedence_order[self.peek()]
            if a<=b:
                return True
            else:
                False
        except KeyError:
            return False
    #conversion
    def infix_2_postfix(self,exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif(i=='('):
                self.push(i)
            elif(i==')'):
                while((not self.isEmpty())and self.peek()!='('):
                    pop=self.pop()
                    self.output.append(pop)
                if(not self.isEmpty() and self.peek()!='('):
                    return
                else:
                    self.pop()
            #checking for operators
            else:
                while(not self.isEmpty() and self.less_Precedence(i)):
                    self.output.append(self.pop())
                self.push(i)
        #popping all operators from stack
        while(not self.isEmpty()):
            self.output.append(self.pop())
            
        print("".join(self.output))
if __name__=="__main__":
    exp="a+b*(c^r-d)+s-(l+m)"
    element=Converter()
    element.infix_2_postfix(exp)



