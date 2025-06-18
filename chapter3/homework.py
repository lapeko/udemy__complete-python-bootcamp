# Task 1
def vol(rad):
    pi = 3.14
    return 4 / 3 * pi * rad ** 3

result = vol(2)
expectation = 33.49333333333333
if not result == expectation:
    print("Result is {} when expected {}".format(result, expectation))
else:
    print("Ok")


# Task 2
def up_low(s):
    lower_count = sum(1 for c in s if c.islower())
    upper_count = sum(1 for c in s if c.isupper())
    return {"lower": lower_count, "upper": upper_count }

tests = [
    {"text": "Hello Mr. Rogers, how are you this fine Tuesday?", "expectation": {"lower": 33, "upper": 4}},
]
for test in tests:
    result = up_low(test["text"])
    if result != test["expectation"]:
        print("Result is {} when expected {}".format(result, test["expectation"]))
    else:
        print("Ok")