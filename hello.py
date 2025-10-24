#mock up data for testing
# cards = [1, 3, 5, 7, 9, 11, 13, 15]
#cards with order descending
# cards = [15, 13, 11, 9, 7, 5, 3, 1]
# query = 7

# def locate_card(cards, query):
#     low, high = 0, len(cards) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         mid_number = cards[mid]
#         print(f"low: {low}, high: {high}, mid: {mid}, mid_number: {mid_number}")
#         if mid_number == query:
#             return mid
#         elif mid_number < query:
#             low = mid + 1
#         elif mid_number > query:
#             high = mid - 1
#     return -1

# def is_leap(year):
#     leap = False
#     # Write your logic here
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False
#     return leap
        

# year = int(input())
# print(is_leap(year))

