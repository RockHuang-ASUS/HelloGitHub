from fortune_cookie import open_cookie

def test_open_cookie_char():
    chars = set("\n '(),./<>V\\_`|")
    for _ in range(100):
        assert set(open_cookie()) <= chars

def test_open_cookie_line():
    for _ in range(100):
        lines = open_cookie().splitlines()
        assert len(lines) % 6 == 2
        assert len(set([len(line) for line in lines])) == 1
