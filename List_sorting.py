class Sort:

    # Bubble sort list of lists based on second index
    @staticmethod
    def list_sort_by_index(list, index):

        sorted_list = list.copy()
        list_len = len(sorted_list)

        for i in range(list_len):
            for j in range(list_len-1):
                if sorted_list[j][index] > sorted_list[j+1][index]:
                    sorted_list[j], sorted_list[j +
                                                1] = sorted_list[j+1], sorted_list[j]

        return sorted_list
