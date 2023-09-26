

def save_data_matrix_to_pdf():
    from PIL import Image
    from pylibdmtx.pylibdmtx import encode

    encoded = encode('hello world'.encode('utf8'), size="24x24")
    img = Image.frombytes(
        'RGB', (encoded.width, encoded.height), encoded.pixels)  # .resize((500, 500))
    img.save('dmtx.png')

    return img


def add_image(in_pdf_file, out_pdf_file):

    from PyPDF2 import PdfWriter, PdfReader
    import io
    from reportlab.pdfgen import canvas

    save_data_matrix_to_pdf()
    img_file = 'dmtx.png'

    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    # can.drawString(10, 100, "Hello world")
    x_start = 0
    y_start = 0
    can.drawImage(img_file, x_start, y_start, width=60,
                  preserveAspectRatio=True, mask='auto')
    can.showPage()
    can.showPage()
    can.showPage()
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)

    new_pdf = PdfReader(packet)

    # read the existing PDF
    existing_pdf = PdfReader(open(in_pdf_file, "rb"))
    output = PdfWriter()

    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()
