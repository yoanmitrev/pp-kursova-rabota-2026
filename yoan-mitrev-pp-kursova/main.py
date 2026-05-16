from models import Magazin


def pokaji_meniu():
    print("\n" + "=" * 45)
    print("МАГАЗИН ЗА ТЕХНИКА – ГЛАВНО МЕНЮ")
    print("====================================")
    print("  1. Добави продукт")
    print("  2. Преглед на наличността")
    print("  3. Продай продукт")
    print("  4. Справка за приходи")
    print("  5. Търсене по категория")
    print("  0. Изход")
    print("==============================================")


def main():
    magazin = Magazin("ТехноМаркет")
     
    # Примерни продукти
    print("\n  Зареждане на начални продукти...\n")
    magazin.dobavi_produkt("Lenovo IdeaPad 3",  899.99, 5,  "Лаптопи")
    magazin.dobavi_produkt("Samsung Galaxy A55", 649.00, 8,  "Телефони")
    magazin.dobavi_produkt("Sony WH-1000XM5",   399.00, 10, "Слушалки")
    magazin.dobavi_produkt("Apple iPad 10",      799.00, 4,  "Таблети")
    magazin.dobavi_produkt("Logitech MX Master", 189.99, 15, "Аксесоари")
    magazin.dobavi_produkt("ASUS ROG Swift",     549.00, 3,  "Монитори")

    while True:
        pokaji_meniu()
        izbor = input("  Избери опция: ").strip()

        if izbor == "1":
            print("\n  -- Добавяне на продукт --")
            ime        = input("  Име на продукт : ").strip()
            kategoriya = input("  Категория      : ").strip()
            cena       = input("  Цена (лв.)     : ").strip()
            kolichestvo = input("  Количество     : ").strip()

            if not cena.replace(".", "", 1).isdigit() or not kolichestvo.isdigit():
                print("  [!] Цената и количеството трябва да са числа.")
            else:
                magazin.dobavi_produkt(ime, float(cena), int(kolichestvo), kategoriya)

        elif izbor == "2":
            print("\n  -- Сортиране по --")
            print("  1) Име   2) Цена   3) Наличност")
            
            sort_izbor = input("  Избор (Enter = по име): ").strip()
            sort_map = {"1": "ime", "2": "cena", "3": "kolichestvo"}
            sortirane = sort_map.get(sort_izbor, "ime")
            magazin.pokaji_nalichnost(sortirane)

        elif izbor == "3":
            print("\n  -- Продажба --")
            ime = input("  Продукт за продажба : ").strip()
            try:
                kolichestvo = int(input("  Количество          : "))
            except ValueError:
                print("  [!] Невалидно количество.")
                continue
            magazin.prodaj(ime, kolichestvo)

        elif izbor == "4":
            magazin.spravka_prikhodi()

        elif izbor == "5":
            print("\n  -- Търсене по категория --")
            kategoriya = input("  Категория: ").strip()
            magazin.tarsene_po_kategoriya(kategoriya)

        elif izbor == "0":
            print("\n  Довиждане! 👋\n")
            break

        else:
            print("  [!] Невалидна опция. Опитай отново.")


if __name__ == "__main__":
    main()
