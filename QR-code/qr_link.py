import qrcode

qr_code = qrcode.QRCode(
    box_size = 25,
    border = 25,
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L
)

mylink = "https://github.com/DilshadGit/reactjs/"
qr_code.add_data(mylink)
qr_code.make(fit=True)
pic = qr_code.make_image(fill="black", back_color="white")
pic.save("link_git_qr.png")