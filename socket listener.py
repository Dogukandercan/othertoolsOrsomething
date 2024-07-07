import socket

hedef_port = 5656


soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


soket.bind(('0.0.0.0', hedef_port))


soket.listen(5)

print(f"Dinleme, {hedef_port} portunda başladı...")

while True:
   
    baglanti, istemci_adresi = soket.accept()
    print(f"{istemci_adresi} adresinden bağlantı kabul edildi.")

    while True:
    
        veri = baglanti.recv(1024)

        if not veri:
            break

        print(f" {veri.decode()}")

   
    baglanti.close()
