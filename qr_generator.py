import qrcode

def generate_qr(data, filename):
    # Cria o QR code
    qr = qrcode.QRCode(
        version=1,  # Controle do tamanho do QR Code, 1 é a menor versão
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Define a quantidade de correção de erros
        box_size=10,  # Tamanho de cada quadrado do QR Code
        border=4,  # Tamanho da borda do QR Code
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Cria a imagem do QR code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"Código QR salvo como {filename}")

if __name__ == "__main__":
    # Entrada do usuário
    data = input("Digite o texto ou URL para gerar o QR Code: ")
    filename = input("Digite o nome do arquivo de saída (ex: qr_code.png): ")
    generate_qr(data, filename)
