class Solution:
    def reverse(self, x: int) -> int:
        a= 0
        if x < 0:
            x = -x
            a= 1
        # 1. split하기 (나머지로)
        #(1) x의 자릿수를 찾습니다. 
        
        n=1 
        while True: 
            if (x / 10**n < 1) :
                break
            n+=1
        
        #(2) 각 n자리면 --> 1 .. 1자리면 n자리로 뒤집습니다. 
        new_x = 0
        for i in range(1,n+1):
            new_x += ((x % 10**i)//10**(i-1)) * 10**(n-i)
        if a==1: 
            new_x = -new_x
        #2. 부호는 앞으로 빼고 새로운 정수 생성 
        if new_x > (2**31)-1 or new_x < -(2**31):
            new_x = 0
    
        return new_x 