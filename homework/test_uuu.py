from pig import Bank

def test_add_money():
    hhh = Bank()
    hhh.add_money(200)
    hhh.add_money(300)

    assert hhh.get_balance() == 500


def test_take_money():
    hhh = Bank()
    hhh.add_money(200)
    hhh.take_money(100)
    assert hhh.get_balance() == 100


def test_take_money2():
    hhh = Bank()
    hhh.take_money(100)
    assert hhh.get_balance() == 0









