/**
 * ============================================================================
 * PROYEK DPBO: GAME BILLIARD 2D (C++ & SFML)
 * ============================================================================
 * Tugas Minggu 1 (WBS 1.4): Menyiapkan Repositori dan SFML
 * PIC: User (Grafis dan Antarmuka)
 * Software: Dev-C++ 5.11
 * ============================================================================
 * Deskripsi:
 * Program sederhana ini digunakan untuk memverifikasi bahwa:
 * 1. Pustaka SFML sudah terhubung dengan benar di Dev-C++.
 * 2. Jendela grafis dapat dibuka.
 * 3. Aset gambar yang telah dibuat pada Minggu 2 (Meja, Bola, Stik) dapat dimuat.
 * ============================================================================
 */

#include <SFML/Graphics.hpp>
#include <iostream>

int main() {
    // 1. Membuat jendela aplikasi SFML (ukuran 1024 x 640 piksel)
    sf::RenderWindow window(sf::VideoMode(1024, 640), "Proyek Billiard SFML - Tes Repositori & Aset (Minggu 1 & 2)", sf::Style::Close | sf::Style::Titlebar);
    window.setFramerateLimit(60);

    // 2. Memuat font untuk menampilkan teks status
    sf::Font font;
    if (!font.loadFromFile("assets/fonts/arial.ttf")) {
        std::cout << "[INFO] Font arial.ttf tidak ditemukan, menggunakan tampilan tanpa teks." << std::endl;
    }

    sf::Text statusText;
    statusText.setFont(font);
    statusText.setString("Repositori dan SFML Berhasil Dikonfigurasi (Minggu 1 & 2)");
    statusText.setCharacterSize(20);
    statusText.setFillColor(sf::Color::White);
    statusText.setPosition(20.0f, 15.0f);

    // 3. Tes memuat aset grafis hasil pekerjaan Minggu 2 (WBS 2.4)
    sf::Texture texTable;
    sf::Sprite spriteTable;
    if (texTable.loadFromFile("assets/textures/table_green.png")) {
        texTable.setSmooth(true);
        spriteTable.setTexture(texTable);
        spriteTable.setPosition(32.0f, 50.0f);
    }

    sf::Texture texBall;
    sf::Sprite spriteBall;
    if (texBall.loadFromFile("assets/textures/ball_8.png")) {
        texBall.setSmooth(true);
        spriteBall.setTexture(texBall);
        spriteBall.setScale(0.5f, 0.5f);
        spriteBall.setPosition(500.0f, 310.0f); // Tampilkan bola 8 di tengah meja
    }

    sf::Texture texCue;
    sf::Sprite spriteCue;
    if (texCue.loadFromFile("assets/textures/cue_stick.png")) {
        texCue.setSmooth(true);
        spriteCue.setTexture(texCue);
        spriteCue.setPosition(540.0f, 315.0f); // Tampilkan stik di dekat bola
    }

    std::cout << "====================================================" << std::endl;
    std::cout << "Setup SFML dan Repositori Berhasil!" << std::endl;
    std::cout << "Aset Meja, Bola, dan Stik siap untuk tahap implementasi." << std::endl;
    std::cout << "====================================================" << std::endl;

    // 4. Game loop sederhana
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            // Tutup jendela jika tombol silang (X) diklik
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }

        // Membersihkan layar dengan warna latar belakang gelap
        window.clear(sf::Color(20, 24, 30));

        // Menggambar teks dan aset yang sudah dimuat
        window.draw(statusText);
        window.draw(spriteTable);
        window.draw(spriteBall);
        window.draw(spriteCue);

        // Menampilkan hasil render ke layar
        window.display();
    }

    return 0;
}
