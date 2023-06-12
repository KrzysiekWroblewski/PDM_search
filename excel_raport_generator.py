from fpdf import FPDF


page_width = 210
page_height = 297
font_size = 12


def Generate_Targets(list_of_records):

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

    for row in list_of_records:
        pdf.set_xy(x, y)
        i = 1
        string = "{}. ".format(i)
        for object in row:
            string += str(object) + "-"

        if string[-1] == "-":
            string = string[:-1]
        print(string)

        pdf.generate_record(str(string))
        y = y + font_size+1
        i = i+1

    pdf.output(str("Random_target_" + ".pdf"))
