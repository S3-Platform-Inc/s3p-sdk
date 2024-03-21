from hashlib import sha256

import pytest
import datetime

from s3p_sdk.types import S3PRefer


class TestDocument:
    refer = {
        "1": {
            "id": 1,
            "name": "refer 1",
            "type": "SOURCE",
            "loaded": datetime.datetime.now()
        },
        "1noID": {
            "id": None,
            "name": "refer 1",
            "type": "SOURCE",
            "loaded": datetime.datetime.now()
        },
        "2": {
            "id": 2,
            "name": "refer 2",
            "type": "SOURCE",
            "loaded": datetime.datetime.now()
        },
        "2noID": {
            "id": None,
            "name": "refer 2",
            "type": "SOURCE",
            "loaded": datetime.datetime.now()
        }
    }

    def test_to_logging(self):
        refer = S3PRefer(
            self.refer.get("1").get("id"),
            self.refer.get("1").get("name"),
            self.refer.get("1").get("type"),
            self.refer.get("1").get("loaded"),
        )

        test_string = f'S3P refer | ID\'s: {self.refer.get("1").get("id")} | name: {self.refer.get("1").get("name")} | type: {self.refer.get("1").get("type")}'

        assert test_string == refer.to_logging

    def test_to_logging_without_id(self):
        refer = S3PRefer(
            None,
            self.refer.get("1").get("name"),
            self.refer.get("1").get("type"),
            self.refer.get("1").get("loaded"),
        )

        test_string = f'S3P refer | name: {self.refer.get("1").get("name")} | type: {self.refer.get("1").get("type")}'

        assert test_string == refer.to_logging
