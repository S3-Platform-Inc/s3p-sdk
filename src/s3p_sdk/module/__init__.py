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
    "AssetRepository",
]

WebDriver: str = 'WebDriver'
UndetectedWebdriver: str = 'UndetectedWebdriver'
TimezoneSafeControl: str = 'TimezoneSafeControl'
CutJunkCharactersFromDocumentText: str = 'CutJunkCharactersFromDocumentText'
FilterOnlyNewDocumentWithDB: str = 'FilterOnlyNewDocumentWithDB'
SaveOnlyNewDocuments: str = 'SaveOnlyNewDocuments'
SaveDocument: str = 'SaveDocumentToDB'
AssetRepository: str = 'AssetRepository'

names = (
    WebDriver,
    UndetectedWebdriver,
    TimezoneSafeControl,
    CutJunkCharactersFromDocumentText,
    FilterOnlyNewDocumentWithDB,
    SaveOnlyNewDocuments,
    SaveDocument,
    AssetRepository,
)
