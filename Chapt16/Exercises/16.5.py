def longest_same_run(nums: list[int]) -> tuple[int, int, int]:
    if not nums:
        return (0, 0, 0)
    best_start, best_len = 0, 0
    run_start = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            run_start = i
        run_len = i - run_start + 1
        if run_len > best_len:
            best_start, best_len = run_start, run_len
    return (best_start, best_len, nums[best_start])

def main():
    num = [eval(x) for x in input("Enter a series of numbers ending with 0: ").split()]
    index, length, val = longest_same_run(num)
    print(f"The longest same number sequence starts at index {index} with {length} values of {val}")
main()
