def selection_sort(s):
    for i in range(len(s)):
        m=i
        for j in range(i, len(s)):
            if s[j] < s[i]:
                m = j
                
        print(i,m,s[m])
        (s[i],s[m]) = (s[m], s[i])

    return s

print(selection_sort([9,8,7,6,5,4,3,2,1]))


def insertion_sort(s):
    for i in range(len(s)):
        end = i
        while end > 0 and s[end] < s[end-1]:
            (s[end], s[end-1]) = (s[end-1],s[end])
            end -= 1

    return s

print(insertion_sort([9,8,7,6,5,4,3,2,1]))
