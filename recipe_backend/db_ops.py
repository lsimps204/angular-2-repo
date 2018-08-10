""" Database functions from Oracle and PostgreSQL mapped (roughly) to Python """
import datetime

# 1. NVL (Oracle)
# Returns first argument if it's not null, otherwise returns second argument.
# Ex: start_date := NVL(hire_date, SYSDATE)
# Postgres equivalent: coalesce(hire_date, SYSDATE)
def nvl(hire_date=None):
    return hire_date if hire_date else return datetime.datetime.now()

# 2. NVL2 (Oracle)
# If first argument is valid, returns second argument. Otherwise, if the first argument is invalid, it returns third argument.
# Ex: yearly_income := NVL2(got_bonus, salary + bonus, salary)
def nvl2():
    BONUS = 10
    employee = Employee.objects.first() # Fake employee
    if employee.got_bonus: return employee.salary + BONUS
    else: return employee.salary

# 3. Coalesce (Oracle + PSQL)
# Returns first non-null expression in the list. Returns null if all expressions are null
# Coalesce (expr1, expr2) is equivalent to:
# `CASE WHEN expr1 IS NOT NULL expr1 ELSE expr2 END``
def coalesce(x,y,z):
    return x if x is not None \
    else y if y is not None \
    else z

# 4. Decode (Oracle)
# Has minimum of 3 params. The first parameter is the relevant field to compare
# The second parameter is the search-value, and the third parameter is the value to return
# Params 2 and 3 are repeated for however many potential lookups there are.
# A default can be provided if all fail.
# This construct exists in Postgres as `CASE WHEN x THEN y ELSE .... ELSE z END`
# DECODE(genre_id, 1, 'indie', 2, 'jazz', 3, 'hip-hop')
def decode(*args, default=None):
    if len(args) < 3 or not (len(args) % 2 == 1):
        raise TypeError("Invalid number of arguments. Did El Bear bloody call this function?!")
    field = args[0] # field to search on
    for search_term, result in zip(args[1::2], args[2::2]):
        if search_term == field:
            return result
    return default
