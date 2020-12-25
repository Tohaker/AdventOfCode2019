from lib.get_input import download_input


class TestGetInput:
    def test_download_input(self):
        expected = ['284639-748759']
        downloaded = download_input(4)
        assert expected == downloaded
