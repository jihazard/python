def bubbleSort(list):
    #temp = 0
    for x in range(0, len(list)):
        for y in range(0,len(list)-1-x):
            if list[y] > list[y+1]:
                # temp = list[y]
                # list[y] = list[y+1]
                # list[y+1] = temp 
                list[y], list[y+1] = list[y+1], list[y]
    return list


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    a = arr[:int(len(arr)/2)]
    b = arr[int(len(arr)/2):]

    a = mergeSort(a)
    b = mergeSort(b)

    c=[]
    i=0 
    j=0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    c += a[i:]
    print("a" , a[i:])
    c += b[j:]
    print("b" , b[j:])
    
    return c

def main():
    list = [5, 8, 3, 6, 9, 4, 7, 2, 1]
    print(bubbleSort(list))
    print(sorted(list))
    print(sorted(list, reverse=True))
    print(mergeSort(list))



if __name__ == "__main__":
    main()