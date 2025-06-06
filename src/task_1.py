def rabin_karp_search_multiple_with_flag(haystack, needles):
    if not haystack or not needles:
        return False

    p = 31
    m = 10**9 + 9
    n = len(haystack)

    needle_hashes = {}
    for needle in needles:
        k = len(needle)
        if k > n:
            continue

        needle_hash = 0
        for i in range(k):
            needle_hash = (needle_hash * p + ord(needle[i])) % m

        needle_hashes[needle] = (needle_hash, k)

    result = {needle: [] for needle in needle_hashes}

    for needle, (target_hash, k) in needle_hashes.items():
        if k > n:
            continue

        current_hash = 0
        p_pow = 1
        for _ in range(k - 1):
            p_pow = (p_pow * p) % m

        for i in range(k):
            current_hash = (current_hash * p + ord(haystack[i])) % m

        for i in range(n - k + 1):
            if current_hash == target_hash:
                if haystack[i : i + k] == needle:
                    result[needle].append(i)

            if i < n - k:
                left = ord(haystack[i]) * p_pow % m
                right = ord(haystack[i + k])
                current_hash = (current_hash - left + m) % m
                current_hash = (current_hash * p + right) % m

    found_any = any(positions for positions in result.values())

    if not found_any:
        return False

    return True, result

text = "цей текст містить погано і небезпечно"
banned_words = ["погано", "небезпечно", "заборонені"]

result = rabin_karp_search_multiple_with_flag(text, banned_words)

if result is False:
    print("Нічого не знайдено")
else:
    found_flag, matches = result
    print("Знайдено заборонені слова:")
    for word, positions in matches.items():
        if positions:
            print(f"- {word} на позиціях {positions}")