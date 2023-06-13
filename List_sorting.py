list = [['Rash', 4, 28], ['Varsha', 2, 20],
        ['Nikhil', 1, 20], ['Akshat', 3, 21]]


def list_sort_by_colum(list):

    # bubble sort list of lists based on second index
    sorted_list = list.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(n-1):
            if sorted_list[j][1] > sorted_list[j+1][1]:
                sorted_list[j], sorted_list[j +
                                            1] = sorted_list[j+1], sorted_list[j]
    return sorted_list
