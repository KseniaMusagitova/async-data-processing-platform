from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_upload_valid_csv():
    # Prepare a sample CSV file in memory
    csv_content = b"id,name\n1,Alice\n2,Bob\n"

    # Send the file to the API
    response = client.post(
        "/api/v1/files",
        files={"file": ("sample.csv", csv_content, "text/csv")},
    )

    # Check the response
    assert response.status_code == 201
    assert response.json() == {"filename": "sample.csv"}

def test_upload_invalid_file_type():
    # Prepare a text file
    file_content = b"Hello World"

    # Send the file to the API
    response = client.post(
        "/api/v1/files",
        files={"file": ("test.txt", file_content, "text/plain")},
    )

    # Check that the API rejects the file
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Only CSV files are allowed"
    }

def test_upload_empty_csv():
    # Prepare an empty CSV file
    csv_content = b""

    # Send the file to the API
    response = client.post(
        "/api/v1/files",
        files={"file": ("empty.csv", csv_content, "text/csv")},
    )

    # Verify that the API rejects the empty file
    assert response.status_code == 400
    assert response.json() == {
        "detail": "File cannot be empty"
    }

def test_upload_file_too_large():
    # Prepare a CSV file larger than 5 MiB
    csv_content = b"a" * (5 * 1024 * 1024 + 1)

    # Send the file to the API
    response = client.post(
        "/api/v1/files",
        files={"file": ("large.csv", csv_content, "text/csv")},
    )

    # Verify that the API rejects the large file
    assert response.status_code == 413
    assert response.json() == {
        "detail": "File exceeds the 5 MB limit"
    }