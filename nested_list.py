# CPE 101-01
# LAB 7
# Name: Tyler Baxter
# Section: 03

# The groups_of_3 function takes a list of values as its only argument. This function will group the
# elements of the input list into groups of three.
def group_of_3(l1: list) -> list:
    l2 = [[]]
    location = 0
    for i in range(0, len(l1), 1):
        if i % 3 == 0 and i != 0:
            location += 1
            l2.append([])
        l2[location].append(l1[i])
    if l2 == [[]]:
        l2 = []
    return l2


# Return a list that contains only the final element of each inner list from the given list. If an inner
# list is empty, it has no corresponding integer in the output list.
def final_value(l1: list) -> list:
    l2 = []
    for i in range(0, len(l1), 1):
        for j in range(0, len(l1[i])):
            if j == (len(l1[i]) - 1):
                l2.append(l1[i][j])
    return l2


# Return a 2D list of integers such that each inner list repeats the corresponding integer in the original
# list that number of times. Assume all integers are non-negative.
def repeat_value(l1: list) -> list:
    l2 = []
    for i in range(0, len(l1), 1):
        if l1[i] == 0:
            l2.append([])
        else:
            l2.append([l1[i]])
        for j in range(0, l1[i] - 1, 1):
            l2[i].append(l1[i])
    return l2
