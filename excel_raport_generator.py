from fpdf import FPDF
from gui import GUI
import datetime


page_width = 210
page_height = 297
font_size = 12


class Report:

    @staticmethod
    def generate_report_PDF(list_of_records):

        class PDF(FPDF):
            def generate_record(self, add_record):
                self.set_font("Times", "", size=font_size)
                self.set_text_color(0, 0, 0)
                self.cell(w=100, txt=add_record,
                          border=False, ln=0, align="L")

        pdf = PDF('P', 'mm', (page_width, page_height))
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        x = 10
        y = 10
        string = ""
        for row in list_of_records:
            pdf.set_xy(x, y)
            i = 1
            string = "{}. ".format(i).encode("utf-8")
            for object in row:
                object = str(object).encode("utf-8")

                string += object + "___".encode("utf-8")

            string = string.decode("cp1252")
            if string[-1] == "_":
                string = string[:-3]

            print(string)

            pdf.generate_record(string)
            y = y + (font_size/2.4) + 1
            i = + 1

        # generate raport in selected folder
        pdf.output(name=str(GUI.select_folder()) + "/raport.pdf", dest="")

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
