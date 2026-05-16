class Magazin:

    def __init__(self, ime):
        self.ime = ime
        self.produkti = {}   # {ime: {"cena": float, "kolichestvo": int, "kategoriya": str}}
        self.prikhodi = 0.0  # обща сума от продажби

    #  Метод 1 – добавяне / зареждане на продукт
    def dobavi_produkt(self, ime, cena, kolichestvo, kategoriya="Общо"):
        if cena <= 0 or kolichestvo <= 0:
            print("  [!] Цената и количеството трябва да са положителни числа.")
            return False

        if ime in self.produkti:
            self.produkti[ime]["kolichestvo"] += kolichestvo
            print(f"  [+] '{ime}' вече съществува. Наличност: +{kolichestvo} бр.")
        else:
            self.produkti[ime] = {
                "cena": cena,
                "kolichestvo": kolichestvo,
                "kategoriya": kategoriya,
            }
            print(f"  [+] Добавен продукт: {ime} | {cena:.2f} лв. | {kolichestvo} бр. | {kategoriya}")
        return True

    #  Метод 2 – преглед на наличността
    def pokaji_nalichnost(self, sortirane="ime"):
        if not self.produkti:
            print("  [!] Магазинът е празен.")
            return

        if sortirane == "cena":
            redica = sorted(self.produkti.items(), key=lambda x: x[1]["cena"])
        elif sortirane == "kolichestvo":
            redica = sorted(self.produkti.items(), key=lambda x: x[1]["kolichestvo"], reverse=True)
        else:
            redica = sorted(self.produkti.items(), key=lambda x: x[0])

        print(f"\n  {'Продукт':<22} {'Категория':<16} {'Цена':>10} {'Наличност':>12}")
        print("  " + "-" * 64)
        for ime, info in redica:
            print(
                f"  {ime:<22} {info['kategoriya']:<16} "
                f"{info['cena']:>9.2f} лв. {info['kolichestvo']:>8} бр."
            )
        print()

    #  Метод 3 – продажба
    def prodaj(self, ime, kolichestvo=1):
        if ime not in self.produkti:
            print(f"  [!] Продуктът '{ime}' не съществува в магазина.")
            return False

        produkt = self.produkti[ime]
        if produkt["kolichestvo"] < kolichestvo:
            print(
                f"  [!] Недостатъчна наличност. "
                f"Налични: {produkt['kolichestvo']} бр., заявени: {kolichestvo} бр."
            )
            return False

        suma = produkt["cena"] * kolichestvo
        produkt["kolichestvo"] -= kolichestvo
        self.prikhodi += suma
        print(
            f"  [✓] Продадено: {kolichestvo} x '{ime}' = {suma:.2f} лв. "
            f"(остатък: {produkt['kolichestvo']} бр.)"
        )
        return True

    #  Метод 4 – справка за приходи
    def spravka_prikhodi(self):
        stoynost_nalichnost = sum(
            info["cena"] * info["kolichestvo"] for info in self.produkti.values()
        )
        print(f"\n  {'='*40}")
        print(f"  Магазин: {self.ime}")
        print(f"  {'='*40}")
        print(f"  Реализирани приходи : {self.prikhodi:>12.2f} лв.")
        print(f"  Стойност на склада  : {stoynost_nalichnost:>12.2f} лв.")
        print(f"  {'='*40}\n")

    #  Метод 5 – търсене по категория
    def tarsene_po_kategoriya(self, kategoriya):
        rezultati = {
            ime: info
            for ime, info in self.produkti.items()
            if info["kategoriya"].lower() == kategoriya.lower()
        }

        if not rezultati:
            print(f"  [!] Няма продукти в категория '{kategoriya}'.")
            return

        print(f"\n  Категория: {kategoriya}")
        print(f"  {'Продукт':<22} {'Цена':>10} {'Наличност':>12}")
        print("  " + "-" * 48)
        for ime, info in sorted(rezultati.items()):
            print(f"  {ime:<22} {info['cena']:>9.2f} лв. {info['kolichestvo']:>8} бр.")
        print()
