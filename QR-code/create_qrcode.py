import qrcode

qr_code = qrcode.QRCode(
    box_size = 45,
    border = 55,
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L
)
print(qr_code)
