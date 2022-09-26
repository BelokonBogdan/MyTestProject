class StartPageConstants:
    # Sing in
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_FIELD_XPATH = ".//button[text()='Sign In']"
    SIGN_IN_LOGIN_ERROR_FIELD_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_LOGIN_ERROR_FIELD_TEXT = "Invalid username / pasword"

    # Sing up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_FIELD_XPATH = ".//button[text()='Sign up for OurApp']"

    HELLO_MASSAGE_XPATH = ".//h2"
    HELLO_MASSAGE_USERNAME_XPATH = ".//strong"
    HELLO_MASSAGE_TEXT = "Hello {username}, your feed is empty."
