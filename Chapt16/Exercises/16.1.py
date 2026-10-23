def longest_increasing_run(s: str) -> str:
    if not s:
        return ""
    best_start, best_len = 0, 1
    run_start = 0
    for i in range(1, len(s)):
        if s[i] <= s[i - 1]:
            run_start = i
        run_len = i - run_start + 1
        if run_len > best_len:
            best_start, best_len = run_start, run_len
    return s[best_start: best_start + best_len]

def main():
    text = input("Enter a string: ").strip()
    if not text:
        print("Please enter a non-empty string.")
        return
    print(f"Maximum consecutive substring is {longest_increasing_run(text)}")


main()
