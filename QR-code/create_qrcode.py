import qrcode

qr_code = qrcode.QRCode(
    box_size = 25,
    border = 25,
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L
)

