def merge(A,B):
    c = []
    (m,n) = (len(A), len(B))
    (i,j) = (0,0)
    b = True

    while i+j < m+n:
        if i == m:
            c.append(B[j])
            j+=1
        elif j == n:
            c.append(A[i])
            i+=1
        elif A[i] <= B[j]:
            c.append(A[i])
            i+=1
        elif B[j] < A[i]:
            c.append(B[j])
            j+=1

    return c

def merge_sort(a, left, right):
    if right-left <= 1:
        return a[left:right]
    if right-left > 1:
        m = (left+right)//2
        L = merge_sort(a, left, m)
        R = merge_sort(a, m, right)
        return merge(L,R)


a = [9,8,7,6,5,4,3,2,1]
print(merge_sort(a, 0, len(a)))
# print(merge([2,4,6],[1,3,5]))
