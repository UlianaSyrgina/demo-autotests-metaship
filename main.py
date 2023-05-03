import metaship_client


def run_tests():
    shops = metaship_client.get_shops()
    for shop in shops:
        assert 'id' in shop, "Объект Shop не содержит поля 'id'"
        assert 'name' in shop, "Объект Shop не содержит поля 'name'"


if __name__ == '__main__':
    run_tests()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
