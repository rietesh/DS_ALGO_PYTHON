def quick_sort(a, l ,r):
    if r-l <= 1:
        return ()

    p = l
    yellow = l+1
    for green in range(l+1, r):
        if a[green] <= a[p]:
            (a[yellow],a[green]) = (a[green], a[yellow])
            yellow += 1

    (a[p],a[yellow-1]) = (a[yellow-1], a[p])

    quick_sort(a, l, yellow-1)
    quick_sort(a, yellow, r)

    return a

print(quick_sort([9,8,7,6,5,4,3,2,1],0, 9))
