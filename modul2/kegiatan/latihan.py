expenses = [
    {"tanggal": "2023-07-25", "deskripsi": "Makan Siang", "jumlah": 50000},
    {"tanggal": "2023-07-25", "deskripsi": "Transportasi", "jumlah": 25000},
    {"tanggal": "2023-07-26", "deskripsi": "Belanja", "jumlah": 100000},
]


# TODO 1 Buatlah Fungsi add_expense disini untuk
# menambahkan pengeluaran baru ke dalam expenses. Jangan lupa gunakan pure-function.
def add_expense(date, description, amount):
    new_expense = {"tanggal": date, "deskripsi": description, "jumlah": amount}
    return expenses + [new_expense]


# TODO 2 Buatlah fungsi calculate_total_expenses disini
# menggunakan lambda expression untuk menghitung total pengeluaran harian.
calculate_total_expenses = lambda date: sum(
    expense["jumlah"] for expense in expenses if expense["tanggal"] == date
)


# TODO 3 Buatlah fungsi get_expenses_by_date disini menggunakan
# list comprehension untuk menyaring pengeluaran berdasarkan tanggal tertentu.
def get_expenses_by_date(date):
    return [expense for expense in expenses if expense["tanggal"] == date]


# TODO 4 Buatlah fungsi generate_expenses_report disini
# sebagai generator untuk menghasilkan laporan pengeluaran harian dalam bentuk string.
def generate_expenses_report():
    for date in set(expense["tanggal"] for expense in expenses):
        total = calculate_total_expenses(date)
        expenses_on_date = get_expenses_by_date(date)
        detail = ", ".join(
            [
                f"{expense['deskripsi']} - Rp {expense['jumlah']}"
                for expense in expenses_on_date
            ]
        )
        report = f"Laporan Pengeluaran Tanggal {date}:\nTotal Pengeluaran: Rp {total}\nDetail Pengeluaran:\n{detail}"
        yield report


get_user_input = lambda command: int(input(command))


def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    new_expenses = add_expense(date, description, amount)
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses


def view_expenses_by_date():
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")


def view_expenses_report():
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report()
    for entry in expenses_report:
        print(entry)


def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")


def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")

        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            total_expenses = calculate_total_expenses(date)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date()
        elif choice == 4:
            view_expenses_report()
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")


if __name__ == "__main__":
    main()
