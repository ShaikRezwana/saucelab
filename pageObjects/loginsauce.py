class LoginSauce:
    textbox_username_id="user-name"
    textbox_password_id="password"
    button_login_id="login-button"
    options_xpath = ".//*[@id='react-burger-menu-btn']"
    link_logout_xpath=".//*[@id='logout_sidebar_link']"

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element("id",self.textbox_username_id).clear()
        self.driver.find_element("id", self.textbox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element("id",self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element("id",self.button_login_id).click()


    def click_options(self):
        self.driver.find_element("xpath",self.options_xpath).click()

    def click_logout(self):
        self.driver.find_element("xpath",self.link_logout_xpath).click()

