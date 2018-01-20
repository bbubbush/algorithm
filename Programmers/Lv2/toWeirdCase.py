'''
[ 이상한 문자만들기 ]
toWeirdCase함수는 문자열 s를 매개변수로 입력받습니다.
문자열 s에 각 단어의 짝수번째 인덱스 문자는 대문자로, 홀수번째 인덱스 문자는 소문자로 바꾼 문자열을 리턴하도록 함수를 완성하세요.
예를 들어 s가 try hello world라면 첫 번째 단어는 TrY, 두 번째 단어는 HeLlO, 세 번째 단어는 WoRlD로 바꿔 TrY HeLlO WoRlD를 리턴하면 됩니다.

주의 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단합니다.
'''

'''
[ 접근방법 ]
공백을 만날때 마다 소문자로 단어를 치환해야한다. 그래서 공백을 만남을 구분하기 위해 boolean변수를 두고
그 후엔 계속 upper와 lower를 번갈아가면서 사용했다. s의 길이를 n으로 볼때 o(n)의 시간복잡도를 갖는다.
'''


def toWeirdCase(s):
    switch = True
    result = ''
    for i in s:
        if( i == ' ' ):
            result += ' '
            switch = True
        elif( switch ):
            result += i.upper()
            switch = False  
        elif( not switch ):
            result += i.lower()
            switch = True
        
    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.wRvuh sNqfP OVan uQfyw
print("결과 : {}".format(toWeirdCase("try hello world")));
print("결과 : {}".format(toWeirdCase("abcd abc abc")));