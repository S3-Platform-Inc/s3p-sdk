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
    "TemporaryRepository",
    "DownloadDocumentsAssetWithSelenium",
    "UploadToS3",
    "ExtractTextFromFile",
]

WebDriver: str = 'WebDriver'
UndetectedWebdriver: str = 'UndetectedWebdriver'
TimezoneSafeControl: str = 'TimezoneSafeControl'
CutJunkCharactersFromDocumentText: str = 'CutJunkCharactersFromDocumentText'
FilterOnlyNewDocumentWithDB: str = 'FilterOnlyNewDocumentWithDB'
SaveOnlyNewDocuments: str = 'SaveOnlyNewDocuments'
SaveDocument: str = 'SaveDocumentToDB'
AssetRepository: str = 'AssetRepository'
TemporaryRepository: str = 'TemporaryRepository'
DownloadDocumentsAssetWithSelenium = 'DownloadDocumentsAssetWithSelenium'
UploadToS3 = 'UploadToS3'
ExtractTextFromFile = 'ExtractTextFromFile'

names = (
    WebDriver,
    UndetectedWebdriver,
    TimezoneSafeControl,
    CutJunkCharactersFromDocumentText,
    FilterOnlyNewDocumentWithDB,
    SaveOnlyNewDocuments,
    SaveDocument,
    AssetRepository,
    TemporaryRepository,
    DownloadDocumentsAssetWithSelenium,
    UploadToS3,
    ExtractTextFromFile,
)
