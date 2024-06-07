"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    hour=int(input("시간을 입력하세요: "))
    if 0 <= hour <= 23:
        if hour < 12:
            print('오전')
        else:
            print('오후')
    else:
        print('잘못된 입력입니다.')
    return


if __name__ == '__main__':
    main()
