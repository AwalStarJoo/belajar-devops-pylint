"""Modul demonstrasi perbaikan kualitas kode."""

import math


def hitung_penjumlahan(angka1, angka2):
    """Menghitung penjumlahan dua angka.

    Args:
        angka1: Angka pertama.
        angka2: Angka kedua.

    Returns:
        Hasil penjumlahan angka1 dan angka2.
    """
    return angka1 + angka2


def main():
    """Fungsi utama program."""
    hasil = hitung_penjumlahan(10, 20)
    akar = math.sqrt(hasil)
    print(f"Hasil: {hasil}, Akar: {akar}")


if __name__ == "__main__":
    main()