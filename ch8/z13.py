def build_profile(first, last, **user_info):
    """build dic with user inf"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Ilya', 'Koznov',
                             sex = 'male',
                             having_sex = 'no'
                             )
print(user_profile)
