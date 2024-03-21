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

    @property
    def to_logging(self) -> str:
        """
        General string representation of the S3P document for logging purposes
        :return:
        """
        _id = ''
        if self.id:
            _id = f' | ID\'s: {self.id}'
        return f'S3P document{_id} | name: {self.title} | link to web: {self.link} | publication date: {self.published}'

    def __eq__(self, other) -> bool:
        if isinstance(other, S3PDocument):
            return self.hash == other.hash
        else:
            raise TypeError('other is not S3PDocument')
