from tip_calculator import calculateTip




def test_calculateTip():
    assert calculateTip(10, 15) == 1.5
    assert calculateTip(11.25, 15) == 1.69