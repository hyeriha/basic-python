# class = 함수와 변수의 집합.
# 
class Hy:
    #변수 사용
    #분모
    mother = 0
    #분자
    son = 0
    def pp(self):
        print(str(self.son) + "/"+str(self.mother))

    #최대공약수
    def gcd(self,a,b): 
        '''
        return the greatest common divisor of a and b 
        gcd (10,5) -> 5 
        '''
        if b == 0 :
            return a 
        else:
            return self.gcd(b,a%b)
    
    
    # 생성자
    def __init__(self,y,x):
        self.mother = x
        self.son = y
    def sum(self,cl):
        x = self.son +cl.son
        if (self.mother == cl.mother):
            return Hy(x,self.mother)
        else:
            y= self.mother*cl.mother
            
            k=(self.mother*cl.son)
            b=(self.son*cl.mother)
            q=k+b
            o=(self.gcd(q,y))
            return Hy(int(q/o),(int(y/o)))
    def mul(self,cl) :
        a= self.mother*cl.mother
        b= self.son*cl.son
        k=(self.gcd(a,b))
        return Hy(int(b/k),int(a/k))

    # def doit(self,a,b):
    #    k=3*(a+b)
    #    k.reversed()
    #    p=a+1
    #    return (k/p)
    def inverse(self):
        return Hy(self.mother,self.son)
        
c  = Hy(2,5)
c1 = Hy(3,4)
x = c.mul(c1)

w1=Hy(1,2)
w2=x.sum(w1)
w3=Hy(3,1)
w4=w2.mul(w3)

w7=Hy(1,1)
w6=x.sum(w7)
w9=w6.inverse()
w8=w4.mul(w9)
w8.pp()
# t2 =c.mul(c1)
# t2.pp()
#
# p4=(t2,t1,t2)
# p4.pp()
