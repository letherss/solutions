def largest_anagram_group(words):
    groups = {}

    for word in words:
        key = ''.join(sorted(word))
        groups.setdefault(key, []).append(word)

    groups = [sorted(group) for group in groups.values() if len(group) > 1]

    if not groups:
        return []

    return min(groups, key=lambda group: (-len(group), group))

if __name__ == "__main__":
    print(largest_anagram_group(["listen", "silent", "enlist", "hello", "world"]))
    # ['enlist', 'listen', 'silent']

    print(largest_anagram_group(["cat", "dog", "bird"]))
    # []

    print(largest_anagram_group(["tea", "eat", "ate", "tan", "nat"]))
    # ['ate', 'eat', 'tea']