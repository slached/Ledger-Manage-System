# This file contains tests
import sys
import os
import pytest
import secrets

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from random import randrange
from fastapi.testclient import TestClient
from monorepo import app
from monorepo.core.ledgers.schemas import LedgerOperationConf

client = TestClient(app)


# all test functions must contain test_
# Positive Tests
# we will store the created owner data in
@pytest.fixture(scope="module")
def create_owner_fixture():
    test_body = {
        "name": f"test_name_{randrange(0,1000)}",
        "surname": f"test_surname_{randrange(0,1000)}",
        "balance": 4,
    }
    response = client.post("/create_owner", json=test_body)
    assert response.status_code == 200
    return response.json()["id"]


def test_create_owner(create_owner_fixture):
    assert create_owner_fixture is not None


def test_get_balance(create_owner_fixture):
    response = client.get(f"/ledger/{create_owner_fixture}")
    assert response.status_code == 200
    assert response.json()["balance"] == 4


def test_add_ledger_entry(create_owner_fixture):
    test_body = {
        "owner_id": f"{create_owner_fixture}",
        # content creation needs 5 credit but user has 4 so this test response must be return 400 sufficient
        "ledger_operation": LedgerOperationConf.CONTENT_CREATION.name,
        "nonce": str(secrets.token_bytes(16).hex()),
    }
    response = client.post("/ledger", json=test_body)
    assert response.status_code == 400

# must fail
def test_add_ledger_entry_fail(create_owner_fixture):
    test_body = {
        "owner_id": f"{create_owner_fixture}",
        # content creation needs 5 credit but user has 4 so this test response must be return 400 sufficient
        "ledger_operation": LedgerOperationConf.CONTENT_CREATION.name,
        "nonce": str(secrets.token_bytes(16).hex()),
    }
    response = client.post("/ledger", json=test_body)
    assert response.status_code == 200
