from hashlib import sha256

import pytest
import datetime

from s3p_sdk.types import S3PDocument


class TestDocument:
    data = {
        "doc1": {
            "id": None,
            "title": "title for doc 1",
            "abstract": "abstract for doc 1",
            "text": "text for doc 1",
            "link": "www.link.test",
            "storage": "storage.link",
            "other": None,
            "published": datetime.datetime(2024, 3, 3),
            "loaded": None
        },
        "doc2": {
            "id": 2,
            "title": "title for doc 2",
            "abstract": "abstract for doc 2",
            "text": "text for doc 2",
            "link": "www.link2.test",
            "storage": "storage2.link",
            "other": None,
            "published": datetime.datetime(2024, 3, 3),
            "loaded": None
        },
        "doc2-clone": {
            "id": None,
            "title": "title for doc 2",
            "abstract": "abstract for doc 2",
            "text": "text for doc 2",
            "link": "www.link2.test",
            "storage": "storage2.link",
            "other": None,
            "published": datetime.datetime(2024, 3, 3),
            "loaded": None
        }
    }

    def test_true_hash(self):
        testdoc = S3PDocument(
            self.data.get('doc1').get("id"),
            self.data.get('doc1').get("title"),
            self.data.get('doc1').get("abstract"),
            self.data.get('doc1').get("text"),
            self.data.get('doc1').get("link"),
            self.data.get('doc1').get("storage"),
            self.data.get('doc1').get("other"),
            self.data.get('doc1').get("published"),
            self.data.get('doc1').get("loaded"),
        )

        test_concat_name = str(self.data.get('doc1').get("title")) + '_' + str(self.data.get('doc1').get("link")) + '_' + str(
            self.data.get('doc1').get("published").timestamp())
        test_hash = sha256(test_concat_name.encode('utf8')).digest()
        assert test_hash == testdoc.hash

    def test_broke_title_hash(self):
        testdoc = S3PDocument(
            self.data.get('doc1').get("id"),
            None,
            self.data.get('doc1').get("abstract"),
            self.data.get('doc1').get("text"),
            self.data.get('doc1').get("link"),
            self.data.get('doc1').get("storage"),
            self.data.get('doc1').get("other"),
            self.data.get('doc1').get("published"),
            self.data.get('doc1').get("loaded"),
        )

        # test_concat_name = str(self.data.get('doc1').get("title")) + '_' + str(
        #     self.data.get('doc1').get("link")) + '_' + str(
        #     self.data.get('doc1').get("published").timestamp())
        # test_hash = sha256(test_concat_name.encode('utf8')).digest()
        pytest.raises(TypeError)

    def test_broke_published_hash(self):
        testdoc = S3PDocument(
            self.data.get('doc1').get("id"),
            self.data.get('doc1').get("title"),
            self.data.get('doc1').get("abstract"),
            self.data.get('doc1').get("text"),
            self.data.get('doc1').get("link"),
            self.data.get('doc1').get("storage"),
            self.data.get('doc1').get("other"),
            None,
            self.data.get('doc1').get("loaded"),
        )

        # test_concat_name = str(self.data.get('doc1').get("title")) + '_' + str(
        #     self.data.get('doc1').get("link")) + '_' + str(
        #     self.data.get('doc1').get("published").timestamp())
        # test_hash = sha256(test_concat_name.encode('utf8')).digest()
        pytest.raises(TypeError)

    def test_need_only_hash(self):
        testdoc = S3PDocument(
            None,
            self.data.get('doc1').get("title"),
            None,
            None,
            self.data.get('doc1').get("link"),
            None,
            None,
            self.data.get('doc1').get("published"),
            None,
        )

        test_concat_name = str(self.data.get('doc1').get("title")) + '_' + str(
            self.data.get('doc1').get("link")) + '_' + str(
            self.data.get('doc1').get("published").timestamp())
        test_hash = sha256(test_concat_name.encode('utf8')).digest()
        # pytest.raises(TypeError)
        assert test_hash == testdoc.hash

    def test_equality_different_doc(self):
        testdoc1 = S3PDocument(
            self.data.get('doc1').get("id"),
            self.data.get('doc1').get("title"),
            self.data.get('doc1').get("abstract"),
            self.data.get('doc1').get("text"),
            self.data.get('doc1').get("link"),
            self.data.get('doc1').get("storage"),
            self.data.get('doc1').get("other"),
            self.data.get('doc1').get("published"),
            self.data.get('doc1').get("loaded"),
        )
        testdoc2 = S3PDocument(
            self.data.get('doc2').get("id"),
            self.data.get('doc2').get("title"),
            self.data.get('doc2').get("abstract"),
            self.data.get('doc2').get("text"),
            self.data.get('doc2').get("link"),
            self.data.get('doc2').get("storage"),
            self.data.get('doc2').get("other"),
            self.data.get('doc2').get("published"),
            self.data.get('doc2').get("loaded"),
        )

        assert testdoc1 != testdoc2

    def test_equality_copies_doc(self):
        testdoc2 = S3PDocument(
            self.data.get('doc2').get("id"),
            self.data.get('doc2').get("title"),
            self.data.get('doc2').get("abstract"),
            self.data.get('doc2').get("text"),
            self.data.get('doc2').get("link"),
            self.data.get('doc2').get("storage"),
            self.data.get('doc2').get("other"),
            self.data.get('doc2').get("published"),
            self.data.get('doc2').get("loaded"),
        )
        testdoc2_copy = S3PDocument(
            self.data.get('doc2-clone').get("id"),
            self.data.get('doc2-clone').get("title"),
            self.data.get('doc2-clone').get("abstract"),
            self.data.get('doc2-clone').get("text"),
            self.data.get('doc2-clone').get("link"),
            self.data.get('doc2-clone').get("storage"),
            self.data.get('doc2-clone').get("other"),
            self.data.get('doc2-clone').get("published"),
            self.data.get('doc2-clone').get("loaded"),
        )

        assert testdoc2_copy == testdoc2

    def test_to_logging(self):
        testdoc = S3PDocument(
            self.data.get('doc2').get("id"),
            self.data.get('doc2').get("title"),
            self.data.get('doc2').get("abstract"),
            self.data.get('doc2').get("text"),
            self.data.get('doc2').get("link"),
            self.data.get('doc2').get("storage"),
            self.data.get('doc2').get("other"),
            self.data.get('doc2').get("published"),
            self.data.get('doc2').get("loaded"),
        )

        string_for_logging = (f"S3P document | ID\'s: {self.data.get('doc2').get('id')} "
                              f"| name: {self.data.get('doc2').get('title')} "
                              f"| link to web: {self.data.get('doc2').get('link')} "
                              f"| publication date: {self.data.get('doc2').get('published')}")

        assert string_for_logging == testdoc.to_logging

    def test_to_logging_without_id(self):
        testdoc = S3PDocument(
            None,
            self.data.get('doc2').get("title"),
            self.data.get('doc2').get("abstract"),
            self.data.get('doc2').get("text"),
            self.data.get('doc2').get("link"),
            self.data.get('doc2').get("storage"),
            self.data.get('doc2').get("other"),
            self.data.get('doc2').get("published"),
            self.data.get('doc2').get("loaded"),
        )

        string_for_logging = (f"S3P document "
                              f"| name: {self.data.get('doc2').get('title')} "
                              f"| link to web: {self.data.get('doc2').get('link')} "
                              f"| publication date: {self.data.get('doc2').get('published')}")

        assert string_for_logging == testdoc.to_logging
