from datetime import date
from models import JobApplication


def get_application_id_from_user() -> str:
    application_id = input("Lütfen Başvuru kodunu giriniz: ").strip()
    return application_id


def get_application_from_user() -> JobApplication:
    application_id = get_application_id_from_user()
    company_name = input("Lütfen Şirket Adını Giriniz : ").strip()
    position_title = input("Lütfen Pozisyon Adını Giriniz : ").strip()
    applied_on_text = input("Lütfen Başvuru Tarihini Giriniz (YYYY-MM-DD) : ").strip()
    try:
        applied_on = date.fromisoformat(applied_on_text)
    except ValueError as e:
        raise ValueError("Lütfen Belirlenen Formatta Tarih Girişini Yapınız!") from e

    notes = input(
        "İş bölümü hakkındaki notunuz (isteğe bağlı, boş bırakmak için Enter'a basın): "
    ).strip()

    return JobApplication(
        application_id=application_id,
        company_name=company_name,
        position_title=position_title,
        applied_on=applied_on,
        notes=notes,
    )


def get_new_status_from_user() -> str:
    new_status = input(
        "Lütfen yeni durumu belirlenen formatlarda giriniz(applied, interview, offer, rejected, withdrawn): "
    ).strip()
    return new_status


def show_applications(applications: list[JobApplication]) -> None:
    print("--------BAŞVURULAR----------")
    if not applications:
        print("Henüz Bir Başvuru Bulunmamıştır.")
        return

    for application in applications:
        print(
            f"App Kodu : {application.application_id}, Şirket Adı : {application.company_name}, Pozisyon : {application.position_title}, Başlama Tarihi: {application.applied_on.isoformat()}, Not: {application.notes}, Durum: {application.status}"
        )


def show_menu() -> str:
    print("------İŞ BAŞVURUSU TAKİP SİSTEMİ-------")
    print("1. Başvuruları Görüntüle")
    print("2. Başvuru Ekle")
    print("3. Başvuru Durumunu Güncelle")
    print("4. Çıkış")

    choice = input("Lütfen bir seçim yapınız(1-4) : ").strip()
    return choice
