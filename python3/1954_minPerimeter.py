class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        i = 1
        apples = 0 
        while True:
            apples += i*4
            apples += i*2*4
            if i%2:
                apples += (i+i*2)*(i-1)*4
            else:
                apples += ((i+i*2)/2 + (i+i*2)*((i-1)//2))*8
            if apples >= neededApples:
                return i*8
            i += 1