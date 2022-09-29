import random

def get_random(ini, end):
    return random.randrange(ini, end + 1)


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0]
    stars = [0, 0]

    for a in range(1, 6):
        for x in range(len(nums)):
            while True:
                numero = get_random(1, 50)
                if numero not in nums:
                    nums[x] = numero
                    break
        for x in range(len(stars)):
            while True:
                numero = get_random(1, 12)
                if numero not in nums:
                    stars[x] = numero
                    break

        nums.sort(key=int)
        stars.sort(key=int)
        print(f'{a}º Numbers = {nums}')
        print(f'{a}º Stars = {stars}')

