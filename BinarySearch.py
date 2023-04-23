def binarysearch(List_of_items):
    low = 0
    high = len(v) - 1

    try:
        To_find = int(input("Enter the value to search\n"))

        while high - low > 1:

            mid = (high + low) //2

            if List_of_items[mid] < To_find:
                low = mid + 1
            else:
                high = mid

        if List_of_items[low] == To_find:
            print("Found at index:", low)
            binarysearch(v)

        elif List_of_items[high] == To_find:
            print("Found at index:", high)
            binarysearch(v)
        else:
            print("Not found")
            binarysearch(v)

    except ValueError:
        print("Input error.\nTry again...")
        binarysearch(v)

v= [1,2,3,4,5,6,]
binarysearch(v)  