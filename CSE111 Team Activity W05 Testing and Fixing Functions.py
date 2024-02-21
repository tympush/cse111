from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():

    assert make_full_name("Tymur", "Pushnoy") == "Pushnoy; Tymur"
    assert make_full_name("Peter", "Bob") == "Bob; Peter"
    assert make_full_name("Bob", "Peter") == "Peter; Bob"

def test_extract_family_name():

    assert extract_family_name("Pushnoy; Tymur") == "Pushnoy"
    assert extract_family_name("Bob; Peter") == "Bob"
    assert extract_family_name("Peter; Bob") == "Peter"

def test_extract_given_name():

    assert extract_given_name("Pushnoy; Tymur") == "Tymur"
    assert extract_given_name("Bob; Peter") == "Peter"
    assert extract_given_name("Peter; Bob") == "Bob"

pytest.main(["-v", "--tb=line", "-rN", __file__])