# match-case (switch-case) = An alternative to using many "elif" statements
#                            Execute some code if a value matches a 'case

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _ :
            return "Not a Day"
        
print(is_weekend("Thursday"))