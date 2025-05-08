# Start with a copy of user_profile.py from page 153.
# Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""

    profile = {}
    profile['first_name'] = first.title().strip()
    profile['last_name'] = last.title().strip()

    for key, value in user_info.items():
        profile[key.title().strip()] = value.title().strip()
    print(profile)

build_profile('albert', 'einstein', location='princeton', field='physics')

build_profile('justice', 'kamwanja', location='Eldoret', field='software engineering')