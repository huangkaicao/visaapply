from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def save_and_continue():
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton2").click()

    driver.find_element(By.ID, "ctl00_btnContinueApp").click()

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def DOB_input(DAYid,DAYtext,MONTHid,MONTHtext,YEARid,YEARtext):
    Birth_Day=driver.find_element(By.ID, DAYid)
    dropdown_Birth_Day = Select(Birth_Day)
    dropdown_Birth_Day.select_by_visible_text(DAYtext)

    Birth_Month=driver.find_element(By.ID, MONTHid)
    dropdown_Birth_Month = Select(Birth_Month)
    dropdown_Birth_Month.select_by_visible_text(MONTHtext)

    driver.find_element(By.ID, YEARid).send_keys(YEARtext)

def no_selected(myclass):
    info_div = driver.find_element(By.CLASS_NAME,myclass)

    no_buttons = info_div.find_elements(By.XPATH,".//input[@type='radio' and @value='N']")

    for button in no_buttons:
        button.click()

def sel_allchkbox(myclass):
    info_div = driver.find_element(By.CLASS_NAME,myclass)

    chkbox_all = info_div.find_elements(By.XPATH,".//input[@type='checkbox']")

    for checkbox in chkbox_all:
        if not checkbox.is_selected():
            checkbox.click()

def dropdown_process(id,text):
    ele=driver.find_element(By.ID, id)

    dropdown_ele = Select(ele)

    dropdown_ele.select_by_visible_text(text)

def Explicit_Wait_func(element_to_wait_for_id):
    wait = WebDriverWait(driver, 10)

    ele=wait.until(EC.visibility_of_element_located((By.ID, element_to_wait_for_id)))

    if ele.get_attribute("type") == "text":
        wait.until(EC.element_to_be_clickable((By.ID, element_to_wait_for_id)))

def first_page():
    driver.get("https://ceac.state.gov/genniv/")

    dropdown_process("ctl00_SiteContentPlaceHolder_ucLocation_ddlLocation","CHINA, BEIJING")

    input("验证码识别功能敬请期待，目前请手动在浏览器中输入验证码后，在terminal按回车键继续...")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_newApplication").click()

def second_page():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_lblBarcode")

    Application_ID_Element=driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_lblBarcode")
    Application_ID=Application_ID_Element.text
    print("请记下您的申请ID：", Application_ID)

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_chkbxPrivacyAct").click()

    dropdown_process("ctl00_SiteContentPlaceHolder_ddlQuestions","What is the given name of your father's father?")

    ANS="JACK"
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_txtAnswer").send_keys(ANS)
    print("请记下您的密保问题答案：", ANS)

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_btnContinue").click()

def personal_one():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SURNAME")

    sel_allchkbox("fieldset-group")

    SURNAME="ZHANG"
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SURNAME").send_keys(SURNAME)
    print("请记下您填写的SURNAME：", SURNAME)

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_GIVEN_NAME").send_keys("SAN")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblOtherNames_1").click()

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblTelecodeQuestion_1").click()

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_GENDER","MALE")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_MARITAL_STATUS","SINGLE")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlDOBDay","01")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlDOBMonth","JAN")

    DOBYear="1990"
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxDOBYear").send_keys(DOBYear)
    print("请记下您填写的出生年份：", DOBYear)

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_POB_CITY").send_keys("BEIJING")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_POB_CNTRY","CHINA")

    save_and_continue()

def personal_two():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_NATL")

    no_selected("fieldset-group")

    sel_allchkbox("fieldset-group")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_NATL","CHINA")

    save_and_continue()

def travel():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_dlPrincipalAppTravel_ctl00_ddlPurposeOfTrip")

    no_selected("fieldset-group")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_dlPrincipalAppTravel_ctl00_ddlPurposeOfTrip","TEMP. BUSINESS PLEASURE VISITOR (B)")

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_dlPrincipalAppTravel_ctl00_ddlOtherPurpose")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_dlPrincipalAppTravel_ctl00_ddlOtherPurpose","BUSINESS & TOURISM (TEMPORARY VISITOR) (B1/B2)")

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_ddlTRAVEL_DTEDay")

    Travel_Day="ctl00_SiteContentPlaceHolder_FormView1_ddlTRAVEL_DTEDay"
    Travel_Month="ctl00_SiteContentPlaceHolder_FormView1_ddlTRAVEL_DTEMonth"
    Travel_Year="ctl00_SiteContentPlaceHolder_FormView1_tbxTRAVEL_DTEYear"
    DOB_input(Travel_Day,"01",Travel_Month,"JAN",Travel_Year,"2025")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxTRAVEL_LOS").send_keys("1")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlTRAVEL_LOS_CD","Week(s)")

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_tbxStreetAddress1")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxStreetAddress1").send_keys("1250 1ST AVE")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxCity").send_keys("SEATTLE")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlTravelState","WASHINGTON")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbZIPCode").send_keys("98123")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlWhoIsPaying","Self")

    save_and_continue()

def travel_companions():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_lblOtherPersonsTravelingWithYou")

    no_selected("fieldset-group")

    save_and_continue()

def previous_travel():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_lblPREV_US_TRAVEL_IND")
    
    no_selected("fieldset-group")

    save_and_continue()

def address_and_phone():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_LN1")

    sel_allchkbox("fieldset-group")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_LN1").send_keys("1 Guangcai Rd, Fengtai District")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_CITY").send_keys("BEIJING")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlCountry","CHINA")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblMailingAddrSame_0").click()

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_HOME_TEL").send_keys("15601235678")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblAddPhone_1").click()

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_EMAIL_ADDR").send_keys("123456789@qq.com")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblAddEmail_1").click()

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_dtlSocial_ctl00_ddlSocialMedia","QZONE (QQ)")

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_dtlSocial_ctl00_tbxSocialMediaIdent")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_dtlSocial_ctl00_tbxSocialMediaIdent").send_keys("123456789")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblAddSocial_1").click()

    save_and_continue()

def passport_info():
    driver.implicitly_wait(Pause_Time)

    sel_allchkbox("fieldset-group")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblLOST_PPT_IND_1").click()

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlPPT_TYPE","REGULAR")

    driver.implicitly_wait(Pause_Time)
    
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxPPT_NUM").send_keys("F57412589")

    driver.implicitly_wait(Pause_Time)

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlPPT_ISSUED_CNTRY","CHINA")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxPPT_ISSUED_IN_CITY").send_keys("BEIJING")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxPPT_ISSUED_IN_STATE").send_keys("BEIJING")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlPPT_ISSUED_IN_CNTRY","CHINA")

    Issued_Day="ctl00_SiteContentPlaceHolder_FormView1_ddlPPT_ISSUED_DTEDay"
    Issued_Month="ctl00_SiteContentPlaceHolder_FormView1_ddlPPT_ISSUED_DTEMonth"
    Issued_Year="ctl00_SiteContentPlaceHolder_FormView1_tbxPPT_ISSUEDYear"
    DOB_input(Issued_Day,"02",Issued_Month,"JAN",Issued_Year,"2020")

    save_and_continue()

def contract_info():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_cbxUS_POC_NAME_NA")

    Not_Know=driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_cbxUS_POC_NAME_NA")
    if not Not_Know.is_selected():
        Not_Know.click()

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_ORGANIZATION").send_keys("DEMOCRATIC")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlUS_POC_REL_TO_APP","OTHER")

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_ADDR_LN1")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_ADDR_LN1").send_keys("1250 1ST AVE")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_ADDR_CITY").send_keys("SEATTLE")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlUS_POC_ADDR_STATE","WASHINGTON")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_ADDR_POSTAL_CD").send_keys("98123")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_HOME_TEL").send_keys("4556134502")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_EMAIL_ADDR").send_keys("987654321@qq.com")

    save_and_continue()

def family_info():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_lblFATHER_SURNAME")

    sel_allchkbox("fieldset-group")

    no_selected("fieldset-group")

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_rblUS_OTHER_RELATIVE_IND_1")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblUS_OTHER_RELATIVE_IND_1").click()

    save_and_continue()

def present_work():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_ddlPresentOccupation")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlPresentOccupation","ENGINEERING")

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_tbxEmpSchName")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxEmpSchName").send_keys("PEKING UNIVERSITY")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxEmpSchAddr1").send_keys("1 Guangcai Rd, Fengtai District")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxEmpSchCity").send_keys("BEIJING")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxWORK_EDUC_ADDR_STATE").send_keys("BEIJING")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxWORK_EDUC_ADDR_POSTAL_CD").send_keys("100021")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxWORK_EDUC_TEL").send_keys("5678888")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlEmpSchCountry","CHINA")

    Start_Day="ctl00_SiteContentPlaceHolder_FormView1_ddlEmpDateFromDay"
    Start_Month="ctl00_SiteContentPlaceHolder_FormView1_ddlEmpDateFromMonth"
    Start_Year="ctl00_SiteContentPlaceHolder_FormView1_tbxEmpDateFromYear"
    DOB_input(Start_Day,"15",Start_Month,"MAR",Start_Year,"2010")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxCURR_MONTHLY_SALARY").send_keys("10000")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxDescribeDuties").send_keys("WORKING")

    save_and_continue()

def previous_work():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_lblPreviouslyEmployed")

    no_selected("fieldset-group")

    save_and_continue()
   
def additional_work():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_lblCLAN_TRIBE_IND")

    no_selected("fieldset-group")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_dtlLANGUAGES_ctl00_tbxLANGUAGE_NAME").send_keys("CHINESE")

    save_and_continue()

def security_check():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_Label5")

    no_selected("fieldset-group")

    save_and_continue()

def photo_uploaded():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_btnUploadPhoto")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_btnUploadPhoto").click()

    Explicit_Wait_func("ctl00_cphMain_imageFileUpload")

    upload_button = driver.find_element(By.ID,"ctl00_cphMain_imageFileUpload")
    upload_button.send_keys(image_path)

    driver.find_element(By.ID, "ctl00_cphButtons_btnUpload").click()

    Explicit_Wait_func("ctl00_cphButtons_btnContinue")

    driver.find_element(By.ID, "ctl00_cphButtons_btnContinue").click()

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_btnUploadPhoto")

    save_and_continue()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
script_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_directory, "testphoto", "testphoto.JPEG")

driver = webdriver.Chrome(options=chrome_options)
Pause_Time=2
security_check_count=0

first_page()
second_page()
personal_one()
personal_two()
travel()
travel_companions()
previous_travel()
address_and_phone()
passport_info()
contract_info()
family_info()
present_work()
previous_work()
additional_work()
while(security_check_count<5):
    security_check()
    security_check_count+=1
photo_uploaded()

print("自动填表已完成，请在后续步骤中仔细核对所填信息，如有不对，请手动修改，祝您签证通过，旅途愉快")