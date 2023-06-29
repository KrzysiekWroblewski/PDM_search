from fpdf import FPDF
from gui import GUI
import datetime


page_width = 210
page_height = 297
font_size = 12


class Report:

    @staticmethod
    def generate_report_txt(list_of_records: list, name_of_file: str, search_Path_sld_prt: bytes, search_Path_sld_prt_revision: bytes, indexes_to_report: list[int]):

        print(list_of_records)

        GUI.Mbox("Wyszukiwarka PDM via CSV",
                 "Wybierz folder gdzie zapisać raport braków", 1)

        date_stamp = datetime.datetime.now()
        date_stamp = date_stamp.strftime("%Y-%B-%d %H_%M")
        file = ((GUI.select_folder()) + "/" + date_stamp +
                "_" + name_of_file + "_report.txt")

        with open(file, 'w', encoding="utf-8") as f:
            f.write(date_stamp + "\t" + file)
            f.write("\n\n")

            i = 1

            for row in list_of_records:
                string = "{}. ".format(i)
                for index in indexes_to_report:
                    string += row[index].decode("utf-8") + "\t"

                """if string[-1] == "_":
                    string = string[:-3]
                """

                i += 1

                f.write(string)
                f.write("\n")

            f.write("\n")
            f.write("Ścieżka wyszukiwania:")
            f.write("\n")
            f.write(search_Path_sld_prt.decode("utf-8"))
            f.write("\n")
            f.write("\n")
            f.write("Ścieżka wyszukiwania z rewizją:")
            f.write("\n")
            f.write(search_Path_sld_prt_revision.decode("utf-8"))
            f.write("\n")
