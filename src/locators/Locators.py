from selenium.webdriver.common.by import By


class Locators:
    # for loginPage
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.XPATH, "/html/body/div/div/div/div/div")
    ASAL_LOGO = (By.CSS_SELECTOR, "img[src*='Asal Technologies.svg']")
    AURORA_LOGO = (By.CSS_SELECTOR, "img[src*='Aurora.svg']")
    ORION_LOGO = (By.CSS_SELECTOR, "img[src*='Orion.svg']")

    # for the EvaluationPage
    CRITERIA_ROW_LOCATOR = (By.CSS_SELECTOR, "#assets-data-table tbody tr")
    RATING_DIVS_LOCATOR = (By.CSS_SELECTOR, "td div.checker")
    LIKE_TEXTAREA_LOCATOR = (By.ID, "Likes")
    DISLIKE_TEXTAREA_LOCATOR = (By.ID, "Dislikes")
    SUGGESTION_TEXTAREA_LOCATOR = (By.ID, "Improvements")

    STRENGTHS_TEXTAREA_LOCATOR = (By.ID, "Strengths")
    IMPROVEMENTS_TEXTAREA_LOCATOR = (By.ID, "Areas_of_improvements")

    SAVE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[id='saveButton']")
    SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[id='submitbtn']")
    SCROLL_TO_TOP_BUTTON_LOCATOR = (By.CSS_SELECTOR, "div.scroll-to-top")

    # for HomePage, MyTeamPage
    TITLE_OF_PAGE = (By.XPATH, "/html/body/div[3]/div[2]/div/h2/b")
    MY_EVALUATION_LINK = (By.CSS_SELECTOR, "a[href='/Employee/EvaluationView']")
    MY_EVALUATION_HISTORY = (By.CSS_SELECTOR, "a[href='/Employee/EvaluationHistory']")
    MY_TEAM_MENU_ITEM = (By.XPATH, "//a[@href='/Supervisor/getEmployees']")
