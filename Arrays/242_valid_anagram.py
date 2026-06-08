# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Dificuldade: Easy
# Solução 1 — Sorted:  O(n log n) tempo | O(n) espaço
# Solução 2 — Count:   O(n) tempo       | O(1) espaço

def isAnagramSorted(s: str, t: str) -> bool:
    """Abordagem usando ordenação - O(n log n) tempo, O(n) espaço"""
    return sorted(s) == sorted(t)


def isAnagramCount(s: str, t: str) -> bool:
    """Abordagem usando array de contagem - O(n) tempo, O(1) espaço"""
    if len(s) != len(t):
        return False

    count = [0] * 26

    for i in range(len(s)):
        count[ord(s[i]) - ord("a")] += 1
        count[ord(t[i]) - ord("a")] -= 1

    return all(c == 0 for c in count)


if __name__ == "__main__":
    casos = [
        (("anagram", "nagaram"), True),
        (("rat", "car"),         False),
        (("", ""),               True),
        (("a", "a"),             True),
        (("ab", "ba"),           True),
        (("abc", "abcd"),        False),
        (("listen", "silent"),   True),
        (("hello", "world"),     False),
        (("aab", "bba"),         False),
        (("aaaa", "aaaa"),       True),
    ]

    print("=" * 50)
    print("Testando abordagem com SORTED")
    print("=" * 50)
    for (s, t), esperado in casos:
        resultado = isAnagramSorted(s, t)
        status = "✅" if resultado == esperado else "❌"
        print(f"{status} s='{s}', t='{t}' → {resultado}")


    print("\n" + "=" * 50)
    print("Testando abordagem com COUNT (Array[26])")
    print("=" * 50)
    for (s, t), esperado in casos:
        resultado = isAnagramCount(s, t)
        status = "✅" if resultado == esperado else "❌"
        print(f"{status} s='{s}', t='{t}' → {resultado}")