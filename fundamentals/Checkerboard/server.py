from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", row = 8, col = 8, color_one = "red", color_two = "black")

@app.route('/<int:x>')
def row(x):
    return render_template("index.html", row = x, col = 8, color_one = "red", color_two = "black")

@app.route('/<int:x>/<int:y>')
def cus_board(x,y):
    return render_template("index.html", row = x, col = y, color_one = "red", color_two = "black")

@app.route('/<int:x>/<int:y>/<string:first_color>')
def cus_board_two(x,y,first_color):
    return render_template("index.html", row = x, col = y, color_one = first_color, color_two = "black")

@app.route('/<int:x>/<int:y>/<string:first_color>/<string:second_color>')
def cus_board_three(x,y,first_color,second_color):
    return render_template("index.html", row = x, col = y, color_one = first_color, color_two = second_color)



if __name__ == "__main__":
    app.run(debug = True)