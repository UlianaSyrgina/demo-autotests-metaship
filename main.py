import tests


def run_tests():
    tests.get_shops_test()
    tests.get_warehouses_test()
    tests.create_shop_test()
    print("All tests successfully passed")


if __name__ == '__main__':
    run_tests()