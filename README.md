Nama    : Sabrina Atha Shania

NPM     : 2206829591

Kelas   : PBP A

------------------------------------------------ TUGAS 5 ------------------------------------------------
1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
    Elemen selector terdiri dari 3 jenis, Element selector, Id selector, dan Class selector yang memiliki manfaat tersendiri, diantaranya sebagai berikut.
    
    - Element Selector, dapat digunakan ketika ingin mengubah properti untuk semua elemen yang memiliki tag HTML yang sama. Manfaatnya yaitu:
        1. Dapat mengatur gaya elemen-elemen tertentu secara konsisten di seluruh situs web. Sebagai contoh, Dapat mengubah ukuran font untuk semua judul p di seluruh situs web dengan menggunakan p selector
        2. Dapat menghindari pengulangan kode CSS yang tidak perlu. Hal ini bermanfaat untuk membuat perubahan global dengan lebih mudah.
        3. Dapat memiliki fleksibilitas untuk mengubah tampilan elemen-elemen dan menyesuaikan properti CSS seperti warna, ukuran, padding, dan margin.

    - Id Selector, dapat digunakan ketika ingin mengubah properti untuk semua elemen yang menggunakan ID pada tag sebagai selector-nya. ID bersifat unik dalam satu halaman web. ID dapat ditambahkan pada halaman template HTML. Manfaatnya yaitu:
        1. Dapat memiliki tingkat selektivitas yang sangat tinggi dalam hierarki CSS. Ini berarti, aturan CSS pada Id akan memiliki prioritas lebih tinggi dibandingkan dengan selector lainnya, seperti class selector atau element selector.
        2. Dapat lebih mudah dipahami karena aturan CSS tersebut berlaku secara khusus untuk elemen dengan ID tertentu. Ini dapat membantu dalam pemeliharaan dan debugging kode CSS.
        3. Dapat memiliki kinerja yang Lebih Baik karena mudah menemukan elemen dengan ID harus unik di seluruh halaman. Ini dapat meningkatkan kinerja ketika merender halaman web yang lebih besar.

    - Class Selector, dapat digunakan ketika ingin mengubah properti untuk mengelompokkan elemen dengan karakteristik yang sama. Manfaatnya yaitu:
        1. Dapat mengelompokkan elemen-elemen yang memiliki kesamaan dalam hal tampilan atau fungsi dengan memberikan class yang sama kepada beberapa elemen HTML yang berbeda, dan kemudian menerapkan gaya yang sama pada semua elemen tersebut dengan mudah.
        2. Dapat lebih mudah dipelihara karena dapat dengan jelas melihat bahwa class tersebut digunakan untuk menggambarkan gaya atau fungsi tertentu dalam halaman web.
        3. Dapat memiliki selektivitas yang Lebih Terkontrol. Selector class memiliki tingkat selektivitas yang lebih rendah dibandingkan dengan selector ID. Ini memberikan fleksibilitas dan kendali yang baik dalam mengatur tampilan elemen-elemen.

==================================================================================

2. Jelaskan HTML5 Tag yang kamu ketahui.
    HTML5 (Hypertext Markup Language 5) adalah versi terbaru dari standar HTML yang digunakan untuk membuat dan mengatur konten web. HTML5 memiliki banyak tag atau elemen yang memungkinkan pengembang web untuk menggambarkan konten dan struktur halaman web secara lebih baik. HTML5 juga memiliki beberapa perbedaan yang dapat menjadi keunggulan dibandingkan HTML, diantaranya sebagai berikut.
    - Mendukung audio dan video melalui tag video ataupun audio
    - Menambahkan elemen-elemen semantik seperti header, nav, article, dan section sehingga struktur dokumen lebih jelas
    - Mengizinkan Javascript berjalan di background karena penggunaan API
    - Grafik vektor merupakan tag seperti svg dan canvas untuk menggantikan ketergantungan pada gambar bitmap
    - Memperkenalkan elemen-elemen input yang lebih kaya seperti input type="email dan input type="date, yang memudahkan validasi data
    - Memiliki aksesibilitas yang lebih baik
    - Memiliki fitur yang mendukung responsivitas dan desain dapat menyesuaikan dengan berbagai perangkat dan ukuran layar
    - Memiliki penyimpanan lokal, sehingg dapat meningkatkan kinerja aplikasi web dengan mengurangi permintaan ke server.

==================================================================================

3. Jelaskan perbedaan antara margin dan padding.
    Margin dan padding adalah dua properti penting dalam CSS yang digunakan untuk mengatur tata letak elemen HTML pada halaman web. Mereka memiliki fungsi yang berbeda dan memengaruhi cara elemen-elemen berinteraksi dengan elemen-elemen sekitarnya dalam halaman. Margin memiliki fungsi untuk mengosongkan area di sekitar border (transparan). Padding memiliki fungsi untuk mengosongkan area di sekitar konten (transparan). Perbedaan diantara keduanya diantaranya sebagai berikut.
    - Margin adalah ruang yang ada di sekitar elemen HTML, sedangkan padding adalah ruang yang ada di sekitar konten elemen HTML
    - Margin memiliki latar belakang kosong dan biasanya tidak berwarna, sedangkan padding tidak memiliki latar belakang atau warna
    - Margin dapat memengaruhi tata letak elemen-elemen di sekitarnya, sehingga dapat memengaruhi jarak antara elemen tersebut dan elemen-elemen lainnya di sekitarnya. Sedangkan  Padding tidak berdampak pada elemen-elemen luar
    - Margin sering digunakan untuk mengontrol jarak antara elemen-elemen dengan menggunakan margin untuk memberikan jarak vertikal atau horizontal antara elemen-elemen. Sedagkan padding memengaruhi ukuran konten dalam elemen, sehingga ukuran elemen tersebut akan menjadi lebih besar
   
==================================================================================
4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
    Tailwind CSS dan Bootstrap adalah dua framework CSS yang digunakan untuk mempercepat pengembangan tampilan web. Mereka memiliki pendekatan yang berbeda dalam cara mereka memungkinkan pengembang untuk merancang dan menggaya halaman web. Berikut adalah perbedaan antara keduanya.

    - Pendekatan Styling
    Tailwind adalah framework CSS yang berfokus pada penggunaan kelas utility, di mana dapat menggabungkan kelas-kelas yang ada dalam HTML untuk mengatur gaya elemen. 
    Bootstrap adalah framework CSS yang berfokus pada penggunaan gaya pre-didesain dengan kelas-kelas yang telah ditentukan dengan memilih komponen-komponen yang telah dibuat sebelumnya dan mengatur elemen dengan cara menggunakan kelas Bootstrap yang sesuai.

    - Ukuran berkas
    Tailwind cenderung menghasilkan ukuran berkas CSS yang lebih besar karena menyediakan banyak kelas utility yang dapat digunakan. Semakin banyak kelas, maka semakin besar ukuran berkas CSS.
    Bootstrap memiliki ukuran berkas CSS yang cukup besar dibandingkan tailwind arena menyediakan banyak gaya dan komponen yang sudah siap pakai.

    - Kustomisasi
    Tailwind sangat fleksibel dalam hal kustomisasi karena dapat mengkustomisasi tampilan dengan mengedit konfigurasi dan mengubah atau menambahkan kelas utility sesuai kebutuhan.
    Bootstrap juga dapat disesuaikan, tetapi tidak sefleksibel seperti Tailwind. Bootstap perlu melakukan lebih banyak pekerjaan kustomisasi melalui penyesuaian CSS atau menghapus komponen yang tidak diperlukan.

    - Kekurangan waktu pengembangan
    Tailwind mungkin memerlukan lebih banyak waktu dalam proses pengembangan awal karena harus merancang tampilan dari awal dengan menggabungkan kelas utility.
    Bootstrap memungkinkan pengembangan yang lebih cepat karena dapat menggunakan komponen yang sudah ada dan hanya melakukan penyesuaian minor.

    Tailwind dan Bootstrap memiliki waktu penggunaan yang berbeda menyesuaikan kebutuhan. Berikut detailnya.
    - Apabila membutuhkan solusi cepat dan tidak ingin terlalu banyak berurusan dengan styling kustom, maka gunakan Bootstrap
    - Apabila memiliki desain yang sangat kustom dan ingin lebih banyak kontrol atas gaya elemen, maka gunakan Tailwind karena lebih fleksibel
    - Apabila ingin mengoptimalkan performa halaman web dengan ukuran berkas CSS yang lebih kecil, Tailwind mungkin lebih unggul karena Anda hanya akan menggunakan kelas yang diperlukan
    - Bootstrap memiliki dokumentasi yang kuat dan banyak contoh yang mudah diikuti, sehingga cocok untuk pengembang yang baru memulai
    - Tailwind membutuhkan disiplin dalam penggunaannya karena perlu menggabungkan kelas utility dengan benar dan menghindari pengulangan kode yang tidak perlu

==================================================================================
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Kustomisasi halaman login, register, dan tambah inventori
        - Melakukan kostumisasi halaman login, dilanjutka dengan halaman register, dan halaman tambah inventori
        - Menggunakan framework yang tersedia dan sumber source code lainnya yang dapat diakses online
        - Melakukan perubahan terhadap code dari framework maupun dari sumber lain menyesuaikan dengan keinginan dan kreativitas saya
        - Memastikan bahwa kode tersebut dapat berjalan sebagai mestinya, termasuk button dan lain lain
    
    2. Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card
        - Menggunakan framework yang tersedia dan sumber source code lainnya yang dapat diakses online
        - Melakukan kostumisasi dan perubahan menyesuaikan dengan kebutuhan dan keinginan bentuk web
        - Memastikan bahwa kode tersebut dapat berjalan sebagai mestinya, termasuk button dan lain lain
    
    3. Menjawab pertanyaan di dalam file README.md
    4. Melakukan git workflow (add, commit, push)
==================================================================================
------------------------------------------------ TUGAS 4 ------------------------------------------------
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
    UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna baru dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal. 
    Untuk menggunakan UserCreationForm, kita perlu mengimpornya dari Django.contrib.auth.forms.

    Kelebihan :
    - Mudah digunakan dalam pembuatan formulir pendaftaran pengguna baru
    - Diatur untuk berinteraksi langsung dengan model User yang ada di Django (integrasi dengan model), jadi tidak perlu merancang kembali model pengguna atau database yang terkait dengannya
    - Mencakup validasi bawaan untuk memastikan bahwa username unik, password aman, dan pengguna telah mengonfirmasi kata sandi dengan benar
    - Mudah menyesuaikan tampilan dan perilaku formulir ini sesuai dengan kebutuhan Anda

    Kekurangan :
    - Tidak menyediakan template desain, sehingga mungkin perlu merancang formulir kustom dari awal
    - Fitur tambahan terbatas, sehingga apabila memerlukan fitur tambahan seperti pengumpulan profil pengguna yang lebih kaya, mungkin perlu menambahkan formulir tambahan atau membuat formulir kustom
    - Bahasa bawaan pada field dalam UserCreationForm sudah ditentukan oleh Django, jadi jika ingin menggunakan nama field yang berbeda, perlu menyesuaikan model User dan formulirnya

==================================================================================

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    Autentikasi adalah proses verifikasi identitas pengguna dengan menentukan apakah pengguna yang mencoba mengakses aplikasi adalah pengguna yang mereka klaim. Sistem autentikasi memeriksa apakah informasi yang diberikan cocok dengan yang ada di database pengguna. Apabila cocok, pengguna dianggap berhasil melakukan autentikasi. Django menyediakan sistem autentikasi bawaan yang dapat digunakan untuk mengelola autentikasi pengguna dengan mudah, termasuk penggunaan model User.

    Otorisasi adalah proses yang menentukan izin apa yang dimiliki oleh pengguna dengan mengatur apa yang diizinkan atau tidak diizinkan oleh pengguna tersebut. Sistem otorisasi ini dilakukan setelah proses autentikasi selesai. Sistem otorisasi akan menentukan apakah pengguna tersebut memiliki izin untuk melakukan tindakan tertentu, seperti mengedit profilnya sendiri atau mengakses halaman tertentu dalam aplikasi. Django memiliki sistem otorisasi yang berbasis pada penggunaan decorator (misalnya @login_required) dan mixin yang memungkinkan untuk mengontrol izin akses ke tampilan dan fungsi aplikasi.

    Berikut poin poin dari autentikasi dan otorisasi:
    1. Autentikasi memastikan bahwa pengguna hanya bisa mengakses akun mereka sendiri, sedangkan otorisasi membatasi tindakan apa yang dapat dilakukan oleh pengguna yang sudah diautentikasi 
    2. Autentikasi memungkinkan aplikasi mengenali pengguna, yang dapat mengarah pada pengalaman pengguna yang lebih personal dan disesuaikan, sementara otorisasi memastikan bahwa pengguna hanya dapat melihat dan mengakses bagian aplikasi yang relevan.

    Alasan keduanya penting yaitu:
    1. Membantu melindungi data sensitif dan mencegah akses yang tidak sah
    2. Sebagai persyaratan hukum dan etika yang memastikan bahwa hanya pengguna yang berwenang yang dapat mengakses dan mengubah data tertentu
    3. Sebagai pengelolaan hak akses berdasarkan peran pengguna
    4. Menyesuaikan dengan pengalaman pengguna

==================================================================================

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
    Cookies adalah potongan kecil data yang disimpan di sisi client oleh aplikasi web. Cookies digunakan dalam konteks aplikasi web untuk menyimpan informasi yang dapat diakses kembali oleh server web atau aplikasi. Cookies sering digunakan untuk mengelola data sesi pengguna, melacak preferensi, mengidentifikasi pengguna, dan banyak tujuan lainnya.
    
    Cookie, juga dikenal sebagai Cookie HTTP, adalah file teks kecil yang dibuat dan dikelola oleh browser sebagai respons terhadap permintaan Server Web tertentu. Browser Anda menyimpannya secara lokal, dan sebagian besar browser akan menampilkan cookie yang dibuat berdasarkan pengaturan Privasi dan Keamanan.Cookie memudahkan penggabungan fitur tertentu yang sebelumnya tidak mungkin dilakukan menggunakan HTTP.

    Dalam konteks Django, cookies juga digunakan untuk mengelola data sesi pengguna. Django menggunakan cookies untuk mengelola data sesi pengguna melalui sebuah mekanisme yang disebut session cookies. Ini adalah cara yang umum digunakan untuk menyimpan informasi sesi pengguna di aplikasi web. Cookie Django berfungsi dengan cara yang sama seperti permintaan HTTP lainnya di Internet. Keuntungan menggunakan cookies dan mekanisme sesi seperti yang disediakan oleh Django adalah:
    - HTTP adalah protokol yang stateless, yang berarti server tidak dapat secara alami mengingat informasi antara permintaan dari pengguna. 
    - Cookies memungkinkan pengguna menyediakan pengalaman yang lebih personal untuk pengguna dengan mengingat preferensi mereka dan status sesi mereka.
    - Informasi sensitif (seperti token otentikasi) dapat disimpan dalam sesi yang dienkripsi di server, sehingga tidak terekspos di perangkat pengguna.
    
    Berikut adalah bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna:  
    1. Permintaan dikirim ke server oleh browser
        Ketika pengguna mengakses sebuah situs web dengan menggunakan browser, browser tersebut akan membuat permintaan HTTP ke server yang meng-host situs web tersebut. Permintaan ini dapat berisi berbagai informasi, seperti URL tujuan, jenis permintaan (misalnya GET atau POST), header permintaan, dan lain-lain.

    2. Server mengirimkan respons ke browser bersama dengan satu atau lebih cookie
        Setelah menerima permintaan dari browser, server akan memproses permintaan tersebut dan menghasilkan respons yang biasanya berisi konten HTML, gambar, data lain yang diminta oleh pengguna, atau cookie dalam respons.

    3. Cookie yang diterima browser dari server disimpan. Mulai sekarang, setiap kali permintaan dibuat ke server, browser akan mengirimkan cookie ini ke server hingga cookie tersebut habis masa berlakunya
        Setelah menerima cookie dari server, browser akan menyimpannya secara lokal pada perangkat pengguna. Ketika pengguna membuat permintaan berikutnya ke server, browser akan secara otomatis mengirimkan cookie tersebut ke server sebagai bagian dari header permintaan. Ini memungkinkan server untuk mengenali dan mengidentifikasi pengguna yang sudah terotentikasi atau menyimpan preferensi pengguna.

    4. Cookie akan dihapus dari browser jika sudah habis masa berlakunya
        Setiap cookie memiliki waktu masa berlaku (expire time) yang ditentukan oleh server saat mengirimkannya. Ketika waktu masa berlaku ini habis, browser akan menghapus cookie tersebut dari penyimpanan lokal. Hal ini menjadi mekanisme yang penting untuk menjaga privasi dan keamanan pengguna. Ketika cookie habis masa berlakunya, pengguna tidak lagi diidentifikasi atau tidak lagi memiliki informasi sesi yang tersimpan di browser.

==================================================================================

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    Penggunaan cookies dalam pengembangan web dapat aman jika diimplementasikan dan dikelola dengan baik. Namun, ada potensi risiko keamanan yang perlu diwaspadai. Berikut adalah beberapa risiko potensial yang terkait dengan penggunaan cookies:
    1. Jika informasi pribadi atau sensitif disimpan dalam cookies tanpa enkripsi yang memadai, ada potensi bahwa informasi tersebut dapat diakses oleh pihak yang tidak berwenang sehingga terjadi pelanggaran keamanan    
    2. Beberapa orang menganggap pelanggaran privasi pada cookies yang dapat digunakan oleh pihak-pihak tertentu (seperti iklan daring) untuk melacak perilaku pengguna secara online
    4. Penyerang dapat mencoba memanipulasi isi cookie dengan cara yang merusak. Cross-Site Scripting adalah serangan di mana penyerang menyisipkan kode skrip berbahaya ke dalam halaman web yang akan dilihat oleh pengguna lain. Jika cookies disisipkan dengan kode skrip, ini dapat digunakan untuk mencuri informasi dari pengguna yang terpengaruh.

   Berdasarkan risiko potensial penggunaan cookies diatas, pengembang perlu memitigasi risiko potensial yang terkait dengan cookies, berikut beberapa praktik terbaik yang dapat diikuti:
   1. Gunakan HTTPS untuk mengamankan transmisi data antara browser dan server, sehingga cookie tidak dapat dengan mudah disadap
   2. Enkripsi cookie sensitif atau informasi yang perlu diterapkan dan dilindungi. Pastikan untuk menggunakan cookie yang memiliki atribut "Secure" untuk memastikan bahwa mereka hanya dikirimkan melalui koneksi HTTPS
   3. Tetapkan masa berlaku yang wajar untuk cookie, terutama cookie sesi, dan pastikan bahwa mereka dihapus setelah tidak lagi diperlukan
   4. Pastikan bahwa aplikasi tidak menyisipkan data yang tidak terpercaya secara langsung ke dalam cookie tanpa validasi atau sanitasi yang memadai
   5. Berikan pengguna opsi untuk mengelola cookie, termasuk menolak cookie yang tidak diperlukan atau tidak diinginkan.

==================================================================================

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Mengimplementasikan fungsi registrasi, login, dan logout
        - Menjalankan virtual envinronment
        - Mengimport seluruh library yang dibutuhkan
        - Memasukkan fungsi register, login, dan logout ke dalam views.main
        - Membuat file html untuk register dan login di dalam folder main/templates
        - Menambahkan button di dalam main.html untuk logout
        - Mengimport function yang sudah dibuat ke dalam urls.py di main
        - Menambahkan path kearah function 

    2. Membuat dua akun pengguna dengan masing-masing tiga dummy data
        - Membuat akun dan mengisi data datanya melalui localhost:8000/

    3. Menghubungkan model Item dengan User
        - Menambahkan kode "from django.contrib.auth.models import User" pada main.models
        - Tambahkan kode "user = models.ForeignKey(User, on_delete=models.CASCADE)" pada class Item
        - Tambahkan kode "product.user = request.user dan product.save()" pada function create_books di views
        - Ubah books.objects.all() jadi books.object.filter(user=request.user) pada show_main di views
        - Simpan perubahan dengan makemigrations, masukkan input 1 sebagai default value dan input 1 sebagai user ID
        - Lakukan makemigrations dan migrate untuk migrasi model dan menyimpan data 

    4. Menampilkan detail informasi pengguna yang sedang logged in
        - Pastikan web dalam kondisi logged out
        - Menkstriksi halaman main dengan menambahkan "from django.contrib.auth.decorators import login_required" sebagai syarat masuk halaman harus melalui login
        - Set cookies dengan kode "response.set_cookie('last_login', str(datetime.datetime.now()))" dan tambahkan kode "'last_login': request.COOKIES['last_login']," pada context di views.main
        - Menambahkan kode pada function log out dengan "response.delete_cookie('last_login')"
        - Menambahkan kode html untuk detail informasi logged in dan last login

    5. Menjawab pertanyaan di dalam file README.md
    6. Melakukan git workflow (add, commit, push)
------------------------------------------------ TUGAS 3 ------------------------------------------------

1. Apa perbedaan antara form POST dan form GET dalam Django?
    - Form POST digunakan untuk mengirim data dari formulir ke server untuk mengolahnya, seperti menambahkan data ke database atau mengirim pesan.
    - Form GET digunakan untuk melakukan pencarian, filter, atau mengambil data yang sudah ada tanpa mengirimkan data tambahan ke server.

    Perbedaan antara form POST dan form GET adalah :
    1.  POST :
        - Metode HTTP yang digunakan untuk mengirim data formulir ke server 
        - Data dikirim dalam tubuh permintaan HTTP, sehingga tidak terlihat dalam URL
        - Tidak ada batasan nyata pada panjang data yang dapat dikirimkan, sehingga cocok untuk mengirim data yang besar
        - Lebih aman karena data dikirim dalam metode HTTP yang tidak terlihat dalam URL
        - Tidak cocok untuk permintaan yang dapat dibookmark karena data tidak terlihat dalam URL, sehingga tidak dapat menyimpan URL dan mengaksesnya kembali dengan parameter yang sama
        - Biasanya tidak dapat di-cache karena setiap permintaan POST dianggap unik

    2. GET :
        - Metode HTTP yang digunakan untuk mengambil data dari server
        - Data dikirim sebagai parameter di URL, sehingga terlihat dalam URL
        - Panjang URL memiliki batasan, yang dapat berbeda-beda tergantung pada server web dan peramban, sehingga GET lebih cocok ketika data pendek dan sederhana
        - Kurang aman karena data dikirim dalam metode HTTP yang terlihat dalam URL
        - Cocok untuk permintaan yang dapat dibookmark karena data terlihat dalam URL, sehingga pengguna dapat menyimpan URL dan mengaksesnya kembali dengan parameter yang sama
        - Dapat di-cache oleh beberapa peramban atau server proxy karena data terlihat dalam URL

==================================================================================

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    - XML(eXtensible Markup Language) adalah bahasa markup yang digunakan untuk mendefinisikan dan mengorganisir data terstruktur. XML digunakan untuk menyimpan, mengirim, dan mengolah data dalam format hierarkis yang dapat disesuaikan dengan kebutuhan aplikasi.
    - JSON (JavaScript Object Notation) adalah format pertukaran data yang berfokus pada objek dan array. JSON dirancang untuk menjadi ringkas dan mudah dibaca oleh manusia.
    - HTML (Hypertext Markup Language) adalah bahasa markup yang digunakan untuk membuat halaman web yang dapat ditampilkan oleh peramban web. HTML digunakan untuk mengatur tampilan dan struktur halaman web.

    1. XML
        - self-descriptive
        - XML termasuk format serbaguna yang digunakan untuk menyimpan, mengirim, dan mengolah data terstruktur
        - XML memiliki sintaks yang ketat dan harus mengikuti aturan berhenti dan aturan penutupan tag, contoh:
        <person>
            <name>Tata</name>
            <age>19</age>
        </person>
        - XML digunakan dalam berbagai konteks, termasuk pertukaran data antara aplikasi, konfigurasi, penyimpanan data, dan lain lain
        - XML lebih fleksibel dan mendukung tipe data yang lebih beragam dan lebih kompleks daripada JSON dalam hal representasi data terstruktur.
        - XML Prolog bersifat opsional, akan tetapi jika ada maka posisinya harus berada di awal dokumen XML
        - Pada dokumen XML semua elemen wajib memiliki closing tag

    2. JSON
        - self-describing
        - JSON lebih ringkas daripada XML dan lebih mudah dibaca oleh manusia
        - JSON memiliki sintaks yang lebih ringkas dan sederhana dengan pasangan nama-nilai yang menggunakan tanda titik dua, contoh:
        {
            "name": "Tata",
            "age": 19
        }
        - JSON digunakan secara luas dalam API web untuk pertukaran data antara server dan klien, konfigurasi dan penyimpanan data terstruktur
        - JSON lebih ringkas dan lebih efisien dalam hal ukuran data, mudah dipahami oleh manusia, dan lebih sering digunakan dalam kasus pertukaran data ringan
        - Value dapat berupa tipe data primitif (string, number, boolean) ataupun berupa objek

    3. HTML
        - HTML tidak digunakan untuk pengiriman data secara langsung tetapi digunakan untuk merender halaman web, menampilkan teks, gambar, tautan, dan lainnya.
        - HTML enggunakan elemen dan tag markup seperti <p> (paragraf), <img> (gambar), dan <a> (tautan)
        - HTML digunakan untuk membuat halaman web yang dapat dilihat oleh peramban web dan diakses oleh pengguna

==================================================================================

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    JSON (JavaScript Object Notation) sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki keunggulan keunggulan dibandingkan yang lainnya dan menjadikannya pilihan yang sangat baik dalam lingkungan ini, diantaranya sebagai berikut.

    - Ringkas dan Mudah Dibaca
    Data dalam JSON direpresentasikan sebagai pasangan nama-nilai, yang membuatnya sangat intuitif, sehingga pengembang dapat dengan cepat memahami struktur data.

    - Bahasa Agnostik
    JSON tidak terikat pada bahasa pemrograman tertentu. Pengembang dapat menghasilkan dan mengonsumsi data JSON dari berbagai bahasa pemrograman yang berbeda. Sebagai contoh, data JSON yang dihasilkan oleh server dapat digunakan oleh klien yang ditulis dalam bahasa pemrograman JavaScript, Python, Java, C#, dan lain-lain.

    - Dukungan Browser Built-in
    Banyak peramban web modern memiliki dukungan bawaan (built-in) untuk parsing dan menghasilkan data JSON, sehingga JSON menjadi pilihan yang ideal untuk berkomunikasi antara peramban dan server web tanpa perlu menggunakan teknik atau pustaka tambahan.

    - Efisiensi dan Kecilnya Ukuran Data
    JSON adalah format data yang ringan. Data yang dikirim dalam format JSON biasanya memiliki ukuran yang lebih kecil, sehingga dapat mengurangi beban jaringan dan mempercepat pertukaran data.

    - Kompatibilitas dengan JavaScript
    JSON sangat cocok dengan bahasa pemrograman JavaScript, yang digunakan secara luas dalam pengembangan web. Hal ini menyebabkan JSON mudah digunakan dalam pengembangan aplikasi berbasis web, termasuk aplikasi single-page (SPA) yang populer.

    - Mendukung Struktur Data Terstruktur
    JSON mendukung berbagai jenis data terstruktur, termasuk objek, array, string, angka, boolean, dan nilai-nilai null. Sehingga, aman untuk merepresentasikan data yang lebih kompleks dan fleksibel.

    - Digunakan dalam RESTful API
    JSON adalah format pertukaran data yang standar dalam arsitektur RESTful API (Application Programming Interface). API web modern sering menggunakan JSON sebagai format data yang diterima dan dikirimkan oleh server.

    - Komunitas dan Dukungan
    JSON telah menjadi standar de facto dalam pertukaran data dalam pengembangan web, dan ada banyak dukungan komunitas dan pustaka untuk mengolah data JSON di berbagai bahasa pemrograman.


==================================================================================

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Membuat input form 
        - Menambahkan extend base.html pada main.html
        - Menambahkan file baru bernama forms.py pada main dan menambahkan kode didalamnya
        - Menambahkan tambahan import pada views.py dan membuat fungsi baru bernama create_books untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data di-submit dari form
        - Mengubah render pada fungsi show_main dalam views menjadi 
        return render(request, "main.html", {'books': books, 'detail' : context})
        - Routing dengan mengimport fungsi create_books ke urls.py pada folder main
        - Menambahkan path url routing create_books ke dalam urlpatterns
        - Buat berkas html baru dengan nama create_books untuk mengisi form dan submit
        - Menambahkan kode untuk menampilkan data produk hasil dari form serta tombol "Add New Book" yang akan redirect ke halaman form.
    
    2. Menambahkan 5 fungsi pada views.py dalam folder main (show_main, show_xml, show_json, show_xml_by_id, show_json_by_id)
        - Dalam tiap fungsi ditambahkan kode berikut
        data = Books.objects.all() (HTML, XML, JSON)
        data = Books.objects.filter(pk=id) (XML_by_id, JSON_by_id)
        - Menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi
    
    3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
        - Mengimpor fungsi (show_main, show_xml, show_json, show_xml_by_id, show_json_by_id) pada urls.py yang ada pada folder main
        - Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor
    
    4. Menjawab pertanyaan di dalam file README.md
    5. Mengakses kelima URL menggunakan Postman
    6. Melakukan git workflow (add, commit, push)

==================================================================================

5. Hasil Screenshot postman
    - HTML

    ![CHEESE!](Images/html1.png)
    ![CHEESE!](Images/html2.png)

    - XML
    ![CHEESE!](Images/xml.png)

    - JSON
    ![CHEESE!](Images/json.png)

    - XML by id
    ![CHEESE!](Images/xml_by_id.png)

    - JSON by id
    ![CHEESE!](Images/json_by_id.png)



------------------------------------------------ TUGAS 2 ------------------------------------------------
Tautan link adaptable : https://galaxylibrary.adaptable.app

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. Membuat file dan repositori baru, lalu dilanjutkan dengan membuat django project

    2. Membuat aplikasi main dengan berikut tahapannya:
        - Membuat file HTML dengan isi web yang akan ditampilkan sesuai dengan tema yang diambil, yaitu "Pengelolaan koleksi perpustakaan"
        - Membuat class Books yang terdapat di dalam models.py untuk mendefinisikan data yang akan digunakan sebagai dasar dari database, diantaranya nama, jumlah, dan deskripsi
        - Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model maupun form dan dikembalikan ke dalam file HTML yang sudah dibuat
        - Meng-import models yang sudah dibuat sebelumnya ke dalam file views.py. Selanjutnya, memanggil fungsi model untuk menyimpan data baru ke dalam database. 
        - Pada views juga mengambil dan menyimpan nilai form yang telah di submit ke dalam database
        - Kemudian pada views akan melakukan render dengan books, form, dan context sebagai data yang akan dikembalikan ke dalam file HTML
        - Melakukan pemanggilan variabel detail dan form serta melakukan iterasi terhadap variabel books yang telah ikut di render ke dalam HTML.


    3. Membuat routing untuk memetakan fungsi yang telah dibuat pada views.py, berikut tahapannya:
        - Mendaftarkan aplikasi ke dalam urls.py yang terdapat pada folder another_world dengan menambahkan "path('main/', include('main.urls'))," pada variabel urlpatterns

    4. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga dapat dibuka secara umum, berikut tahapannya:
        - Melakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub
        - Deploy repository github ke dalam Adaptable dengan login, tekan tombol new app, memasukkan repository github, memilih python app_template sebagai template deployment, postgreSQL sebagai basis data, mengisi nama app, menambahkan command "python manage.py migrate && gunicorn shopping_list.wsgi", ceklis HTTP Listener on PORT, lalu deploy app
        - Apabila deployment berhasil, link aplikasi Adaptable sudah dapat dibuka oleh teman-teman


==================================================================================

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    Django framework

    ![CHEESE!](Images/Django-framework.jpg)

    Webserver work 

    ![CHEESE!](Images/Webserver-work.jpg)

    - Kaitan antara urls.py dan views.py adalah urls.py akan mem-parse argumen dan diteruskan ke views.py yang terkait, kemudian views.py akan mengambil request tersebut dan memberikan web response.
   - Kaitan antara views.py dan berkas html adalah views.py akan mengambil template dari berkas html, kemudian template tersebut di-merge di views.py dan diolah serta digabungkan.
   - Kaitan antara views.py dan models.py adalah models.py akan mengambil data dan diberikan ke views.py.

   Kaitan antara urls.py, views.py, models.py, dan berkas html adalah urls.py yang bertugas mem-parse argumen dari user dan berkas html yang berisi template web akan memberikan outputnya ke views.py. Selanjutnya, ketika ada query pemanggilan data dari views.py, models.py akan menjembatani pemanggilan data ke database. Kemudian views.py akan menggabungkan dan mengolahnya sehingga menjadi satu halaman web yang utuh.

==================================================================================

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    Virtual environment adalah sebuah alat untuk menjaga ruang terpisah untuk sebuah proyek dengan pustaka dan dependensi di satu tempat. Environment ini spesifik ke proyek tertentu dan tidak berinterfer dengan dependensi proyek lainnya. Berikut beberapa alasan mengapa kita menggunakan virtual environment:

    - Virtual environment memungkinkan untuk menginstal dan mengelola versi pustaka atau paket yang berbeda untuk setiap proyek tanpa khawatir tentang konflik dependensi. 
    - Virtual environment menghindari masalah dengan memastikan bahwa setiap proyek memiliki lingkungan sendiri yang mengisolasi dependensinya.
    - Virtual environment memungkinkan untuk menjaga kebersihan lingkungan pengembangan, sehingga dapat dengan mudah menghapus atau memperbarui dependensi yang tidak diperlukan tanpa memengaruhi lingkungan global sistem.
    - Virtual environment dapat bantu mereproduksi lingkungan pengembangan yang sama persis di berbagai mesin atau server. 
    - Virtual environment memungkinkan untuk bekerja dengan aman tanpa merusak sistem.

    Iya, Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi akan sulit, tidak efisien, tidak efektif, dan tidak produktif. Oleh karena itu, sangat disarankan untuk menggunakan virtual environment dalam pengembangan proyek Django. Melalui penggunakan virtual environment, akan menjadi praktik yang baik dalam pengembangan Django karena memberikan sejumlah keuntungan yang telah dijelaskan sebelumnya, seperti isolasi dependensi, menghindari konflik, dan menjaga kebersihan lingkungan pengembangan.

==================================================================================

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya
    1. MVC atau dikenal sebagai Model View Controller adalah sebuah pola arsitektur atau desain dalam pengembangan perangkat lunak seperti membuat sebuah aplikasi dengan cara memisahkan kode menjadi tiga bagian yang terdiri dari:
        - Model
        Bagian yang bertugas untuk mengelola data seperti menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
        - View
        Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI) kepada user.
        - Controller
        Bagian yang bertugas sebagai perantara untuk menghubungkan serta mengatur model dan view agar dapat saling terhubung.
    2. MVT atau dikenal sebagai Model View Template adalah sebuah pola arsitektur atau desain yang digunakan dalam pengembangan web aplikasi, terutama dalam kerangka kerja web Django yang sangat populer untuk bahasa pemrograman Python. MVT ini dibagi menjadi 3 bagian yang terdiri dari:
        - Model
        Bagian yang bertugas untuk mengelola data seperti menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
        - View
        Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI) kepada user.
        - Template
        Bagian yang bertugas untuk untuk mengatur tampilan dan presentasi data dalam aplikasi web.
    3. MVVM atau yang dikenal sebagai Model-View-ViewModel merupakan pola arsitektur atau desain (design pattern) yang digunakan dalam pengembangan perangkat lunak, terutama dalam pengembangan aplikasi berbasis antarmuka pengguna (UI) seperti aplikasi mobile dan aplikasi desktop. MVVM dibuat untuk memisahkan tanggung jawab dalam mengelola tampilan (UI) dari logika bisnis dalam aplikasi. MVVM ini dibagi menjadi 3 bagian yang terdiri dari:
        - Model
        Bagian yang bertugas untuk mengelola data seperti menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
        - View
        Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI) kepada user.
        - ViewModel
        Bagian yang bertugas sebagai perantara antara Model dan View dengan mengambil data dari Model dan memformatnya sedemikian rupa sehingga dapat dengan mudah ditampilkan di View. 

    Perbedaan Virtual environment ini terletak pada bagian ketiga dari MVC, MVT, dan MVVM
    - C pada MVC yaitu Controller yang bertindak sebagai perantara antara Model dan View. Mengatur aliran logika aplikasi dan menerima input dari pengguna.
    - T pada MVT yaitu Template yang digunakan untuk merender tampilan dan memisahkan tampilan data dalam aplikasi web.
    - VM pada MVVM yaitu View-Model yang bertindak sebagai perantara antara Model dan View dengan mengambil data dari Model dan memformatnya sehingga dapat dengan mudah ditampilkan di View. 

