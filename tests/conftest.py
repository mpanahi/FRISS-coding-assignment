import pytest
from fastapi.testclient import TestClient
import sys
sys.path.insert(0, './')
from db import *
import sql_app.models as models
from main import *

import json
@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite:///testing.db", connect_args={"check_same_thread": False}
    )
    models.Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")  #
def client_fixture(session: Session):  #
    def get_db_override():  #
        return session

    app.dependency_overrides[get_db] = get_db_override  #

    client = TestClient(app)  #
    yield client  #
    app.dependency_overrides.clear()  #