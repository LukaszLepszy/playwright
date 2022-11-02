class LoginLocators:
    USERNAME_INPUT = "input[id='user-name'][placeholder='Username']"
    PASSWORD_INPUT = "input[id='password'][placeholder='Password']"
    LOGIN_BUTTON = "input[id='login-button']"
    PRODUCTS_TITTLE = "div[class='header_secondary_container'] span[class='title']"
    ERROR_MESSAGE = "div[class='error-message-container error']"
    ERROR_ICON_USERNAME = "#login_button_container > div > form > div:nth-child(1) > svg"
    ERROR_ICON_PASSWORD = "#login_button_container > div > form > div:nth-child(2) > svg"