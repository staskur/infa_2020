# сортировки
def insert_sort(A):
    """ сортировка списка А вставками """
    N = len(A)
    for verh in range(1,N):
        k=verh
        while k>0 and A[k-1] > A[k]:
            A[k],A[k-1] = A[k-1],A[k]
            k-=1


def choice_sort(A):
    """ сортировка списка А выбором """
    N=len(A)
    for poz in range(0,N-1):
        for k in range(poz+1, N):
            if A[k] < A[poz]:
                A[k], A[poz] = A[poz], A[k]

def bubble_sort(A):
    """ сортировка списка А пузырьком """
    N = len(A)
    for obhod in range(1,N):
        for k in range(0, N-obhod):
            if A[k] > A[k+1]:
                A[k],A[k+1] = A[k+1],A[k]

def test_sort(sort_algoritm):
    print("Тестируем :", sort_algoritm.__doc__)
    print("testcase #1: ", end="")
    A=[4,2,5,1,3]
    A_sorted= [1,2,3,4,5]
    sort_algoritm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10,20))+list(range(0,10))
    A_sorted = list(range(20))
    sort_algoritm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algoritm(A)
    print("Ok" if A == A_sorted else "Fail")

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
