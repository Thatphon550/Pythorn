def reverse_display(value):
    reverse_display_helper(value, len(value) - 1)

def reverse_display_helper(s, high):
    print(s[high], end = "")
    if high == 0:
        return
    reverse_display_helper(s, high - 1)

reverse_display("abcd")
