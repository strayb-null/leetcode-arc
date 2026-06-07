# 1929. Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/
# Dificuldade: Easy
# Tempo: O(n) | Espaço: O(n)

def getConcatenation(nums: list[int]) -> list[int]:
    return nums + nums


if __name__ == "__main__":
    casos = [
        ([1, 2, 1],    [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
        ([],           []),
        ([5],          [5, 5]),
    ]

    for nums, esperado in casos:
        resultado = getConcatenation(nums)
        status = "✅" if resultado == esperado else "❌"
        print(f"{status} nums={nums} → {resultado}")