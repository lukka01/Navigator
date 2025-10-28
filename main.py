import os
import random


#პირველი დავალება
def build_structure(root_dir):
    structure = {}

    for dirpath, dirnames, filenames in os.walk(root_dir):

        relative_path = os.path.relpath(dirpath, root_dir)
        if relative_path == ".":
            relative_path = root_dir

        structure[relative_path] = {
            "dirs": dirnames,
            "files": filenames
        }

    return structure



root_directory = "./data"
result = build_structure(root_directory)


for path, content in result.items():
    print(f"{path}:")
    print(f"  Directories: {content['dirs']}")
    print(f"  Files: {content['files']}")
    print()

#მეორე დავალება

def build_file_data_structure(root_dir):
    structure = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        relative_path = os.path.relpath(dirpath, root_dir)
        if relative_path == ".":
            continue
        parts = relative_path.split(os.sep)
        if filenames:
            key = tuple(parts[:-1]) if len(parts) > 1 else (root_dir,)
            file_info = {}
            for filename in filenames:
                name_without_ext = os.path.splitext(filename)[0]
                file_info[(parts[-1], name_without_ext)] = [
                    str(random.randint(100000000, 999999999)) for _ in range(9)
                ]
            structure[key] = file_info
    return structure

root_directory = "./data"
result = build_file_data_structure(root_directory)

from pprint import pprint
pprint(result)

 # დავალება 3

def element_exists(structure, value):
    for group in structure.values():
        for numbers in group.values():
            if str(value) in numbers:
                return True
    return False

print(element_exists(result, 123456789))  # example usage

# დავალება 4

def all_even_digits(num_list):
    for n in num_list:
        for digit in str(n):
            if int(digit) % 2 != 0:
                return False
    return True

print(all_even_digits(['2468', '222444666']))  # example usage
print(all_even_digits(['123456']))  # example usage


# დავალება 5

def count_files_with_all_even_numbers(structure):
    count = 0
    for group in structure.values():
        for file_tuple, numbers in group.items():
            if any(all_even_digits([num]) for num in numbers):
                count += 1
    return count

print(count_files_with_all_even_numbers(result))

# ბონუს დავალება

def process_dictionary(data: dict, outer_key=None, inner_key=None, condition=None):



    if outer_key is None or outer_key not in data:
        print("გარე გასაღები არ არსბობს ან არაა მითითებული.")
        return None

    selected = data[outer_key]

    # 2. თუ მნიშვნელობა არის ლექსიკონი
    if isinstance(selected, dict):
        if inner_key is None or inner_key not in selected:
            print("შიდა გასაღები არ არსებობს ან არ არის მითითებული.")
            return None
        selected = selected[inner_key]

    # 3. თუ მოცემულია პირობა
    if condition is not None:
        selected = [x for x in selected if condition(x)]

    # თუ შედეგი ცარიელია
    if not selected:
        print("დასამუშავებელი ელემენტები ვერ მოიძებნა.")
        return None

    # 4. საშუალო არითმეტიკული
    return sum(selected) / len(selected)




#  ერთგანზომილებიანი ლექსიკონი
simple_dict = {
    "numbers": [10, 13, 23, 33, 42, 53, 60]
}

result1 = process_dictionary(
    data=simple_dict,
    outer_key="numbers",
    condition=lambda x: str(x).endswith("3")
)
print("3-ით დაბოლოვებული რიცხვების საშუალო არითმეტიკული:", result1)


# ტესტი II — ორგანზომილებიანი ლექსიკონი
nested_dict = {
    "set1": {
        "a": [10, 20, 30, 40],
        "b": [5, 15, 25, 35]
    },
    "set2": {
        "x": [100, 200, 300],
        "y": [150, 250, 350]
    }
}

result2 = process_dictionary(
    data=nested_dict,
    outer_key="set2",
    inner_key="y"
)
print("set2['y'] ელემენტების საშუალო არითმეტიკული:", result2)

