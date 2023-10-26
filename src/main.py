from src.functions import get_operations, get_executed_operations, sort_by_date, get_output_data
from pathlib import Path

# count_last_operation = int(input())
count_last_operation = 5

operations_filepath = Path(__file__).parent.joinpath("operations.json")
all_operations = get_operations(operations_filepath)
filtered_operations = get_executed_operations(all_operations)
sorted_operations = sort_by_date(filtered_operations, count_last_operation)

for operation in sorted_operations:
    print(get_output_data(operation), end='\n\n')
