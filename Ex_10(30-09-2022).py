

if __name__ == '__main__':
    num = int(input('Digite um numeriro: '))

    nums = []
    for x in range(1, num + 1):
        nums.append(x)

    a = int(len(nums))
    total = 1
    for x in range(len(nums)):
        total *= nums[a - 1]
        a -= 1

    print(f'{nums}')
    print(f'{total}')
