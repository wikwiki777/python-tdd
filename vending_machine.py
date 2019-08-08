from byotest import *

usd_coins = {1: 20, 5: 20, 10: 20, 25: 20, 50: 20, 100: 20}
eur_coins = {1: 20, 2: 20, 5: 20, 10: 20, 20: 20, 50: 20, 100: 20}


def get_change(amount, coins=eur_coins):
    change = []
    for coin in sorted(coins.keys(), reverse=True):
        while coin <= amount and coins[coin] > 0:
            print("You have insterted {0} coins".format(amount))
            amount -= coin
            print("Checking for available change {0} and deducting from insterted coins = {1}".format(coin, amount))
            coins[coin] -= 1
            print("Available change left of denomination {0}:{1}".format(coin, coins[coin]))
            change.append(coin)

    print("Now returning your change in {0}".format(change))
    return change


# test_are_equal(get_change(0), [])
# test_are_equal(get_change(1), [1])
# test_are_equal(get_change(2), [2])
# test_are_equal(get_change(5), [5])
# test_are_equal(get_change(10), [10])
# test_are_equal(get_change(20), [20])
# test_are_equal(get_change(50), [50])
# test_are_equal(get_change(100), [100])
# test_are_equal(get_change(3), [2, 1])
# test_are_equal(get_change(7), [5, 2])
# test_are_equal(get_change(9), [5, 2, 2])
test_are_equal(get_change(35, usd_coins), [25, 10])


print("All tests pass!")
