# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Dificuldade: Easy
# Tempo: O(n) | Espaço: O(n)

def containsDuplicate(nums: list[int]) -> bool:
    vistos = set()

    for num in nums:
        if num in vistos:
            return True
        vistos.add(num)

    return False


if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))        # True  - tem o 1 duplicado
    print(containsDuplicate([1, 2, 3, 4]))        # False - sem duplicatas
    print(containsDuplicate([1, 1, 1, 3, 3, 4]))  # True  - vários duplicados