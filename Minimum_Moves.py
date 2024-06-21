class Solution(object):
    def minMovesToSeat(self, seats, students):
       seats.sort()
       students.sort()      
       moves=0
       for i,j in zip(seats,students):
           moves += abs(i-j)
       return moves         

           
               
               

Sol=Solution()
seats=[3,1,5]
students=[2,7,4]
ans=(Sol.minMovesToSeat(seats,students))
print(ans)