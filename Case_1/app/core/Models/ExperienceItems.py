from dataclasses import dataclass

@dataclass
class Experience:
    starts: str
    ends: str
    employer: str
    city: str
    url: str
    position: str
    description: str
    order: int

    def data(self):
        return {
            'starts': self.starts,
            'ends': self.ends,
            'employer': self.employer,
            'city': self.city,
            'url': self.url,
            'position': self.position,
            'description': self.description,
            'order': self.order,
        }