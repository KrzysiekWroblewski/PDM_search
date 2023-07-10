from fpdf import FPDF
from gui import GUI
import datetime


class Report:

    @staticmethod
    def date_stamp() -> str:
        date_stamp = datetime.datetime.now()
        date_stamp = date_stamp.strftime("%Y-%B-%d %H_%M")
        return date_stamp

    @staticmethod
    def Report_list_to_txt(title_message: str, file, list_of_excels_to_report, list_of_excels_with_missing_orders, date_stamp, indexes_to_report, list_search_Path_sld_prt, list_search_Path_sld_prt_revision):

        with open(file, 'w', encoding="utf-8") as f:
            f.write(title_message)
            f.write("\t")
            f.write(date_stamp)
            f.write("\n")
            f.write("\n")
            f.write("\n")

            i = 0
            for list in list_of_excels_with_missing_orders:

                f.write(list_of_excels_to_report[i])
                f.write("\n\n")
                j = 0

                for row in list:
                    string = "{}. ".format(j+1)
                    for index in indexes_to_report:
                        string += row[index] + "\t"

                    f.write(string)
                    f.write("\n")
                    j += 1

                f.write("\n")
                f.write("Ścieżka wyszukiwania:")
                f.write("\n")
                f.write(list_search_Path_sld_prt[i])
                f.write("\n")
                f.write("\n")
                f.write("Ścieżka wyszukiwania z rewizją:")
                f.write("\n")
                f.write(
                    list_search_Path_sld_prt_revision[i])
                f.write("\n")
                f.write("\n")
                f.write("\n")
                f.write("\n")
                f.write(
                    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                f.write("\n")
                f.write("\n")
                i += 1
