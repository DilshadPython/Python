# This Module is required to import
# pip install tuabla-py
import  tabula

# read the pdf file
pdf = tabula.read_pdf("API_Status.pdf", pages='all')[0]
tabula.convert_into("API_Status.pdf", "api_stat.csv", output_format="csv", pages='all')
print(pdf)