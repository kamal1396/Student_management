print("""
==========================================================================
Aparmaq istediyiniz emeliyyatin nomresini secin:
==========================================================================
==========================================================================
==========================================================================
 1 Yaratmaq istediyiniz telebe sayi
 2 Telebe yarat
 3 Butun yaradilan telebeler
 4 Telebe adina gore melumat
 5 Ən uzun adli telebe
 6 password-u 8den yuxari olan telebeler
 7 Ov soyadli telebe
 """)

datas = []


class Telebe:
    def __init__(self, _name, _surname, _email, _password):
        self.name = _name
        self.surname = _surname
        self.email = _email
        self.password = _password

    def showDetails(self):
        print(f"Adı: {self.name} Soyadı: {self.surname} E-maili: {self.email} Passwor-du: {self.password}")


def qeydiyyatSayisec():
    telebesayi = int(input("Yaratmaq istədiyiniz tələbə sayını yazın: "))
    for say in range(telebesayi):
        say += 1
        print(f"{say}-inci tələbənin qeydiyyatı")
        datas.append(Telebe(*telebeYarat()))


def telebeYarat():
    ad_input = (input("Tələbənin adı: "))
    soyad_input = str(input("Tələbənin soyadı: "))
    email_input = str(input("Tələbənin e-maili : "))
    password_input = (input("Tələbənin password-u: "))
    return [ad_input, soyad_input, email_input, password_input]


def adaGoreMelumatTap():
    normal_ad = input("adi qeyd edin: ")
    for telebe in datas:
        if normal_ad in telebe.name:
            print(f"Adi : {telebe.name} Soyadı: {telebe.surname} Email: {telebe.email} Şifrəsi: {telebe.password}")


def uzunAdTap():
    for telebe in datas:
        uzunAd = len(telebe.name)
        for telebe in range(len(datas)):
            if len(datas[telebe].name) > uzunAd:
                print(f" en uzun ad: {datas[telebe].name}")


def password8DenYuxariTap():
    for telebe in datas:
        if len(telebe.password) > 8:
            print(f" Password : {telebe.password}")


def ovSoyadliTelebeniTap():
    for telebe in datas:
        if "ov" in telebe.surname:
            print(f"{telebe.surname}")


while True:
    giris_input = int(input("istifadə etmək istidyiniz əməliiyat növünü seçin: "))
    if giris_input == 1:
        qeydiyyatSayisec()
    elif giris_input == 2:
        telebeYarat()
    elif giris_input == 3:
        for telebe in datas:
            telebe.showDetails()

    elif giris_input == 4:
        adaGoreMelumatTap()
    elif giris_input == 5:
        uzunAdTap()
    elif giris_input == 6:
        password8DenYuxariTap()
    elif giris_input == 7:
        ovSoyadliTelebeniTap()
    else:
        giris_input = int(input("istifadə etmək istidyiniz əməliiyat növünü seçin: "))

