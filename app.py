from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process the form data (save to database, etc.)
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        ssn = request.form.get('ssn')

        # You can save the data to a database or perform any other necessary actions here

        # Redirect to a page displaying user details
        return redirect(url_for('user_details', 
                                first_name=first_name, 
                                last_name=last_name, 
                                email=email, 
                                phone=phone, 
                                address=address, 
                                ssn=ssn))

    return render_template('index.html')

@app.route('/user_details')
def user_details():
    # Retrieve user details from URL parameters
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    address = request.args.get('address')
    ssn = request.args.get('ssn')

    return render_template('user_details.html', 
                           first_name=first_name, 
                           last_name=last_name, 
                           email=email, 
                           phone=phone, 
                           address=address, 
                           ssn=ssn)

if __name__ == '__main__':
    app.run(debug=True)
