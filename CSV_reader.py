import csv
import pyperclip
from gui import GUI


class CSV:

    @staticmethod
    def read_BOM_from_CSV(result, csv_delimiter, csv_sep, part_column):

        open_file = GUI.select_file()
        decoding_list = ["latin-1", "utf-16-le", "utf-8"]
        i = 0
        decoded = False
        for decode in decoding_list:
            try:
                csv_encode = decoding_list[i]
                # merging text function
                merged_text = CSV.results_from_CSV(open_file, csv_encode, result,
                                                   csv_delimiter, csv_sep, part_column)
                decoded = True
                break
            except:
                print("Decoding", decoding_list[i], "do not work")
                i = i + 1

        if decoded != True:
            GUI.Mbox("Wyszukiwarka plikow PDM",
                     "Błędna operacja lub błędny wybór kolumny numeru części", 1)

        Message_01 = str("Sciezke wyszukiwania skopiowano do schowka: " + "\n" + "\n" + "Source file path: " + str(open_file) +
                         str("\n") + str("\n") + "Number of files: " + str(merged_text[0]))

        print(Message_01)
        GUI.Mbox("Wyszukiwarka PDM via CSV", Message_01, 1)

    @staticmethod
    def results_from_CSV(open_file, csv_encode, result, csv_delimiter, csv_sep, part_column):

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
                try:
                    if "lustro" in line[part_column].lower():
                        continue
                except:

                    if "lustro" in line[part_column].lower():
                        continue
                # merged search path for files with revisions
                if result[0] == "Files with revision: PDF, DXF, STP":
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
