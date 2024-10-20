# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

#match-case variant:

def is_weeekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _: #instead if "else", use case _ which is the wild card.
            return False

print(is_weeekend("Pizza"))


# def day_of_week(day):
#     if day == 1:
#         return "It is Sunday"
#     elif day == 2:
#         return "It is Monday"
#     elif day == 3:
#         return "It is Tuesday"
#     elif day == 4:
#         return "It is Wednesday"
#     elif day == 5:
#         return "It is Thursday"
#     elif day == 6:
#         return "It is Friday"
#     elif day == 7:
#         return "It is Saturday"
#     else:
#         return "Not a valid day"
    
# print(day_of_week(1))