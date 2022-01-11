# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다. (1은 소수가 아닙니다.)

# n은 2이상 1000000이하의 자연수입니다.

import math;


def solution(n):
    answer_arr = [];  # 소수를 담을 배열
    answer = 0;  # 소수의 개수
    arr = [True for i in range(n + 1)];  # n까지의 배열을 만드는데, 일단 전부 소수라고 가정(True)한다.

    for m in range(2, int(math.sqrt(n) + 1)):  # 2부터 n의 제곱근까지 반복문 돌리기
        if arr[m] == True:  # 이 배열 안에 가장 작은 자연수부터 시작
            x = 2;  # 배수가 될 변수 x. 2배수부터 시작
            while m * x <= n:  # 입력받은 n이하일 때까지 m의 배수를 찾음
                arr[m * x] = False;  # 그리고 m의 배수에 해당하는 애들은 전부 False로 바꿈(소수가 아님)
                x += 1  # 배수를 늘려가면서 계속 지움

    # 모든 소수를 출력
    for i in range(2, n + 1):
        if arr[i]:
            answer_arr.append(i);
    answer = len(answer_arr);

    return answer;