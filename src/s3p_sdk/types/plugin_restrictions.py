import dataclasses
from datetime import datetime

from s3p_sdk.types import S3PDocument


@dataclasses.dataclass
class S3PPluginRestrictions:
    maximum_materials: int | None
    to_last_material: S3PDocument | None
    from_date: datetime | None
    to_date: datetime | None


MAX_MATERIAL = "MAX_MATERIAL"
LAST_MATERIAL = "LAST_MATERIAL"
FROM_DATE = "FROM_DATE"
TO_DATE = "TO_DATE"
