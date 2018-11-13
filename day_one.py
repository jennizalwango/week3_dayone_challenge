#in this l have used conditions,datatypes,inputs and output
def get_age_bracket(year_of_birth): 
    age = 2018 - year_of_birth
    if age < 0:
        return('invalid age')
    elif age < 18:
        return('you are a minor')
    elif age < 36:
        return('you are a youth')
    elif age > 37:
        return('you are an elder')

year_of_birth = int(input('enter the year you were born:\n'))
result = get_age_bracket(year_of_birth)
print(result)

  
   

#for dictionaries
