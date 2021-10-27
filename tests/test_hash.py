from auth.hash import Hash


def test_01():
    val1 = Hash.encrypt('123')
    assert Hash.verify(val1, '123')
    # print(val1)
