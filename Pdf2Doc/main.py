# Import Libraries
import _tkinter

from pdf2docx import parse
from typing import Tuple


def pdf_convert_doc(inputf: str, outputf: str, page: Tuple=None):
	if pages:
		pages = [int(x) for x in list(pages) if x.isnumeric()]
	result = parse(pdf=input, doc_pth=output, pages=pages)

	summery = {
		'file': input,
		'doc': output,
		'pages': str(pages)
	}

	# Printing Summary
	print("## Summary ########################################################")
	print("\n".join("{}:{}".format(x, y) for x, y in summary.items()))
	print("###################################################################")
	return result


if __name__ == "__main__":
    import sys
    inputf = sys.argv[1]
    outputf = sys.argv[2]
    pdf_convert_doc(inputf, outputf)