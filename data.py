from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

script_directory = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_directory, "json", "data.json")

@app.route('/', methods=['GET', 'POST'])
def form():
    with open(data_path, 'r') as file:
        data = json.load(file)
    dropdown_fields = {
        'first_page.location': ["CHINA, BEIJING", "CHINA, GUANGZHOU", "JAPAN, OSAKA/FUKUOKA", "JAPAN, TOKYO/SAPPORO"],
        'second_page.security_question': ["What is the given name of your father's father?", "What is the given name of your mother's mother?"],
        'personal_one.marital_status': ["SINGLE", "MARRIED", "DIVORCED"],
        'personal_one.day': ["01", "02", "03"],
        'personal_one.month': ["JAN", "FEB", "MAR"],
        'personal_one.country': ["CHINA", "KOREA, REPUBLIC OF (SOUTH)", "JAPAN"],
        'personal_two.country': ["CHINA", "KOREA, REPUBLIC OF (SOUTH)", "JAPAN"],
        'travel.purpose_of_trip': ["TEMP. BUSINESS PLEASURE VISITOR (B)", "ACADEMIC OR LANGUAGE STUDENT (F)"],
        'travel.specify': ["BUSINESS & TOURISM (TEMPORARY VISITOR) (B1/B2)", "BUSINESS/CONFERENCE (B1)"],
        'travel.day': ["01", "02", "03"],
        'travel.month': ["JAN", "FEB", "MAR"],
        'travel.time_unit': ["Day(s)", "Week(s)", "Month(s)"],
        'travel.state': ["WASHINGTON", "TENNESSEE", "KANSAS"],
        'travel.paying': ["Self", "Present Employer", "Other Person"],
        'travel.paying': ["Self", "Present Employer", "Other Person"],
        'address_and_phone.country': ["CHINA", "KOREA, REPUBLIC OF (SOUTH)", "JAPAN"],
        'address_and_phone.social_media_name': ["QZONE (QQ)", "FACEBOOK", "INSTAGRAM"],
        'passport_info.type': ["REGULAR", "OFFICIAL"],
        'passport_info.country': ["CHINA", "KOREA, REPUBLIC OF (SOUTH)", "JAPAN"],
        'passport_info.day': ["01", "02", "03"],
        'passport_info.month': ["JAN", "FEB", "MAR"],
    }
    if request.method == 'POST':
        updated_data = request.form.to_dict()
        with open(data_path, 'r') as file:
            data = json.load(file)
        for form_key, value in updated_data.items():
            if not value.strip():
                print("Null check failed")
                return redirect(url_for('form'))
            keys = form_key.split('.')
            if len(keys) == 2:
                category, key = keys
                if category in data and key in data[category]:
                    data[category][key] = value
        with open(data_path, 'w') as file:
            json.dump(data, file, indent=4)
        return redirect(url_for('form'))
    else:
        with open(data_path, 'r') as file:
            data = json.load(file)
        return render_template('form.html', data=data,dropdown_fields=dropdown_fields)


app.run()
