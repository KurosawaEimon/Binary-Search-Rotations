# the main function "find_num_rotations" counts the number of times a sorted list of integers has been rotated
# a single rotation refers to each number in the sequence shifting one place to the right,
# i.e the last number is moved to index 0: [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3] has been rotated 2 times.
#######################################################################################################################


# takes list of sorted numbers, shifted to right n times, and returns number of shifts/rotations.
def find_num_rotations(numbers):
    # generate initial start and end points
    start_pos = 0
    end_pos = len(numbers) - 1
    # if only one number in list, no solution exists
    if len(numbers) == 1:
        return []

    # start binary search
    while start_pos <= end_pos:
        check_pos = (start_pos + end_pos) // 2
        num_checked = numbers[check_pos]

        # find num to right and left of "num_checked"
        left_num, right_num = generate_left_right_nums(numbers, check_pos)

        # if either is equal to "num_checked", check for next different number in right/left direction
        if left_num == num_checked:
            left_num = find_different_num(numbers, check_pos-1, "left")
        if right_num == num_checked:
            right_num = find_different_num(numbers, check_pos+1, "right")

        # if all nums in both directions are equal: return [] as no solution exists
        if left_num == "equal to" and right_num == "equal to":
            return []

        # if all nums to left are equal, search right side
        elif left_num == "equal to":
            start_pos = check_pos + 1
        # if all nums to right are equal: if num directly to left is greater => first min number found, else check left side
        elif right_num == "equal to":
            if left_num > num_checked:
                return check_pos
            else:
                end_pos = check_pos - 1

        # if number to right and left of num_checked is bigger, min num found so return index
        elif left_num > num_checked and right_num > num_checked:
            return check_pos
        # if number to right is smaller, search in that direction
        elif num_checked > right_num:
            start_pos = check_pos + 1
        # if number to left is smaller, search in that direction
        elif num_checked > left_num:
            end_pos = check_pos - 1
    # if loop fails to return solution before termination, return empty list
    return []


# generate numbers directly left and right of current checked number
# inputs: "numbers"=list of numbers; "check_pos"=index of current number being checked
# outputs: "left_num"=value of num directly to left; "right_num"=value of num directly to right
def generate_left_right_nums(numbers, check_pos):
    if check_pos == 0:
        left_num = numbers[-1]
    else:
        left_num = numbers[check_pos - 1]
    if check_pos == len(numbers) - 1:
        right_num = numbers[0]
    else:
        right_num = numbers[check_pos + 1]
    return left_num, right_num


# Binary search through list to find next number that is different to current checked number
# inputs: "numbers" is list of numbers, "pos_same_num" is index of number being checked, "direction" is left/right
# output: if different number found return it as new left/right_num, else return "equal to"
def find_different_num(numbers, pos_same_num, direction):

    # store value of original number to check
    test_number = numbers[pos_same_num]

    # generate start_pos,end_pos based on "direction"
    if direction == "right":
        start_pos = pos_same_num + 1
        end_pos = len(numbers) - 1
    elif direction == "left":
        start_pos = 0
        end_pos = pos_same_num - 1

    # start binary search
    while start_pos <= end_pos:
        check_pos = (start_pos + end_pos) // 2
        num_checked = numbers[check_pos]

        # if current checked num is equal to test_num, move search towards "direction"
        if num_checked == test_number and direction == "left":
            end_pos = check_pos - 1
        elif num_checked == test_number and direction == "right":
            start_pos = check_pos + 1

        # if current checked num is not equal:
        elif num_checked != test_number:
            if direction == "left":
                # if num to right is test_num, num_checked is next number to left
                if numbers[check_pos+1] == test_number:
                    return num_checked
                # else gone too far so move search back to right
                else:
                    start_pos = check_pos + 1
            elif direction == "right":
                # similarly for right direction
                if numbers[check_pos-1] == test_number:
                    return num_checked
                else:
                    end_pos = check_pos - 1
    return "equal to"


tests = []

tests.append({
    'input': [],
    'output': []
})

tests.append({
    'input': [4, 5, 1, 2, 3],
    'output': 2
})

tests.append({
    'input': [31, 28, 26, 20, 19, 17, 15, 1, 2, 3, 5, 6, 7, 8, 9, 10, 13],
    'output': 7
})

tests.append({
    'input': [31, 31, 31, 20, 19, 19, 19, 19, 17, 15, 15, 1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9, 10, 10, 13],
    'output': 11
})

tests.append({
    'input': [1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1],
    'output': 9
})

tests.append({
    'input': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'output': []
})

tests.append({
    'input': [5, 4, 3, 2, 1, 1],
    'output': 4
})

tests.append({
    'input': [1],
    'output': []
})


for test in tests:
    ans = find_num_rotations(test['input'])
    if ans == test['output']:
        print("PASSED")
    else:
        print("FAILED")
        print(f"func output: {ans}", f"correct ans: {test['output']}")
    print()