"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    a =int(input())
    if 100<=a<=999:
        reversed_a=str(a)[::-1]
        print(reversed_a)
    else:
        print('세 자리 정수를 입력하세요')

    return


if __name__ == '__main__':
    main()
