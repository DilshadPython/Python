# pip install python-barcode or direct in the computer without virtualenv
# pip install --break-system-packages barcode
# pip install --break-system-package pyzbar - DO NOT NEED IT HERE
# pip install --break-system-package pyzbar opencv-python DON NOT NEED IT HERE
# 13 is the length for European Article number ENA

from barcode import EAN13

enter_num = input("Enter the 12 digits number: ")
code = EAN13(enter_num)
code.save("thecode")
print(code)
