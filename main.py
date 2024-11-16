country_code={'India' : '0091',
              'Australia' : '0025', 
              'Nepal' : '00977','Nigeria':'0234'}
print("country code for Nigeria:")
print(country_code.get('Nigeria','Not found'))
print("country code for France:")
print(country_code.get('France','Not found'))