'''
[ 멀리뛰기 ]
효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는

	(1칸, 1칸, 1칸, 1칸)
	(1칸, 2칸, 1칸)
	(1칸, 1칸, 2칸)
	(2칸, 1칸, 1칸)
	(2칸, 2칸)

의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이
몇 가지인지 출력하는 jumpCase 함수를 완성하세요. 예를 들어 4가 입력된다면, 5를 반환해 주면 됩니다.
'''

'''
[ 접근방법 ]
고생 많이 했다. 카페서 몇 시간동안 붙잡고 풀어도 답이 안나와서 매우 분노하며 다른 분의 풀이를 검색해서 보고 풀었다.
그래서 그 분의 설명을 이해한 대로 끄적여보겠다.

효진이는 1칸 혹은 2칸만 이동할 수 있다. 혹여나 효진이가 체력이 안좋아 1칸만 이동할 수 있다면 n이 몇이든 경우의 수는 1밖에 없다.

효진이의 능력은 변하지 않으니깐 변할 수 있는 n에 대해 접근해보겠다.

	n = 0일 땐 가만히 있는 방법밖에 없다.
	n = 1일 땐 1칸만 뛰는 경우밖에 없다.
	n = 2일 땐 1칸씩 두 번, 2칸씩 한 번 이동하는 경우가 있다.
	n = 3일 땐? 여기부터 머리가 아퍼진다.

그래서 상황을 조금 다르게 생각해 보겠다. n = 3일 때 1번째 칸 혹은 2번째 칸에 효진이는 꼭 도착해야 한다. 
한 번에 3칸 이상 점프할 수 없기 때문에 꼭 거쳐가야한다.

그러므로 1번째 칸에 머푼 효진이는 1칸을 한번 이동하는 경우의 수를 통해 도착했다. 도착했다.
2번째 칸에 머문 효진이는 2칸을 한번 이동하는 경우의 수와 1칸씩 두번 이동하는 경우의 수, 2가지 방법이 존재한다.

여기서부터가 중요하다. 효진이가 1번 칸에 있는 경우에는 2칸을 이동하여 3번 칸에 도착하는 방법밖에 없다. 한칸만 움직이는 순간, 
2번칸에서 움직이는 경우의 수와 중복이 되기 때문이다.

효진이가 2번칸에 있는 경우도 마찬가지다. 이 경우엔 한칸 움직는 선택지 말고는 없다. 이를 식으로 나타내면 아래와 같다.

	(1칸까지 이동하는 경우의 수 * 1칸에서 3칸으로 가는 경우의수) + (2칸까지 이동하는 경우의 수 * 2칸에서 3칸으로 가는 경우의 수) = 3칸으로 오는 경우의 수

위의 식 중에 1에서 3칸으로 가는 경우의 수와 2칸에서 3칸으로 가는 경우의 수는 한가지 밖에 없으니 1이라 하면 

    n칸으로 오는 경우의 수 = n-1칸으로 오는 경우의 수 + n-2칸으로 오는 경우의수

이렇게 식이 정리가 된다.

재귀함수다. 미래의 육상 꿈나무인 효진이 덕분에 우리는 재귀를 공부할 수 있게 되었다! 아래 코드는 재귀에서 중복되는 연산을 Memoization을 통해 제거하는 코드이다.

Memoization을 알려준 민구형님께 이 시간을 빌어 감사를 전한다.
'''

listA = [1, 1]  
def jumpCase(num):
    if len(listA) > num:
    	return listA[num]

    if num < 2:
    	return num
    
    listA.append(jumpCase(num-1) + jumpCase(num-2))
    
    return listA[num]

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(5))
