"""
S3P modules package.
It consists different modules: its unique name.
"""

__all__ = [
    'names',
    'WebDriver',
    'UndetectedWebdriver',
    'TimezoneSafeControl',
    'CutJunkCharactersFromDocumentText',
    'FilterOnlyNewDocumentWithDB',
    'SaveDocument',
]

WebDriver: str = 'WebDriver'
UndetectedWebdriver: str = 'UndetectedWebdriver'
TimezoneSafeControl: str = 'TimezoneSafeControl'
CutJunkCharactersFromDocumentText: str = 'CutJunkCharactersFromDocumentText'
FilterOnlyNewDocumentWithDB: str = 'FilterOnlyNewDocumentWithDB'
SaveOnlyNewDocuments: str = 'SaveOnlyNewDocuments'
SaveDocument: str = 'SaveDocumentToDB'

names = (
    WebDriver,
    UndetectedWebdriver,
    TimezoneSafeControl,
    CutJunkCharactersFromDocumentText,
    FilterOnlyNewDocumentWithDB,
    SaveOnlyNewDocuments,
    SaveDocument,
)
