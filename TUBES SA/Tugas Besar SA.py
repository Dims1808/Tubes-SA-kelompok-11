import tkinter as tk  # Mengimpor modul tkinter untuk membuat antarmuka grafis
from itertools import combinations  # Mengimpor fungsi combinations dari modul itertools

class FurnitureSelection:  # Membuat kelas FurnitureSelection
    def __init__(self, master):  # Mendefinisikan fungsi __init__ untuk inisialisasi objek
        self.master = master  # Menetapkan master (root window) ke objek
        self.master.title("Furniture Selection")  # Mengatur judul jendela aplikasi

        # Daftar barang-barang furnitur beserta harganya
        self.furniture_items = [
            ("Sofa", 2000000),
            ("Meja", 500000),
            ("Rak TV", 800000),
            ("Lampu", 250000),
            ("Rak Buku", 500000)
        ]
        # Mengubah harga setiap barang furnitur dari string menjadi integer
        self.furniture_items = [(name, int(price)) for name, price in self.furniture_items]

        # Membuat label untuk label "Budget:"
        self.budget_label = tk.Label(master, text="Budget:")
        self.budget_label.pack()
        # Membuat entry untuk pengguna memasukkan budget
        self.budget_entry = tk.Entry(master)
        self.budget_entry.pack()

        # Membuat tombol untuk pemilihan Brute Force dan menetapkan fungsi brute_force_select sebagai perintah saat diklik
        self.brute_force_button = tk.Button(master, text="Brute Force", command=self.brute_force_select)
        self.brute_force_button.pack()
        # Membuat tombol untuk pemilihan Greedy dan menetapkan fungsi greedy_select sebagai perintah saat diklik
        self.greedy_button = tk.Button(master, text="Greedy", command=self.greedy_select)
        self.greedy_button.pack()
        # Membuat tombol untuk pemilihan Dynamic Programming dan menetapkan fungsi dynamic_select sebagai perintah saat diklik
        self.dynamic_button = tk.Button(master, text="Dynamic Programming", command=self.dynamic_select)
        self.dynamic_button.pack()

        # Membuat label untuk menampilkan item-item yang dipilih
        self.result_label = tk.Label(master, text="Selected items:")
        self.result_label.pack()
        # Membuat Text widget untuk menampilkan item-item yang dipilih
        self.result_text = tk.Text(master, height=10, width=40)
        self.result_text.pack()

    def brute_force_select(self):  # Mendefinisikan fungsi untuk pemilihan Brute Force
        budget = int(self.budget_entry.get())  # Mengambil nilai budget dari input pengguna
        selected_items = self.brute_force(self.furniture_items, budget)  # Memanggil fungsi brute_force
        self.display_result(selected_items)  # Memanggil fungsi display_result untuk menampilkan hasil

    def greedy_select(self):  # Mendefinisikan fungsi untuk pemilihan Greedy
        budget = int(self.budget_entry.get())  # Mengambil nilai budget dari input pengguna
        selected_items = self.greedy(self.furniture_items, budget)  # Memanggil fungsi greedy
        self.display_result(selected_items)  # Memanggil fungsi display_result untuk menampilkan hasil

    def dynamic_select(self):  # Mendefinisikan fungsi untuk pemilihan Dynamic Programming
        budget = int(self.budget_entry.get())  # Mengambil nilai budget dari input pengguna
        selected_items = self.dynamic_programming(self.furniture_items, budget)  # Memanggil fungsi dynamic_programming
        self.display_result(selected_items)  # Memanggil fungsi display_result untuk menampilkan hasil

    def display_result(self, selected_items):  # Mendefinisikan fungsi untuk menampilkan hasil pemilihan
        self.result_text.delete(1.0, tk.END)  # Menghapus teks sebelumnya dari Text widget
        for item in selected_items:  # Iterasi melalui item-item yang dipilih
            self.result_text.insert(tk.END, f"{item[0]} - Rp {item[1]}\n")  # Menambahkan item ke dalam Text widget

    def brute_force(self, furniture_items, budget):  # Mendefinisikan fungsi Brute Force
        selected_items = []  # Inisialisasi daftar untuk item-item yang dipilih
        max_value = 0  # Inisialisasi nilai maksimum

        # Melakukan iterasi untuk kombinasi dari setiap ukuran (dari 1 hingga semua barang)
        for r in range(1, len(furniture_items) + 1):
            combinations_list = list(combinations(furniture_items, r))  # Membuat daftar kombinasi
            for combination in combinations_list:  # Iterasi melalui setiap kombinasi
                total_price = sum(item[1] for item in combination)  # Menghitung total harga kombinasi
                if total_price <= budget:  # Jika total harga tidak melebihi budget
                    total_value = sum(item[1] for item in combination)  # Menghitung total nilai kombinasi
                    if total_value > max_value:  # Jika total nilai kombinasi lebih besar dari nilai maksimum sebelumnya
                        max_value = total_value  # Perbarui nilai maksimum
                        selected_items = combination  # Perbarui item-item yang dipilih
        return selected_items  # Kembalikan item-item yang dipilih

    def greedy(self, furniture_items, budget):  # Mendefinisikan fungsi Greedy
        sorted_items = sorted(furniture_items, key=lambda x: x[1])  # Mengurutkan item berdasarkan harga
        selected_items = []  # Inisialisasi daftar untuk item-item yang dipilih
        remaining_budget = budget  # Inisialisasi sisa budget

        # Iterasi melalui item-item yang diurutkan
        for item in sorted_items:
            if item[1] <= remaining_budget:  # Jika harga item tidak melebihi sisa budget
                selected_items.append(item)  # Tambahkan item ke dalam daftar yang dipilih
                remaining_budget -= item[1]  # Kurangi sisa budget dengan harga item
        return selected_items  # Kembalikan item-item yang dipilih

    def dynamic_programming(self, furniture_items, budget):  # Mendefinisikan fungsi Dynamic Programming
        n = len(furniture_items)  # Jumlah barang furnitur
        dp = [[0] * (budget + 1) for _ in range(n + 1)]  # Matriks untuk menyimpan hasil DP

        # Melakukan iterasi untuk setiap barang furnitur
        for i in range(1, n + 1):
            for j in range(1, budget + 1):  # Melakukan iterasi untuk setiap nilai budget
                if furniture_items[i - 1][1] <= j:  # Jika harga barang furnitur tidak melebihi budget
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - furniture_items[i - 1][1]] + furniture_items[i - 1][1])
                    # Memilih nilai maksimum antara hasil sebelumnya dan hasil tambahan dari barang furnitur saat ini
                else:
                    dp[i][j] = dp[i - 1][j]  # Jika harga barang furnitur melebihi budget, gunakan hasil sebelumnya

        selected_items = []  # Inisialisasi daftar untuk item-item yang dipilih
        j = budget  # Nilai sementara dari budget
        for i in range(n, 0, -1):  # Iterasi mundur untuk memilih item-item yang dipilih
            if dp[i][j] != dp[i - 1][j]:  # Jika nilai DP berubah, tambahkan barang furnitur ke dalam daftar yang dipilih
                selected_items.append(furniture_items[i - 1])
                j -= furniture_items[i - 1][1]  # Kurangi budget dengan harga barang furnitur yang dipilih
        return selected_items  # Kembalikan item-item yang dipilih

root = tk.Tk()  # Membuat objek root (window utama)
ui = FurnitureSelection(root)  # Membuat objek FurnitureSelection dengan root sebagai master
root.mainloop()  # Memanggil metode mainloop untuk menjalankan aplikasi
