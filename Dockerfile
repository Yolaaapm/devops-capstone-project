# Menggunakan image Python resmi yang ringan
FROM python:3.9-slim
# Menentukan direktori kerja di dalam kontainer
WORKDIR /app
# Menyalin file requirements terlebih dahulu untuk optimasi cache
COPY requirements.txt .
# Menginstal dependensi
RUN pip install --no-cache-dir -r requirements.txt
# Menyalin seluruh kode proyek ke dalam direktori kerja
COPY . .
# Menentukan port yang akan digunakan aplikasi
EXPOSE 8080
# Menjalankan aplikasi menggunakan Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "service:app"]
