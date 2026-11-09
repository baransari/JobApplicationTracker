from dataclasses import dataclass
from datetime import date


@dataclass
class JobApplication:
    application_id: str
    company_name: str
    position_title: str
    applied_on: date
    status: str = "applied"
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.application_id.strip():
            raise ValueError("Uygulam kodu boş bırakılamaz!")
        if not self.company_name.strip():
            raise ValueError("Şirket adı boş bırakılamaz!")
        if not self.position_title.strip():
            raise ValueError("Pozisyon başlığı boş bırakılamaz!")
        if not isinstance(self.applied_on, date):
            raise TypeError("Başvuru tarihi date türünde olmalı!")
        if self.status not in {"applied", "interview", "offer", "rejected", "withdrawn"}:
            raise ValueError("Status belirlenen formatlarda olmalı!")
