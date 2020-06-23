#인풋
word1 = input("끝말잇기를 시작하지 : ") #인풋의 값은 기본적으로 string(글자.스트링)
#세 글자 까지만 허용하자. 라고 생각했다.
if (len(word1) == 3) :
    #계속진행
    while True:   
        word2 = input()
        
        #인풋의 끝자리 음절과
        #다음 인풋의 첫 음절이 같아야 성공
        if (len(word2) == 3) and (word2[0] == word1[2]):
            print("정답입니다")
        else:
            print("오답입니다")
            
            break


else:
    print("오답이오")
    #종료
    
print("게임이 종료되었습니다.")