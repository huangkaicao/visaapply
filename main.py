from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

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
    first_page = data_filled["first_page"]

    driver.get("https://ceac.state.gov/genniv/")

    dropdown_process("ctl00_SiteContentPlaceHolder_ucLocation_ddlLocation",first_page["location"])

    input("验证码识别功能敬请期待，目前请手动在浏览器中输入验证码后，在terminal按回车键继续...")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_newApplication").click()

def second_page():
    second_page = data_filled["second_page"]

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_lblBarcode")

    Application_ID_Element=driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_lblBarcode")
    Application_ID=Application_ID_Element.text
    print("请记下您的申请ID：", Application_ID)

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_chkbxPrivacyAct").click()

    dropdown_process("ctl00_SiteContentPlaceHolder_ddlQuestions",second_page["security_question"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_txtAnswer").send_keys(second_page["security_answer"])
    print("请记下您的密保问题答案：", second_page["security_answer"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_btnContinue").click()

def personal_one():
    personal_one = data_filled["personal_one"]

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SURNAME")

    sel_allchkbox("fieldset-group")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SURNAME").send_keys(personal_one['surname'])
    print("请记下您填写的SURNAME：", personal_one['surname'])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_GIVEN_NAME").send_keys(personal_one['given_name'])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblOtherNames_1").click()

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblTelecodeQuestion_1").click()

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_GENDER",personal_one['gender'])

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_MARITAL_STATUS",personal_one['marital_status'])

    DOB_Day_id="ctl00_SiteContentPlaceHolder_FormView1_ddlDOBDay"
    DOB_Month_id="ctl00_SiteContentPlaceHolder_FormView1_ddlDOBMonth"
    DOB_Year_id="ctl00_SiteContentPlaceHolder_FormView1_tbxDOBYear"
    DOB_input(DOB_Day_id,personal_one['day'],DOB_Month_id,personal_one['month'],DOB_Year_id,personal_one['year'])
    print("请记下您填写的出生年份：", personal_one['year'])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_POB_CITY").send_keys(personal_one['city'])

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_POB_CNTRY",personal_one['country'])

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def personal_two():
    personal_two = data_filled["personal_two"]

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_NATL")

    no_selected("fieldset-group")

    sel_allchkbox("fieldset-group")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_NATL",personal_two['country'])

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def travel():
    travel = data_filled["travel"]

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_dlPrincipalAppTravel_ctl00_ddlPurposeOfTrip")

    no_selected("fieldset-group")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_dlPrincipalAppTravel_ctl00_ddlPurposeOfTrip",travel['purpose_of_trip'])

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_dlPrincipalAppTravel_ctl00_ddlOtherPurpose")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_dlPrincipalAppTravel_ctl00_ddlOtherPurpose",travel['specify'])

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_ddlTRAVEL_DTEDay")

    Travel_Day="ctl00_SiteContentPlaceHolder_FormView1_ddlTRAVEL_DTEDay"
    Travel_Month="ctl00_SiteContentPlaceHolder_FormView1_ddlTRAVEL_DTEMonth"
    Travel_Year="ctl00_SiteContentPlaceHolder_FormView1_tbxTRAVEL_DTEYear"
    DOB_input(Travel_Day,travel['day'],Travel_Month,travel['month'],Travel_Year,travel['year'])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxTRAVEL_LOS").send_keys(travel['length'])

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlTRAVEL_LOS_CD",travel['time_unit'])

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_tbxStreetAddress1")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxStreetAddress1").send_keys(travel['street_address'])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxCity").send_keys(travel['city'])

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlTravelState",travel['state'])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbZIPCode").send_keys(travel['zip_code'])

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlWhoIsPaying",travel['paying'])

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def travel_companions():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_lblOtherPersonsTravelingWithYou")

    no_selected("fieldset-group")

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def previous_travel():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_lblPREV_US_TRAVEL_IND")
    
    no_selected("fieldset-group")

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def address_and_phone():
    address_and_phone = data_filled["address_and_phone"]

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_LN1")

    sel_allchkbox("fieldset-group")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_LN1").send_keys(address_and_phone["street_address"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_CITY").send_keys(address_and_phone["city"])

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlCountry",address_and_phone["country"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblMailingAddrSame_0").click()

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_HOME_TEL").send_keys(address_and_phone["tel"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblAddPhone_1").click()

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_EMAIL_ADDR").send_keys(address_and_phone["email"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblAddEmail_1").click()

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_dtlSocial_ctl00_ddlSocialMedia",address_and_phone["social_media_name"])

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_dtlSocial_ctl00_tbxSocialMediaIdent")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_dtlSocial_ctl00_tbxSocialMediaIdent").send_keys(address_and_phone["social_media_account"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblAddSocial_1").click()

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def passport_info():
    passport_info = data_filled["passport_info"]

    driver.implicitly_wait(Pause_Time)

    sel_allchkbox("fieldset-group")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblLOST_PPT_IND_1").click()

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlPPT_TYPE",passport_info["type"])

    driver.implicitly_wait(Pause_Time)
    
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxPPT_NUM").send_keys(passport_info["number"])

    driver.implicitly_wait(Pause_Time)

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlPPT_ISSUED_CNTRY",passport_info["country"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxPPT_ISSUED_IN_CITY").send_keys(passport_info["city"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxPPT_ISSUED_IN_STATE").send_keys(passport_info["province"])

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlPPT_ISSUED_IN_CNTRY",passport_info["country"])

    Issued_Day="ctl00_SiteContentPlaceHolder_FormView1_ddlPPT_ISSUED_DTEDay"
    Issued_Month="ctl00_SiteContentPlaceHolder_FormView1_ddlPPT_ISSUED_DTEMonth"
    Issued_Year="ctl00_SiteContentPlaceHolder_FormView1_tbxPPT_ISSUEDYear"
    DOB_input(Issued_Day,passport_info["day"],Issued_Month,passport_info["month"],Issued_Year,passport_info["year"])

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def contract_info():
    contract_info = data_filled["contract_info"]

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_cbxUS_POC_NAME_NA")

    Not_Know=driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_cbxUS_POC_NAME_NA")
    if not Not_Know.is_selected():
        Not_Know.click()

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_ORGANIZATION").send_keys(contract_info["org"])

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlUS_POC_REL_TO_APP",contract_info["relationship"])

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_ADDR_LN1")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_ADDR_LN1").send_keys(contract_info["street_address"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_ADDR_CITY").send_keys(contract_info["city"])

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlUS_POC_ADDR_STATE",contract_info["state"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_ADDR_POSTAL_CD").send_keys(contract_info["zip_code"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_HOME_TEL").send_keys(contract_info["tel"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxUS_POC_EMAIL_ADDR").send_keys(contract_info["email"])

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def family_info():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_lblFATHER_SURNAME")

    sel_allchkbox("fieldset-group")

    no_selected("fieldset-group")

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_rblUS_OTHER_RELATIVE_IND_1")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_rblUS_OTHER_RELATIVE_IND_1").click()

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def present_work():
    present_work = data_filled["present_work"]

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_ddlPresentOccupation")

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlPresentOccupation",present_work["occupation"])

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_tbxEmpSchName")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxEmpSchName").send_keys(present_work["company"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxEmpSchAddr1").send_keys(present_work["street_address"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxEmpSchCity").send_keys(present_work["city"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxWORK_EDUC_ADDR_STATE").send_keys(present_work["province"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxWORK_EDUC_ADDR_POSTAL_CD").send_keys(present_work["zip_code"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxWORK_EDUC_TEL").send_keys(present_work["tel"])

    dropdown_process("ctl00_SiteContentPlaceHolder_FormView1_ddlEmpSchCountry",present_work["country"])

    Start_Day="ctl00_SiteContentPlaceHolder_FormView1_ddlEmpDateFromDay"
    Start_Month="ctl00_SiteContentPlaceHolder_FormView1_ddlEmpDateFromMonth"
    Start_Year="ctl00_SiteContentPlaceHolder_FormView1_tbxEmpDateFromYear"
    DOB_input(Start_Day,present_work["day"],Start_Month,present_work["month"],Start_Year,present_work["year"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxCURR_MONTHLY_SALARY").send_keys(present_work["salary"])

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_tbxDescribeDuties").send_keys(present_work["detailed_duty"])

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def previous_work():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_lblPreviouslyEmployed")

    no_selected("fieldset-group")

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()
   
def additional_work():
    additional_work = data_filled["additional_work"]

    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_lblCLAN_TRIBE_IND")

    no_selected("fieldset-group")

    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_FormView1_dtlLANGUAGES_ctl00_tbxLANGUAGE_NAME").send_keys(additional_work["language"])

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

def security_check():
    Explicit_Wait_func("ctl00_SiteContentPlaceHolder_FormView1_Label5")

    no_selected("fieldset-group")

    # save_and_continue()
    driver.find_element(By.ID, "ctl00_SiteContentPlaceHolder_UpdateButton3").click()

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
data_path = os.path.join(script_directory, "json", "data.json")

with open(data_path, 'r') as file:
    data_filled = json.load(file)

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