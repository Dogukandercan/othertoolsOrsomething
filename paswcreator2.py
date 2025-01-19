min_deger = 1
max_deger = 10
word = "example"
punctuation = "!"


file_name = "passwords.txt"

w = min_deger
with open(file_name, 'w') as file:
    while w < max_deger:
        line = str(w) + word + punctuation + "\n"
        file.write(line)
        w += 1

print(f"Oluşturulan şifreler '{file_name}' dosyasına kaydedildi.")
