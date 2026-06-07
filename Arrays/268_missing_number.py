# 268. Missing Number
# https://leetcode.com/problems/missing-number/
# Dificuldade: Easy
# Tempo: O(n) | Espaço: O(1)

def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    return (n * (n + 1) // 2) - sum(nums)


if __name__ == "__main__":
    casos = [
        ([0, 1, 3],        2),
        ([0, 1],           2),
        ([1, 2],           0),
        ([0, 2, 3],        1),
        ([1],              0),
        ([4, 2, 3, 0, 1],  5),
    ]

    for nums, esperado in casos:
        resultado = missingNumber(nums)
        status = "✅" if resultado == esperado else "❌"
        print(f"{status} nums={nums} → {resultado}")