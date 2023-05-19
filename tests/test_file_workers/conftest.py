import pytest

cnt = 0

@pytest.fixture(autouse=True)
def clean_text_file():
    global cnt
    with open('tests/copy_prodfile.txt', 'w'):
        pass

    print(cnt)
    cnt += 1