# File: main.py

from antrian_pesanan import AntrianPesanan

def main():
    antrian = AntrianPesanan()

    antrian.display_antrian()

    antrian.enqueue("nasi goreng")
    antrian.enqueue("mie ayam")
    antrian.enqueue("Sate")

    antrian.display_antrian()

    antrian.dequeue()

    antrian.display_antrian()

    antrian.dequeue()

    antrian.display_antrian()

if __name__ == "__main__":
    main()
