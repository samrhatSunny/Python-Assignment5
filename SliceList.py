n1 =[]
n2 =[]
def slice_num():
    lst_num = [1,2,3,4,5,6,7,8,9,10]
    global n1,n2
    n1 = lst_num[:5:1]
    n2 = n1[::-1]

def print_slice_num():
    print("Extracted List:",n1)
    print("Reverse List:",n2)
