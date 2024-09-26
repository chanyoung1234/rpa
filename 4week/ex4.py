num = int(input("1 이상의 정수를 입력하시오: "))

if num > 0:
    total = 0
    for i in range(1, num + 1):
        total += i
    print(f"1부터 {num}까지의 합은 {total}입니다.")
else:
    print("1 이상의 정수를 입력하시오.")
