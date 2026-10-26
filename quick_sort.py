def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    n = arr[len(arr) // 2]

    lt = []
    md = []
    rt = []

    for x in arr:
        if x < n: lt.append(x)
        if x == n: md.append(x)
        if x > n: rt.append(x)
    return quick_sort(lt) + md + quick_sort(rt)

if __name__ == "__main__":
    quick_sort([4, 2, 7, 1, 3, 5])
    quick_sort([7, 3, 3, 4, 1])
    quick_sort([])