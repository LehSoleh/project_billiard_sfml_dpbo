# BILLIARD 8-BALL GAME PROJECT (C++ & SFML)

## Proyek Kelompok Desain dan Pemrograman Berorientasi Objek (DPBO)

Anggota Kelompok:

- Zaki Andriansa - 1313625020
- Mochammad Fadlan - 1313625002
- Ahmad Soleh - 1313625029

---

Repositori bersama untuk pengembangan proyek game biliar 2D dengan aturan standar 8-ball menggunakan bahasa C++ dan pustaka Simple and Fast Multimedia Library (SFML). Proyek ini dikembangkan secara bersama oleh tim dengan lingkungan kerja Dev-C++ 5.11 (compiler MinGW 64-bit).

---

## 1. Deskripsi Proyek

Proyek ini bertujuan membangun game biliar 2D satu pemain melawan komputer (AI). Fitur utama yang dikembangkan mencakup:

- Permainan biliar dengan aturan bola 8 (8-ball pool).
- Tiga tingkat kesulitan lawan komputer: Mudah, Sedang, dan Sulit.
- Kontrol interaktif pembidikan stik dan pengaturan kekuatan pukulan.
- Sistem penempatan bola putih bebas (ball-in-hand) saat terjadi pelanggaran.
- Fitur jeda permainan (pause).
- Penyimpanan skor secara otomatis ke berkas lokal.
- Papan skor (leaderboard) untuk melihat rekor skor tertinggi.
- Pengaturan audio (musik dan efek suara) serta pilihan warna kain meja.

---

## 2. Pembagian Peran dan Tugas Kelompok (WBS)

Berdasarkan dokumen perencanaan proyek (Slide 5, 6, dan 8), tugas dibagi ke dalam 3 bidang penanggung jawab (Person In Charge / PIC):

### A. PIC Zaki Andriansa (Bidang Fisika dan Gameplay)

- 1.1 Menetapkan ruang lingkup dan aturan 8-ball (Minggu 1: 28 - 29 Okt)
- 2.1 Menyusun kartu CRC (Minggu 2: 4 - 5 Nov)
- 2.2 Menyusun diagram kelas (Minggu 2: 6 - 8 Nov)
- 3.2 Membuat gerak, gesekan, dan tumbukan bola (Minggu 3 dan 4: 11 - 17 Nov)
- 3.4 Membuat aturan 8-ball, giliran, dan pelanggaran (Minggu 3 dan 4: 18 - 24 Nov)
- 4.1 Membuat pemilihan bola sasaran AI (Minggu 5 dan 6: 25 - 27 Nov)
- 4.2 Membuat tingkat Mudah, Sedang, dan Sulit AI (Minggu 5 dan 6: 28 Nov - 4 Des)
- 5.5 Membuat penempatan bola putih (Minggu 5 dan 6: 2 - 5 Des)
- 6.2 Memperbaiki bug fisika dan lawan komputer (Minggu 7: 9 - 13 Des)
- 7.3 Menyiapkan presentasi dan menyerahkan proyek (Minggu 7: 14 Des)

### B. PIC Mochamad Fadlan (Bidang Audio, Pengujian, dan Dokumentasi)

- 1.2 Menyusun WBS dan jadwal (Minggu 1: 28 - 30 Okt)
- 1.3 Menyusun use case diagram dan use case scenario (Minggu 1: 29 Okt - 2 Nov)
- 2.5 Menyiapkan aset suara dan musik (Minggu 2: 7 - 10 Nov)
- 3.5 Menguji fisika dan aturan secara berkala (Minggu 3 dan 4: 18 - 24 Nov)
- 4.3 Menguji keseimbangan tingkat kesulitan AI (Minggu 5 dan 6: 5 - 8 Des)
- 5.2 Memasang efek suara dan musik (Minggu 5 dan 6: 25 Nov - 1 Des)
- 5.4 Membuat penyimpanan skor dan papan skor (Minggu 5 dan 6: 2 - 8 Des)
- 6.1 Menguji setiap use case (Minggu 7: 9 - 11 Des)
- 7.1 Menyusun laporan dan dokumentasi (Minggu 7: 14 - 15 Des)

### C. PIC Ahmad Soleh (Bidang Grafis dan Antarmuka)

- 1.4 Menyiapkan repositori dan SFML (Minggu 1: 28 Okt - 1 Nov)
- 2.3 Merancang tampilan setiap layar (Minggu 2: 4 - 6 Nov)
- 2.4 Membuat aset grafis meja, bola, dan stik (Minggu 2: 7 - 10 Nov)
- 3.1 Menggambar meja, lubang, dan bola (Minggu 3 dan 4: 11 - 14 Nov)
- 3.3 Membuat garis bidik dan indikator kekuatan (Minggu 3 dan 4: 15 - 19 Nov)
- 5.1 Membuat menu, kolom nama, dan pengaturan (Minggu 5 dan 6: 25 Nov - 1 Des)
- 5.3 Membuat tampilan skor dan giliran (Minggu 5 dan 6: 2 - 5 Des)
- 6.3 Menyempurnakan tampilan (Minggu 7: 9 - 13 Des)
- 7.2 Membuat versi rilis (Minggu 7: 14 Des)

---

## 3. Daftar Use Case Sistem

Daftar fungsi sistem yang dikembangkan dalam proyek ini:

- UC-01 Memulai pertandingan melawan komputer (Objek utama: Permainan)
- UC-02 Memilih tingkat Mudah, Sedang, atau Sulit (Objek utama: PemainKomputer)
- UC-03 Membidik dan mengatur kekuatan pukulan (Objek utama: Stik, Bola)
- UC-04 Menempatkan bola putih setelah pelanggaran (Objek utama: Wasit, Bola)
- UC-05 Menghentikan sementara dan melanjutkan permainan (Objek utama: Permainan, Menu)
- UC-06 Menyimpan skor secara otomatis ke berkas (Objek utama: PapanSkor)
- UC-07 Melihat papan skor (Objek utama: PapanSkor, Menu)
- UC-08 Mengatur suara, musik, dan warna meja (Objek utama: Pengaturan)

---

## 4. Jadwal Pelaksanaan Proyek (7 Minggu: 28 Oktober - 15 Desember 2026)

- Fase 1 Perencanaan (Minggu 1: 28 Oktober - 2 November 2026)
- Fase 2 Desain Objek (Minggu 2: 4 - 10 November 2026)
- Fase 3 Implementasi Inti (Minggu 3 dan 4: 11 - 24 November 2026)
- Fase 4 Lawan Komputer (Minggu 5 dan 6: 25 November - 8 Desember 2026)
- Fase 5 Fitur Pendukung (Minggu 5 dan 6: 25 November - 8 Desember 2026)
- Fase 6 Pengujian (Minggu 7: 9 - 13 Desember 2026)
- Fase 7 Penutupan (Minggu 7: 14 - 15 Desember 2026)

---

## 5. Struktur Direktori Repositori

```
Repo/
|-- assets/
|   |-- fonts/                   # Font teks aplikasi (arial.ttf)
|   |-- screens/                 # Gambar rancangan visual layar (WBS 2.3)
|   |   |-- screen_main_menu.png
|   |   |-- screen_player_setup.png
|   |   |-- screen_gameplay.png
|   |   |-- screen_pause_menu.png
|   |   |-- screen_settings.png
|   |   `-- screen_highscore.png
|   `-- textures/                # Aset visual permainan (WBS 2.4)
|       |-- table_green.png      # Meja hijau turnamen
|       |-- table_blue.png       # Meja biru elektrik
|       |-- table_red.png        # Meja merah marun
|       |-- ball_0.png .. 15.png # Bola 0 sampai 15
|       `-- cue_stick.png        # Stik biliar maple
|-- include/                     # File header kelas C++ (.h)
|-- src/
|   `-- main.cpp                 # Titik masuk program utama
|-- lib/
|   `-- SFML/                    # Pustaka SFML (Include & Lib)
|-- scripts/                     # Generator aset otomatis
|-- BilliardGame.dev             # File proyek Dev-C++ 5.11
|-- compile_cmd.bat              # Skrip kompilasi MinGW Dev-C++
|-- sfml-*.dll, openal32.dll     # DLL runtime SFML
|-- .gitignore                   # Konfigurasi file yang diabaikan Git
`-- README.md                    # Dokumentasi utama proyek
```

---

## 6. Petunjuk Kompilasi di Dev-C++

Setiap anggota tim dapat menjalankan proyek di Dev-C++ dengan langkah berikut:

1. Buka aplikasi Dev-C++ 5.11 pada komputer Anda.
2. Pilih menu File -> Open Project or File...
3. Arahkan dan buka berkas `BilliardGame.dev` pada direktori root proyek.
4. Tekan F9 pada keyboard (atau menu Execute -> Compile & Run).
5. Program akan terkompilasi dan jendela pengujian SFML akan terbuka.

Alternatif kompilasi cepat tanpa membuka antarmuka Dev-C++:

- Jalankan berkas `compile_cmd.bat` secara langsung melalui terminal atau klik ganda pada Windows Explorer.

---

## 7. Panduan Alur Kerja Git Bersama (Workflow)

Untuk menjaga repositori tetap rapi saat setiap anggota melakukan push pekerjaan masing-masing:

1. Pastikan selalu memperbarui kode lokal sebelum mulai bekerja:
   `git pull origin main`
2. Setiap kali menyelesaikan aktivitas WBS sesuai bidang tugas, tambahkan perubahan dan lakukan commit:
   `git add .`
   `git commit -m "feat(bidang): deskripsi aktivitas yang diselesaikan"`
3. Lakukan push perubahan ke repositori remote kelompok:
   `git push origin <nama_branch>`
4. File hasil kompilasi (_.exe, _.o, \*.layout) telah diatur pada `.gitignore` sehingga tidak akan mengotori riwayat commit bersama.
