from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import S3PDocument, S3PUser, S3PRole


@dataclass
class S3PScore:
    """
    id, score, comment, document_id, user_id, role_id, date
    """
    id: int
    score: dict
    comment: str | None
    document: S3PDocument | None
    user: S3PUser | None
    role: S3PRole | None


