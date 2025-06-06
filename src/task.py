def rabin_karp_search(haystack, needle):
    if not needle or not haystack or len(needle) > len(haystack):
        return []

    p = 31
    m = 10**9 + 9
    n = len(haystack)
    k = len(needle)

    needle_hash = 0
    current_hash = 0
    p_pow = 1

    # p^(k-1)
    for _ in range(k - 1):
        p_pow = (p_pow * p) % m

    for i in range(k):
        needle_hash = (needle_hash * p + ord(needle[i])) % m
        current_hash = (current_hash * p + ord(haystack[i])) % m

    result = []
    for i in range(n - k + 1):
        if current_hash == needle_hash:
            if haystack[i : i + k] == needle:
                result.append(i)

        if i < n - k:
            left = ord(haystack[i]) * p_pow % m
            right = ord(haystack[i + k])
            current_hash = (current_hash - left + m) % m
            current_hash = (current_hash * p + right) % m
    return result
