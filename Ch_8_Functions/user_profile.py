''' 
Using Arbitrary Keyword Arguments
p 152
''' 

def build_profile(first, last, **user_info):
    ''' Build a dictionary containing everything we know about a user. '''
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location= 'princeton', field= 'physics')

print(user_profile)

