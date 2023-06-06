import csv
import pyperclip


def open_file_encoding(open_file, csv_encode, result, csv_delimiter, csv_sep, part_column):

    with open(open_file, encoding=csv_encode, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=str(csv_delimiter))

        search_Path = ""
        number_of_files_merged = 0

        for line in csv_reader:

            # rows, should not have empty spaces, function delate them??
            """for word in range(0, len(line)):
                line[word] = line[word].replace(' ', '')
            """

            # prevents from index error if row is empty
            if line == []:
                continue

            # Skip parts with tag: "H", "Handlowe"
            if line[10] == "H":
                continue
            if line[10] == "Handlowe":
                continue

            # merged search path for files with revisions
            elif result[0] == "Files with revision: PDF, DXF, STP":
                search_Path = search_Path + \
                    str(line[part_column]) + "-" + \
                    str(line[part_column+1]) + str(csv_sep)

            # merged search path for files without revisions (.sldprt, .sldasm)
            elif result[0] == "Solid Works Files":
                search_Path = search_Path + \
                    str(line[part_column]) + str(csv_sep)

            number_of_files_merged = number_of_files_merged + 1

        if search_Path[-1] == "|":
            search_Path = search_Path[:-1]

    pyperclip.copy(search_Path)

    return (number_of_files_merged, search_Path)
