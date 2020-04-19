def validate_user_create(data):
    '''Validate the data for a User create operation'''

    return validate_password(data)


def validate_password(data):
    '''Validate the password'''

    password = data.get('password')
    password2 = data.get('password2')
    if password and password != password2:
        return False
    return True
