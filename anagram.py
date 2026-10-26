def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = [0] * 26

    for ch in s1:
        freq[ord(ch) - ord('a')] += 1

    for ch in s2:
        freq[ord(ch) - ord('a')] -= 1

    return all(count == 0 for count in freq)

if __name__ == "__main__":
    is_anagram("heart", "earth")
    is_anagram("python", "typhon")
    is_anagram("hello", "world")
    is_anagram("ab", "abc")
