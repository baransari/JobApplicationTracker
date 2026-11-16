from models import VALID_STATUSES
from storage import update_application_status


def change_application_status(
    application_id: str, new_status: str, db_path: str = "applications.db"
) -> None:
    if new_status not in VALID_STATUSES:
        raise ValueError("Girilen durum geçersiz!")

    update_application_status(application_id, new_status, db_path)
