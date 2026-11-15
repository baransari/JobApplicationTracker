from cli import (
    show_applications,
    get_application_id_from_user,
    get_application_from_user,
    get_new_status_from_user,
    show_menu,
)
from storage import (
    initialize_database,
    insert_application,
    get_all_applications,
    update_application_status,
)


def main() -> None:
    initialize_database()
    while True:
        choice = show_menu()

        if choice == "1":
            applications = get_all_applications()
            show_applications(applications)

        elif choice == "2":
            try:
                application = get_application_from_user()
                insert_application(application)
                print("Başvurunuz Başarıyla Eklenmiştir.")
            except ValueError as e:
                print(f"Yanlış giriş yaptınız : HATA MESAJI :{e}")

        elif choice == "3":
            try:
                application_id = get_application_id_from_user()
                new_status = get_new_status_from_user()
                update_application_status(application_id, new_status)
                print("Güncellemeniz başarıyla tamamlanmıştır.")
            except ValueError as e:
                print(f"Hatalı Giriş Yaptınız : HATA MESAJI {e}")

        elif choice == "4":
            print("SİSTEMDEN ÇIKIŞ YAPILIYOR...")
            break

        else:
            print("Hatalı sayı girişi yaptınız. Seçimleriniz 1-4 arası olmalıdır.")


if __name__ == "__main__":
    main()
