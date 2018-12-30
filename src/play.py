# a = ["a", "b", "c", "d", "e"]
# b = ["a", "c", "b", "d", "e"]
#
# if len(a) == len(b):
#     for i in range(len(a)):
#         if a[i] == b[i]:
#             print(a[i], b[i])
#         else:
#             print("Err")


#https://www.geeksforgeeks.org/python-check-two-lists-least-one-element-common/
# def common_member(a, b):
#     a_set = set(a)
#     b_set = set(b)
#     if len(a_set.intersection(b_set)) >= 2:
#         return(True)
#     return(False)
#
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 7, 8, 9]
# print(common_member(a, b))


#continue statement to return control flow to the top of the loop
def common_data(list1, list2):
    match_cnt = 0

    for x in list1:
        for y in list2:
            if x == y:
                match_cnt += 1
                continue

    return match_cnt

a = [1, 2, 3]
b = [1, 2, 2]
print(common_data(a, b))