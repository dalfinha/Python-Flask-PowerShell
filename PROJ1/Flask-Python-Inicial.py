from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get-process')
def get_process():
    result = subprocess.check_output(['powershell', 'Get-Process'])
    return render_template('result.html', result=result.decode('latin1'))

@app.route('/get-date')
def get_date():
    result = subprocess.check_output(['powershell', 'Get-Date'])
    return render_template('result.html', result=result.decode('latin1'))

@app.route('/get-childitem', methods=['GET', 'POST'])
def get_childitem():
    if request.method == 'POST':
        path = request.form['path']
        result = subprocess.check_output(['powershell', f'Get-ChildItem "{path}"'])
        return render_template('result.html', result=result.decode('latin1'))
    else:
        return render_template('get_childitem.html')

if __name__ == '__main__':
    app.run()
