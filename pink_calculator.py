import tkinter as tk  # Tkinter: Python'un yerleşik GUI (arayüz) kütüphanesi

# OOP yapısında bir hesap makinesi sınıfı
class Calculator:
    def __init__(self, root):
        # Ana pencere ayarları
        self.root = root
        self.root.title("Hesap Makinesi")
        self.root.geometry("380x480")
        self.root.config(bg="#2b2b2b")  # koyu gri arka plan
        self.root.resizable(False, False)

        # Grid sistemi: her sütun ve satır eşit oranda genişlesin
        for i in range(4):
            self.root.columnconfigure(i, weight=1)
        for i in range(6):
            self.root.rowconfigure(i, weight=1)

        # Ekran (Entry widget): Sayı girişini buraya yapıyoruz.
        self.entry = tk.Entry(
            root,
            font=("Arial", 22),
            borderwidth=5,
            relief="flat",
            bg="#fdf2f8",   # çok açık pembe ton
            justify="right"  # sağa hizalı yazı
        )
        # Grid’e yerleştirme (row=0): 4 sütun boyunca uzanıyor.
        self.entry.grid(row=0, column=0, columnspan=4, padx=15, pady=15, ipady=12, sticky="nsew")

        # Buton bilgilerini (metin, satır, sütun) liste olarak tanımladığımız yer.
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("Del", 5, 0), ("=", 5, 1)
        ]

        # Her buton için tek tek tkinter Button oluşturur.
        for (text, row, col) in buttons:
            color, active = self.get_button_colors(text)  # renklendirme fonksiyonu
            if text == "=":
                # "=" tuşu geniş (3 sütunu kaplıyor)
                tk.Button(
                    root, text=text, bg=color, fg="white",
                    activebackground=active, relief="flat",
                    font=("Arial", 14, "bold"),
                    command=self.evaluate  # hesaplama fonksiyonu
                ).grid(row=row, column=col, columnspan=3, padx=6, pady=6, sticky="nsew")
            else:
                # Diğer tüm tuşlar
                tk.Button(
                    root, text=text, bg=color, fg="white",
                    activebackground=active, relief="flat",
                    font=("Arial", 14, "bold"),
                    command=lambda t=text: self.on_click(t)  # tıklama olayını gönder
                ).grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

    # Her butonun rengine karar veren fonksiyon:
    def get_button_colors(self, text):
        if text in {"+", "-", "*", "/", "="}:
            return ("#c2185b", "#ad1457")  # koyu pembe tonları
        elif text in {"C", "Del"}:
            return ("#f48fb1", "#f06292")  # toz pembe tonları
        else:
            return ("#4b4b4b", "#5c5c5c")  # gri (sayılar için)

    # Buton tıklandığında ne olacağını belirler.
    def on_click(self, char):
        if char == "C":
            # Tüm ekranı temizle
            self.entry.delete(0, tk.END)
        elif char == "Del":
            # Son karakteri sil
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current[:-1])
        else:
            # Girilen karakteri ekrana yaz
            self.entry.insert(tk.END, char)

    # "=" tuşuna basıldığında çalışır.
    def evaluate(self):
        try:
            expression = self.entry.get()  # kullanıcıdan gelen ifade
            result = eval(expression)      # matematiksel olarak değerlendir
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))  # sonucu ekrana yaz
        except Exception:
            # Hatalı girişlerde "Hata" yaz
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Hata")

# Ana pencereyi başlatır:
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
