import random
from datetime import datetime, timedelta
from s3p_sdk.types import S3PDocument


def random_doc(seed: int = None, published: datetime = None) -> S3PDocument:
    # Initialize random number generator
    if seed is not None:
        random.seed(seed)
    else:
        random.seed(datetime.now().timestamp())

    # Generate random values for each field
    id = random.randint(1, 1000)  # Random ID between 1 and 1000
    title = f"Document Title {id}"
    abstract = f"This is a random abstract for document {id}." if random.choice([True, False]) else None
    text = f"This is the full text of document {id}." if random.choice([True, False]) else None
    link = f"https://unittest.com/documents/{id}"
    storage = f"storage_location_{random.randint(1, 10)}" if random.choice([True, False]) else None
    other = {"key": f"value_{random.randint(1, 100)}"} if random.choice([True, False]) else None

    # Use the provided published date or generate a random one
    if published is None:
        published = datetime.now() - timedelta(days=random.randint(0, 365))

    loaded = datetime.now() if random.choice([True, False]) else None

    return S3PDocument(
        id=id,
        title=title,
        abstract=abstract,
        text=text,
        link=link,
        storage=storage,
        other=other,
        published=published,
        loaded=loaded
    )
