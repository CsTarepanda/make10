#!/usr/bin/python3
import itertools

ops = ["+", "-", "*", "/"]
nums = input().split()
length = len(nums) - 1
patterns = range(length)


class Value:
    def __init__(self, *fom):
        self.fom = fom

    def __str__(self):
        return "(%s)" % " ".join(map(str, self.fom))


def formula(ops, nums, patterns):
    ops = list(ops)
    nums = list(nums)
    patterns = list(patterns)
    while patterns:
        target = min(patterns)
        index = patterns.index(target)
        value = Value(nums[index], ops[index], nums[index + 1])
        nums.pop(index)
        nums[index] = value

        ops.pop(index)
        patterns.pop(index)
    return str(nums[0])


result = []
for n in itertools.permutations(nums):
    for o in itertools.product(ops, repeat=length):
        for p in itertools.permutations(patterns, length):
            f = formula(o, n, p)
            if f in result: continue
            try:
                v = eval(f)
            except ZeroDivisionError: continue 
            if v != 10: continue
            result.append(f)
            print("%s = %s" % (f, v))
