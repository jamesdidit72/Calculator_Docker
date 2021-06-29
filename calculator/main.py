from flask import Flask, request, abort
import calc_functions as calc_functions

def read_num(num_id):
    num = input(f"enter integer {num_id}: ")
    return int(num)



app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Calulator app Jenkins'

@app.route('/add/<int:num1>/<int:num2>')
def perform_add(num1, num2):
    num3 = calc_functions.add(num1, num2)
    print(num3)
    return str(num3)

# using query string
# URL: 127.0.0.1:5000/add?num1=1&num2=2
@app.route('/add')
def perform_add_query():
    num1 = request.args.get('num1', type =int, default = 0)
    num2 = request.args.get('num2', type = int, default = 0)

    if num1 is None or num2 is None:
        abort(404)
    num3 = calc_functions.add(num1, num2)
    print(num3)
    return str(num3)

if __name__ == '__main__':
    app.run(debug= True, host = '0.0.0.0')
# if __name__ == '__main__':
    # num1 = read_num(1)
    # num2 = read_num(2)

    # result = calc_functions.add(num1, num2)
    # print(result)
