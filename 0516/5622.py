#1을 걸려면 2초 2를 걸려면 3초 
#그럼 n을 걸기 위해선 n+1초가 걸린다고 
#알파벳별로 해당하는 숫자가 정해져있다고 
#연속된 알파벳은 그냥 더해지지만
#연속되지 않은 알파벳일때는 1씩 1씩 움직일때마다 더해져야함
S=str(input())
a = ['a','b','c']

for i in S:
     if i in a:
          
