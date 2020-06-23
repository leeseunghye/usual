# a = 10
# b = 3
# print(a)
# print("a : ", a)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print('나눗셈에서 몫 :', a//b) #나눗셈의몫 
# print(type(a//b)) #정수 int
# print(type(a/b))  #실수 float

# a = "hello"
# b = 'good'
# c = "'이것은인용문'"
# d = '"이것은대사"'

# print(a)
# print(b)
# print(c)
# print(d)

# print(a+b)
# #print(a-b) #string에서는 - 지원하지 않음
# print(a*100)
# ## a== hello
# print(a[1]) # 0 1 2 ~~
# print(a[1:3])
# print(a[:3])
# print(a[2:])
# print( a.replace('l','b') ) #임시로 바꾼거지 a가 바뀐건 아님
# print(a)

# mytxt = int(input("요기다 : ")) #숫자로바꾸쟈
# print(type(mytxt))

# mylist = list() #빈 리스트
# mylist2 = []
# mylist3 = [1,2,3,4]
# mylist4 = ['글자',1, ['숫자',5] ]

# print(mylist4[2][1])
# print(mylist4[1:])

##메서드(편리한 기능)

# mylist.append("1")
# mylist.append("2")
# mylist.append("3")
# mylist.append("4")
# print(mylist)
# # mylist.remove("2")
# # print(mylist)
# # mylist.pop()
# # print(mylist)
# mylist.reverse()
# print("반전 :", mylist)
# mylist.sort()
# print("오름차순:", mylist)
# print(mylist.count("2"))

# tmp_str = ",".join(mylist) #쪼매어렵넹 하나의문자열로만듬
# print(tmp_str)

# result_list = tmp_str.split(",")
# print(result_list)

# result_list[1] = 5
# print(result_list) #str은 각 요소를 바꾸어줄수없어서..

# #자료형
# mytuple = ()
# mytuple2 = (1,)
# mytuple3 = (1,2,(1,2))
# mytuple4 = (1,2,4)
# mytuple5 = (1,2,5)

# mytuple3[0] = 100
# print(mytuple3) #내용을바꿀수없는 list다!!!! 

#딕셔너리는 사전형으로 빠르게 불러올 수 있다
mydict = {1:'hello'}
mydict1 =dict()
mydict2 = {}
mydict3 = {"가":1, "나":"두번째", "다":[1,2,3]}

print(mydict3["나"])
print(mydict3["다"])
mydict3["라"] = "비어있으니넣자"
mydict3["라"] = "아!"
print(mydict3)

print(mydict3.keys())
print(mydict3.items()) #키 - 밸류
print(mydict3.values())


print(mydict3.get("멋직"))#none
print(mydict3["멋직"])