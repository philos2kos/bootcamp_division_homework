"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    score=int(input())
    if 90 <= score <=100:
        print('A')
    elif 80 <= score <90:
        print('B')
    elif 70 <= score <80:
        print('C')
    elif 60 <= score <70:
        print('D')
    else:
        print('F')

    return


if __name__ == '__main__':
    main()
