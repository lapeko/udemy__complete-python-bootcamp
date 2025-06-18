#  def singleNumber(nums):
#    nums_count = {}
#    for n in nums:
#      nums_count[n] = nums_count.get(n, 0) + 1
#    for key, count in nums_count.items():
#      if count == 1:
#        return key

def single_number(nums):
  result = 0
  for num in nums:
    result ^= num
  return result

tests = [
  {"array": [2, 1, 2, 3, 3], "expected": 1},
  {"array": [2, 1, 2, 3, 3], "expected": 1},
  {"array": [2, 1, 2, 3, 3], "expected": 1},
]

for t in tests:
  res = single_number(t["array"])
  if res != t["expected"]:
    print(f"Err: Expected {t["expected"]}, received: {res}")
  else:
    print("Ok")
