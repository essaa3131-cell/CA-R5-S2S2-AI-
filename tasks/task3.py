my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,)

numbers = [5, 10, 15, 20]
total_sum = sum(numbers)

product = 1
for num in [2, 3, 4]:
    product *= num

nums = [10, 3, 25, 1, 7]
min_val = min(nums)
max_val = max(nums)

words = ["hi", "a", "hello", "no", "on"]
count_long = sum(1 for w in words if len(w) >= 2)

original = [1, 2, 3, 4]
copied_list = original.copy()

my_set = {1, 2, 3, 4, 5}
my_set.discard(3)

set1 = {1, 2}
set2 = {1, 2, 3, 4}
is_sub = set1.issubset(set2)

my_set.clear()

sample_set = {10, 3, 25, 1, 7}
s_max, s_min = max(sample_set), min(sample_set)

tup = (10, 20, 30, 40)
idx = tup.index(30)

tuple_pairs = (("a", 1), ("b", 2), ("c", 3))
dict_from_tup = dict(tuple_pairs)

pairs = [(1, 2), (3, 4), (5, 6)]
l1, l2 = list(zip(*pairs))

rev_tuple = tup[::-1]

list_tuples = [("a", 1), ("b", 2), ("c", 3)]
dict_from_list = dict(list_tuples)

data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_data = [t[:-1] + (100,) for t in data]

items = (("item1", 10.5), ("item2", 5.7), ("item3", 8.9))
sorted_items = tuple(sorted(items, key=lambda x: x[1]))

word_list = ["hi", "hello", "fantastic", "world"]
longest = max(word_list, key=len)

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged_dict = {**d1, **d2}

scores = {
    "student1": {"math": 80, "science": 90},
    "student2": {"math": 75, "science": 85},
    "student3": {"math": 92, "science": 88},
}
total_score = sum(
    s for student in scores.values() for s in student.values()
)

print("Task 3 Completed Successfully!")