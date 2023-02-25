from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
import sys

inputs = sys.argv[1:]

watermark = 'wtr.pdf'


def pdf_wtr(pfd_list):
    writer = PdfFileWriter()
    watermark_pdf = PdfFileReader(watermark)
    watermark_page = watermark_pdf.getPage(0)
    for file in pfd_list:
        pdf = PdfFileReader(file)
        for i in range(pdf.getNumPages()):
            pdf_page = pdf.getPage(i)
            pdf_page.mergePage(watermark_page)
            writer.addPage(pdf_page)

    with open('watermarked.pdf', "wb") as merged_file:
        writer.write(merged_file)


pdf_wtr(inputs)
