import subprocess
from flask import Flask
from flask import request
from flask import session
from flask import escape
from flask import redirect, url_for
from flask import render_template
from flask import flash


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if not 'username' in session:
        return redirect(url_for('login'))

    response = ''
    if request.method == 'POST':
        mobile = request.form.get('mobile', '').replace(' ', '').replace('.', '').strip()
        if mobile:
            if not mobile.startswith('+34'):
                mobile = '+34' + mobile
            p = subprocess.Popen(['./mobile.sh', mobile], stdout=subprocess.PIPE)
            response, err = p.communicate()
            rm = '\n'.join(str(i) for i in response.splitlines())

            p = subprocess.Popen(['./mobile.sh', mobile], stdout=subprocess.PIPE)
            response, err = p.communicate()
            rb = '\n'.join(str(i) for i in response.splitlines())



    return render_template('index.html', rm=rm, rb=rb)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pw = request.form['password']
        if pw == app.passwd:
            session['username'] = 'admin'
            return redirect(url_for('index'))

        flash('Wrong password', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.passwd = '123'


if __name__ == "__main__":
    app.run(debug=True)
