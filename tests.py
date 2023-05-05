import metaship_client


def get_shops_test():
    shops = metaship_client.get_shops()
    for shop in shops:
        assert 'id' in shop, "Объект Shop не содержит поля 'id'"
        assert 'name' in shop, "Объект Shop не содержит поля 'name'"


def get_warehouses_test():
    warehouses = metaship_client.get_warehouses()
    for warehouse in warehouses:
        assert 'id' in warehouse, "Объект Warehouse не содержит поля 'id'"
        assert 'name' in warehouse, "Объект Warehouse не содержит поля 'name'"


def create_shop_test():
    new_shop = metaship_client.create_shop()
    assert 'id' in new_shop, "Объект Shop не содержит поля 'id'"
    assert 'type' in new_shop, "Объект Shop не содержит поля 'type'"
    assert 'url' in new_shop, "Объект Shop не содержит поля 'url'"
    assert 'status' in new_shop, "Объект Shop не содержит поля 'status'"
    assert new_shop['status'] == 201, "Создание объекта Shop завершилось неудачно"
