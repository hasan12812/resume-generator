from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # collect form data
        # handle optional photo - convert to base64 if provided
        photo_file = request.files.get('photo')
        photo_data = None
        if photo_file and photo_file.filename:
            import base64
            photo_data = "data:" + photo_file.content_type + ";base64," + base64.b64encode(photo_file.read()).decode('utf-8')

        data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'desired_title': request.form.get('desired_title'),
            'photo': photo_data,
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'country': request.form.get('country'),
            'city': request.form.get('city'),
            'address': request.form.get('address'),
            'postal_code': request.form.get('postal_code'),
            'summary': request.form.get('summary'),
            'experience_title': request.form.getlist('experience_title'),
            'experience_company': request.form.getlist('experience_company'),
            'experience_start': request.form.getlist('experience_start'),
            'experience_end': request.form.getlist('experience_end'),
            'experience_location': request.form.getlist('experience_location'),
            'experience_description': request.form.getlist('experience_description'),
            'experience_skills': request.form.getlist('experience_skills'),
            'experience_level': request.form.getlist('experience_level'),
            'edu_institution': request.form.getlist('edu_institution'),
            'edu_degree': request.form.getlist('edu_degree'),
            'edu_start': request.form.getlist('edu_start'),
            'edu_end': request.form.getlist('edu_end'),
            'edu_location': request.form.getlist('edu_location'),
            'edu_description': request.form.getlist('edu_description'),
            'skill_name': request.form.getlist('skill_name'),
            'skill_level': request.form.getlist('skill_level'),
            'courses': request.form.get('courses'),
            'languages': request.form.get('languages'),
            'references': request.form.get('references'),
            'links': request.form.get('links'),
            'internships': request.form.get('internships'),
            'hobbies': request.form.get('hobbies')
        }
        return render_template('resume.html', data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)