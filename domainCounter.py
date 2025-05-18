# Meminta input nama file
txtFile = input("Masukkan nama file: ")

# Mencoba membuka file
try:
    fhandle = open(txtFile)
except:
    print("File tidak dapat dibuka:", txtFile)
    quit()

# Membuat dictionary baru
domain_counter = dict()

# Membaca setiap baris dalam file
for line in fhandle:
    if line.startswith('From '):
        kata = line.split()
        email = kata[1]  # Ambil alamat email, misalnya: 'cwen@iupui.edu'
        domain = email.split('@')[1]  # Ambil domain
        domain_counter[domain] = domain_counter.get(domain, 0) + 1

print(domain_counter)
