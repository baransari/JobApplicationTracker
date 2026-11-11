def get_application_id_from_user() -> str:
    application_id = input("Lütfen Başvuru kodunu giriniz: ").strip()
    return application_id


def get_new_status_from_user() -> str:
    new_status = input(
        "Lütfen yeni durumu belirlenen formatlarda giriniz(applied, interview, offer, rejected, withdrawn): "
    ).strip()
    return new_status


def show_menu() -> str:
    print("------İŞ BAŞVURUSU TAKİP SİSTEMİ-------")
    print("1. Başvuruları Görüntüle")
    print("2. Başvuru Ekle")
    print("3. Başvuru Durumunu Güncelle")
    print("4. Çıkış")

    choice = input("Lütfen bir seçim yapınız(1-4) : ").strip()
    return choice
