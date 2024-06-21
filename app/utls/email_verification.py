from email_validator import validate_email, EmailNotValidError


def validate_email_with_lib(email):
    """
    邮箱验证
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False
