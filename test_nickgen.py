import nickgen
import pytest

first = lambda x: x[0]

def test_gennick(monkeypatch):
    monkeypatch.setattr(nickgen.random, "choice", first)
    assert nickgen.gennick("vcvc") == "abab"

def test_gennick_extra(monkeypatch):
    monkeypatch.setattr(nickgen.random, "choice", first)
    assert nickgen.gennick("vcvc11") == "abab11"

def test_makepattern():
    assert nickgen.makepattern("abab", nickgen.m, nickgen.l) == "vcvc"
    assert nickgen.makepattern("abab11", nickgen.m, nickgen.l) == "vcvc11"

def test_makepattern_2():
    assert nickgen.makepattern("abab", nickgen.a, nickgen.z) == "azaz"
    assert nickgen.makepattern("abab11", nickgen.a, nickgen.z) == "azaz11"

def test_gennicks(monkeypatch):
    monkeypatch.setattr(nickgen.random, "choice", first)
    monkeypatch.setattr(nickgen, "user", None, False)
    assert nickgen.gennicks("abab") == (
        None,
        "abab",
        "vcvc",
        "azaz",
            "abab, "
            "abab, "
            "abab, "
            "abab, "
            "abab, "
            "abab, "
            "abab, "
            "abab, "
            "abab, "
            "abab")

replaces = (
    ('if 0: ', ''),
    (' '*4, ' '),
    ('process=None', 'process=random.choice'),
    (' if process is None:process=random.choice\n', ''),
    ('def gennicks(string_):','string_=ioru;'),
    ('return ','result='),
    ('gennicks(ioru)','result'),


    ('gennicks', 'A'),
    ('gennick', 'B'),
    ('derk', 'C'),
    ('makepattern', 'D'),
    ('nicks', 'E'),
    ('patterns', 'F'),
    ('pattern', 'G'),
    ('consonants', 'I'),
    ('vowels', 'J'),
    ('process', 'K'),
    ('result', 'L'),
    ('ichar', 'M'),
    ('string_', 'N'),
)

def test_print_encoded():
    print
    derps = []
    for line in open("nickgen.py", "r"):
        if line.strip() == "#!":
            break
        if "#!" in line:
            continue
        derps.append(line.replace("\n", ""))

    derp = "\n".join(derps)
    for x,y in replaces:
        derp = derp.replace(x, y)
    derp = derp.strip()
    print derp
    print
    print
    derp = derp.encode("bz2").encode("base64")\
            .replace("\n", "")
    print len(derp)
    print derp
    print


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
