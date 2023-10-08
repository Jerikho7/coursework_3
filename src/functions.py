import json
import datetime


def get_operations(path):
    with open(path, 'r', encoding='utf-8') as file:
        operations = json.load(file)
    return operations


def get_executed_operations(list_operations):
    executed_operations = []

    for operation in list_operations:
        if operation == {}:
            continue
        elif operation['state'] == 'EXECUTED':
            executed_operations.append(operation)

    return executed_operations


def sort_by_date(list_operations, count_operations):
    sorted_operations = sorted(list_operations, reverse=False, key=lambda operation: operation['date'])

    return sorted_operations[-count_operations:]


def get_output_data(operation):
    date = datetime.datetime.fromisoformat(operation['date'])
    date_data = date.strftime("%d.%m.%Y")

    description = operation['description']

    if operation.get('from') is None:
        from_where = 'Данных нет'
    elif operation['from'].lower().startswith('счет'):
        account_list = operation['from'].split()
        account = '*' * 2 + account_list[1][-4:]
        from_where = account_list[0] + ' ' + account
    else:
        account_list = operation["from"].split()
        card_number = account_list[-1]
        private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
        slice_private_number = [private_number[i:i + 4] for i in range(0, len(private_number), 4)]
        str_slice_private_number = ' '.join(slice_private_number)
        if len(account_list) >= 3:
            from_where = account_list[0] + ' ' + account_list[1] + ' ' + str_slice_private_number
        else:
            from_where = account_list[0] + ' ' + str_slice_private_number

    to_account_list = operation['to'].split()
    to_account = '*' * 2 + to_account_list[1][-4:]
    to_where = to_account_list[0] + ' ' + to_account

    operation_amount = operation['operationAmount']['amount']
    operation_currency_name = operation['operationAmount']["currency"]["name"]

    return f'{date_data} {description}\n' \
           f'{from_where} -> {to_where}\n' \
           f'{operation_amount} {operation_currency_name}\n'
