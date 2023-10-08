from src import functions


def test_get_operations():
    pass


def test_get_executed_operations():
    assert functions.get_executed_operations([{"id": 441945886, "state": "EXECUTED"}, {}, {"id": 587085106, "state": "CANCELED"}]) == [{"id": 441945886, "state": "EXECUTED"}]


def test_sort_by_date():
    assert functions.sort_by_date([{"date": "2019-08-26"}, {"date": "2019-07-03"}, {"date": "2018-06-30"}], 2) == [{"date": "2019-07-03"}, {"date": "2019-08-26"}]


def test_get_output_data():
    assert functions.get_output_data(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }) == f'26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n'
    assert functions.get_output_data(
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }) == f'23.03.2018 Открытие вклада\nДанных нет -> Счет **2431\n48223.05 руб.\n'
    assert functions.get_output_data(
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
         }) == f'04.04.2019 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n79114.93 USD\n'

