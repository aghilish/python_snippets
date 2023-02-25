import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_merger(pfd_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pfd_list:
        merger.append(pdf)

    merger.write('super.pdf')


pdf_merger(inputs)
