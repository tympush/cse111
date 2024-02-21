import pytest
from dice_roller import roll_dice
from dice_roller import get_data



def test_roll_dice():

    for x in range(10):
        diceroll = roll_dice(1, 6)
        assert isinstance(diceroll, int)
        assert 1 <= diceroll <= 6



def test_get_data():

    test_data = get_data("score.csv")

    assert isinstance(test_data, dict), "Returned data is not a dictionary"

    assert test_data["Dirk"] == ["Dirk", "6", "6.0", "1"]
    assert test_data["tymur"] == ["tymur", "29168", "3.51", "8301"]
    assert test_data["Khorne"] == ["Khorne", "310", "3.52", "88"]
    assert test_data["you mean to tell me a shrimp fried this rice?"] == ["you mean to tell me a shrimp fried this rice?", "33", "3.67", "9"]
    assert test_data["h"] == ["h", "136", "3.32", "41"]
    assert test_data["Polish Tank"] == ["Polish Tank", "1034", "3.46", "299"]
    assert test_data["1"] == ["1", "34", "3.78", "9"]
    assert test_data["goo goobie"] == ["goo goobie", "237", "3.43", "69"]
    assert test_data["raid shadow legends"] == ["raid shadow legends", "360", "3.6", "100"]



pytest.main(["-v", "--tb=line", "-rN", __file__])