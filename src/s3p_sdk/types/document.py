from dataclasses import dataclass
from datetime import datetime
from hashlib import sha256


@dataclass
class S3PDocument:
    """
    Объект документа в S3P
    """
    id: int | None
    title: str
    abstract: str | None
    text: str | None
    link: str
    storage: str | None
    other: dict | None
    published: datetime
    loaded: datetime | None

    @property
    def hash(self) -> bytes:
        concat_name = self.title + '_' + self.link + '_' + str(self.published.timestamp())
        return sha256(concat_name.encode('utf8')).digest()

    def __eq__(self, other) -> bool:
        if isinstance(other, S3PDocument):
            return self.hash == other.hash
        else:
            raise TypeError('other is not S3PDocument')
