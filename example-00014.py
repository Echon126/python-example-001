from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser
from PyPDF2 import PdfFileReader


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

        print(pdf.getFormTextFields().get())
        print(number_of_pages)

    print(f.name)



def parse(path, save_name):
    parser = PDFParser(path)
    document = PDFDocument(parser)

    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparms = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparms=laparms)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open('%s' % (save_name), 'a') as f:
                        results = x.get_text().encode('utf-8')
                        f.write(results + "\n")


if __name__ == '__main__':
    # path = open(r'C:\Users\ZKTT\Desktop\example-001\test.pdf')
    # parse(path, 'test.txt')
    extract_information(r'C:\Users\ZKTT\Desktop\example-001\test.pdf')
