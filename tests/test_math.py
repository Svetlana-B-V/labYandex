def test_data_processing(temporary_data):
    """
    Тест использует данные из фикстуры и проверяет их обработку
    """
    print("Начало теста - данные:", temporary_data)

    # Проверяем сумму
    assert sum(temporary_data) == 15

    # Проверяем количество элементов
    assert len(temporary_data) == 5

    # Модифицируем данные (это безопасно - после теста они очистятся)
    temporary_data.append(6)
    print("Данные изменены:", temporary_data)
   
    print("Тест завершён")