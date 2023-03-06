import csv
import os.path
import datetime

# Pizza üst sınıfını oluşturulup içine alt sınıflarda kullanılacak metodlar eklendi.
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

# Farklı pizza tabanları için Pizza üst sınıfını kullanarak 4 adet alt sınıflar oluşturuldu.
class Klasik(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 110.0)


class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita", 120.0)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("TurkPizza", 115.0)


class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 100.0)

# Yukarıda oluşturulan 4 adet pizza alt sınıfın ücretleri ile sosların ücretlerini toplayacak Decorator üst sınıfı oluşturuldu.
class Decorator:
    def __init__(self, component, pizza, extra_cost):
        self.component = component
        self.pizza = pizza
        self.extra_cost = extra_cost

    def get_cost(self):
        return self.extra_cost + self.pizza.get_cost()

    def get_description(self):
        return self.component + " soslu " + self.pizza.get_description()

# Decorator üst sınıfını baz alan 6 adet kendi özel ekstra ücretleri olan sos alt sınıfları oluşturuldu.
class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__("Zeytin", pizza, 5.0)


class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__("Mantar", pizza, 7.0)


class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__("KeciPeyniri", pizza, 10.0)


class Et(Decorator):
    def __init__(self, pizza):
        super().__init__("Et", pizza, 15.0)


class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__("Sogan", pizza, 3.0)


class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__("Misir", pizza, 4.0)

#Sipariş detaylarını tutan bir sınıf oluşturuldu.
class OrdersDatabase:
    def __init__(self):
        self.filename = 'Orders_Database.csv'  # CSV dosyasının adı
        self.fields = ['Isim', 'TC', 'Kredi Kart Numarasi', 'Kredi Karti Sifre', 'Aciklama', 'Siparis Tarihi'] # Sütun adları
        self.file_exists = os.path.exists(self.filename) # Dosyanın mevcudiyeti

    # Yeni siparişleri dosyaya eklemek için add_order oluşturuldu.
    def add_order(self, isim, tc, kredi_kart,  kredi_kart_sifre,description):
        order_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Sipariş zamanı
        order = [isim, tc, kredi_kart, kredi_kart_sifre, description, order_time]  # Yeni sipariş

        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)

            # Dosya yoksa sütun adları yazdır.
            if not self.file_exists:
                writer.writerow(self.fields)
                self.file_exists = True

            writer.writerow(order) # Siparişi dosyaya ekle.

# Menüyü yazdırma fonksiyonları
def main():
    with open("menu.txt", "r") as file:
        for line in file:
            print(line)


def main2():
    with open("menu2.txt", "r") as file:
        for line in file:
            print(line)

#Fonskiyon çağırılarak menü ekrana yazdırıldı.
main()
taban = int(input("Pizza Tabanı Seçiminiz (1-4): "))
main2()
sos = int(input("Sos Seçiminiz (11-16): "))


# Kullanıcının seçimine göre pizza ve sos değerlerini atayacak if-elif-else algoritması yazıldı.
pizza = None

if taban == 1:
    pizza = Klasik()
elif taban == 2:
    pizza = Margarita()
elif taban == 3:
    pizza = TurkPizza()
elif taban == 4:
    pizza = SadePizza()
else:
    print("Geçersiz bir seçim yaptınız. Lütfen kodu tekrar çalıştırıp geçerli bir seçim yapınız.")
    exit()

toppings = None
if sos == 11:
    toppings = Zeytin(pizza)
elif sos == 12:
    toppings = Mantar(pizza)
elif sos == 13:
    toppings = KeciPeyniri(pizza)
elif sos == 14:
    toppings = Et(pizza)
elif sos == 15:
    toppings = Sogan(pizza)
elif sos == 16:
    toppings = Misir(pizza)
else:
    print("Geçersiz bir seçim yaptınız. Lütfen kodu tekrar çalıştırıp geçerli bir seçim yapınız.")
    exit()

#Sipariş detayları yazdırıldı.
print(f"\n{toppings.get_description()} sipariş ettiniz.")
print(f"\nToplam ücret {toppings.get_cost()} TL idir.")


# Müşterinin adı, TC kimliği ve kredi kart bilgileri alındı.
isim = input("\nİsminiz: ").upper()
tc = input("\nTc Kimlik Numara: ")
kredi_kart = input("\nKredi Kartı Numaranız: ")
kredi_kart_sifre = input("\nKredi Kartı Şifreniz: ")
print(f"\n{toppings.get_description()} siparişiniz hazırlanıyor.")
print("Bizi seçtiğiniz için teşekkür ederiz!")


# OrdersDatabase sınıfından bir örnek oluşturularak orders_db değişkenine atandı.
orders_db = OrdersDatabase()
# Yeni bir sipariş eklemek için add_order yöntemini kullanıldı.
orders_db.add_order(isim, tc, kredi_kart, kredi_kart_sifre, toppings.get_description())

