"""
S3P modules package.
It consists different modules: its unique name.
"""

__all__ = [
    'names',
    'WebDriver',
    'TimezoneSafeControl',
    'CutJunkCharactersFromDocumentText',
    'FilterOnlyNewDocumentWithDB',
    'SaveDocument',
]

WebDriver: str = 'WebDriver'
TimezoneSafeControl: str = 'TimezoneSafeControl'
CutJunkCharactersFromDocumentText: str = 'CutJunkCharactersFromDocumentText'
FilterOnlyNewDocumentWithDB: str = 'FilterOnlyNewDocumentWithDB'
SaveDocument: str = 'SaveDocumentToDB'

names = (
    WebDriver,
    TimezoneSafeControl,
    CutJunkCharactersFromDocumentText,
    FilterOnlyNewDocumentWithDB,
    SaveDocument,
)
