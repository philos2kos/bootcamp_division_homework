"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    num = int(input())
    if 0 < num <= 12:
        total = 0
        factorial = 1
        
        for i in range(1, num + 1):
            total += i

        for i in range(1, num + 1):
            factorial *= i


        print(f'{total}: 1부터 {num}까지의 합')
        print(f'{factorial}: {num}!')
        print(total)
        print(factorial)
    else:
        print("잘못된 입력입니다. 1부터 12 사이의 값을 입력하세요.")

    return


if __name__ == '__main__':
    main()
