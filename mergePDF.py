# PyPDF2

from PyPDF2 import PdfFileReader , PdfFileMerger

p1 = input("Enter the path of pdf1 ")
p2 = input("Enter the path of pdf2 ")

pdf1 = PdfFileReader('p1')
pdf2 = PdfFileReader('p2')

out = PdfFileMerger()

out.append(pdf1)
out.append(pdf2)
out.write('merged.pdf')