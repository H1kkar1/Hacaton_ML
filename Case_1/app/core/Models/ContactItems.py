from dataclasses import dataclass

@dataclass
class Contact:
    resume_contact_item_id: int
    value: str
    comment: str
    contact_type: str

    def data(self):
        return {
            "resume_contact_item_id": self.resume_contact_item_id,
            "value": self.value,
            "comment": self.comment,
            "contact_type": self.contact_type,
        }
