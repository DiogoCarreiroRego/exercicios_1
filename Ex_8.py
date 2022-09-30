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

        # Exemplo com 'sort' para ordenar o que tem na lista
        #nums.sort(key=int)
        #stars.sort(key=int)

        # Não funcionado
        """
        troquei = True
        nums_or = [0, 0, 0, 0, 0]
        while troquei:
            troquei = False
            for x in range(4):
                if nums[x] > nums[x + 1]:
                    troquei = True
        """


        print(f'{a}º Numbers = {nums}')
        #print(f'{a}º Stars = {stars}')

