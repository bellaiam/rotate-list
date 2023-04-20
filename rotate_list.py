
  # Handle list is length 0 and shift_by is divisible by the length
  # Modulus might help w/ the wrappign around
  #  create an empty new list
  # Idea: move each element over to an index that is offset by the shift_y input. also need to know the length of the liist
  # use a temporary variable to hold the current value being moved
  #  if the shift_by + the current index is > length, do smth to wrap around
  # dictionary where
  #  deep copy the list
  # move the last thing into the first index
  # append all the rest of the things to that list
  # figure out how to do it with shift_by
# def rotate_list(list, shift_by): 
#   if not isinstance(shift_by, int):
#         return None
#   if len(list) == 0 or shift_by % len(list) == 0:
#     return list
  
#   shift_by = shift_by % len(list)

#   new_list = []

#   for i, item in enumerate(list):
#     new_index = (i + shift_by) % len(list)
#     new_list.insert(new_index, item)

#   return new_list



# def rotate_list(lst, shift_by):
#     if not isinstance(shift_by, int):
#         return None
#     if len(lst) == 0 or shift_by % len(lst) == 0:
#         return lst
#     shift_by = shift_by % len(lst)
#     rotated = [lst[(i - shift_by) % len(lst)] for i in range(len(lst))]
#     return rotated

def rotate_list(lst, shift_by):
    if not isinstance(shift_by, int):
        return None
    if len(lst) == 0:
        return lst
    shift_by = shift_by % len(lst)
    if shift_by == 0:
        return lst
    rotated = lst[-shift_by:] + lst[:-shift_by]
    return rotated

'''
Clarifying questions:
- What if list does not contain integers? still rotate
- what if the list's empty? return []
- Can we use slicing? Yes, but not for hard mode
- What if shift_by is greater than the length of the list?
- Is list sorted
- Size constraint on the lenght of the list?
- Are the items on the list unique? not necessary
if the shift_by not number? return non or raise
What if shift_by is less than zero?
call that an extension and do it later
'''
# test cases
assert rotate_list([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
assert rotate_list([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
assert rotate_list([1, 2, 3, 4, 5], 6) == [5, 1, 2, 3, 4]

assert rotate_list(["cat", 2, "code"], 2) == [2, "code", "cat"]
assert rotate_list([], 4) == []

# ONLY FOR IN-PLACE
# the_list = [3, 4, 5]
# assert rotate_list(the_list, 1) is the_list

assert rotate_list([4, 6], "Not a number") is None

#
# assert
print('Tests pass!')
