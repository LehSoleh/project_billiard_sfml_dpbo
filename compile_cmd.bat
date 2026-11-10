@echo off
echo ===================================================
echo Mengompilasi Proyek Billiard SFML (Dev-C++ MinGW)
echo ===================================================

"C:\Program Files (x86)\Dev-Cpp\MinGW64\bin\g++.exe" -I"include" -I"lib/SFML/include" -L"lib/SFML/lib" src/main.cpp -lsfml-graphics -lsfml-window -lsfml-system -o BilliardGame.exe

if %ERRORLEVEL% EQU 0 (
    echo [SUKSES] Kompilasi berhasil! Menjalankan BilliardGame.exe...
    start BilliardGame.exe
) else (
    echo [GAGAL] Terjadi kesalahan kompilasi.
    pause
)
