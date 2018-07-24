def merge_ranges(list):
    # sort the list
    if len(list) == 0 or len(list) == 1:
        return list

    # Sort list
    list.sort(key=lambda ranges: ranges[0])

    # Loop through list
    i = 0
    while i < (len(list) - 1):
        # if we can merge the next two
        if len(list) == 1:
            return list
        if list[i][1] >= list[i+1][0]:
             # merge
             list[i+1] = (list[i][0], list[i+1][1])
             del list[i]
             continue
        i += 1

    # continue
    return list


# (0,1), (2,3)

# Simplest version of the problem
# IN - [(0,1)]
# OUT - [(0,1)]

# problem V2 -> Multiple meetings no overlap
# IN - [(0, 2), (3, 4)]
# OUT - [(0, 2), (3, 4)]

# problem V3 -> Multiple meetings w/ overlap
# IN - [(0, 2), (1, 3)]
# OUT - [(0, 3)]

# problem V4 -> Multiple meetings w/ overlap
# IN - [(0, 2), (1, 3), (2, 4)]
# OUT - [(0, 4)]

# problem V5 -> Multiple meetings w/ and w/o overlap
# IN - [(0, 2), (5, 6), (1, 3), (2, 4)]
# OUT - [(0, 4), (5, 6)]

# Pattern
# It is easier to solve if sorted goes from n^2 to nlog(n)
# If this.end_time is >= other.start_time
# merge by creating tuple (this.start_time, other.end_time)
# Else leave alone
