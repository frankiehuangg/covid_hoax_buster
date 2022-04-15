import string
from numpy import vectorize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

stopwords = "yang di dan itu dengan untuk tidak ini dari dalam akan pada juga saya ke karena tersebut bisa ada mereka lebih kata tahun sudah atau saat oleh menjadi orang ia telah adalah seperti sebagai bahwa dapat para harus namun kita dua satu masih hari hanya mengatakan kepada kami setelah melakukan lalu belum lain dia kalau terjadi banyak menurut  anda hingga tak baru beberapa ketika saja jalan sekitar secara dilakukan sementara tapi sangat hal sehingga  seorang bagi besar lagi selama antara waktu sebuah jika sampai jadi terhadap tiga serta pun salah merupakan atas sejak  membuat baik memiliki  kembali selain tetapi pertama kedua memang pernah apa mulai sama tentang bukan agar semua sedang kali kemudian hasil sejumlah juta persen sendiri katanya demikian masalah  mungkin umum setiap bulan bagian bila lainnya terus luar cukup termasuk sebelumnya bahkan wib tempat perlu menggunakan memberikan rabu sedangkan kamis langsung apakah pihak melalui diri mencapai  minggu aku  berada tinggi ingin sebelum tengah kini the tahu bersama depan selasa begitu  merasa  berbagai mengenai  maka jumlah masuk   katanya  mengalami sering ujar kondisi akibat hubungan empat paling mendapatkan selalu lima  meminta melihat sekarang mengaku mau kerja acara menyatakan masa proses tanpa selatan sempat  adanya hidup datang senin rasa maupun seluruh mantan lama jenis segera misalnya  mendapat bawah jangan meski terlihat akhirnya jumat  punya yakni terakhir kecil panjang badan juni of  jelas jauh tentu semakin tinggal kurang  mampu posisi  asal sekali  sesuai sebesar berat  dirinya memberi pagi  sabtu  ternyata mencari sumber ruang menunjukkan biasanya nama  sebanyak utara berlangsung barat kemungkinan yaitu  berdasarkan  sebenarnya cara utama pekan terlalu  membawa kebutuhan suatu menerima  penting  tanggal bagaimana terutama tingkat awal sedikit nanti pasti  muncul dekat lanjut ketiga biasa dulu kesempatan  ribu  akhir  membantu terkait  sebab menyebabkan khusus  bentuk ditemukan  diduga mana ya kegiatan sebagian tampil hampir bertemu usai berarti keluar pula digunakan justru  padahal menyebutkan  gedung  apalagi program  milik teman menjalani keputusan sumber a  upaya mengetahui mempunyai berjalan menjelaskan  b mengambil benar lewat belakang ikut barang meningkatkan kejadian kehidupan keterangan penggunaan masing-masing menghadapi vaksin"
stopwords = stopwords.split(' ')

def clean_string(text):
    text = ''.join([word for word in text if word not in string.punctuation])
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stopwords])

    return text

def cosine_sim_vectors(vec1, vec2):
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)

    return cosine_similarity(vec1, vec2)[0][0]

csv = open("files/Berita.txt", 'r').readlines()
csv = list(map(clean_string, csv))

title = input("Masukkan judul: ")
title = clean_string(title)

sim_value = 0

for hoaxes in csv:
    array = [title, hoaxes]

    vectorizer = CountVectorizer().fit_transform(array)
    vectors = vectorizer.toarray()
    
    cosine_sim = cosine_sim_vectors(vectors[0], vectors[1])

    sim_value = max(sim_value, cosine_sim)

print(sim_value)

if (sim_value == 0):
    print("Input tidak valid")
elif (sim_value > 0.5):
    print("Hoax")
elif (sim_value < 0.5 and sim_value > 0.2):
    print("Kemungkinan hoax")
else:
    print("Bukan hoax")