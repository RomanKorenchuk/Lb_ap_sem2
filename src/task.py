def merge_sort_desc(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_desc(arr[:mid])
    right = merge_sort_desc(arr[mid:])
    
    return merge_desc(left, right)

def merge_desc(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

def min_total_price(prices, discount):
    prices = merge_sort_desc(prices)  # Використання merge sort
    total = 0
    l_max = len(prices) // 3
    for i, price in enumerate(prices):
        if i < l_max:
            total += price * (1 - discount / 100)
        else:
            total += price
    
    return format(total, ".2f")
