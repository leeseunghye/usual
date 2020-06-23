#a = int( input("숫자를입력해주세요:") )

# if (a > 10): #True/False
#     print("a가 10보다 큽니다")
# elif (a == 5):
#     print("a는 5입니다")
# else:
#     print("a는 10이거나 더 작군요")

# if (a>5):
#     print("a는 5보다 큽니다")

# if (a>0):
#     print("a는 자연수입니다")
    
# if (a>0):
#     print("a는 양수입니다")
    
#     if (a%2 == 0):
#         print("짝수입니다")
#     else:
#         print("홀수입니다")
        
# else:
#     print("a는 음수입니다")
    
###########주석으로 반복문###########
#ctrl+c를 누르면 종료

# i = 1

# while(i<1000):
#     print(i)
#     i = 1 + i

# tmp_str = "오늘은좋은날이구만요"
# for i in range( len(tmp_str) ):
#   print(tmp_str[i],"출력값 : ", i)
    
#print(list (range(5,10,2) ) )

#파이썬의 함수

# def forfunction(a):
    
#     for i in range(a):
#         print(i)

# forfunction(5)

# print("*" * 100)

# forfunction(10)

import random

a = random.randrange(2,10)
b = random.randrange(2,10)

answer = a*b

print(answer)