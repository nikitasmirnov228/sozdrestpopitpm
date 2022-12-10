from flask import Flask, request


app = Flask(__name__)
app.debug = True


class Car(object):
    def __init__(self, brand, title, cost, year, mileage, numofown, ls):
        self.brand, self.title, self.cost, self.year, self.mileage, self.numofown, self.ls = brand, title, cost, year, mileage, numofown, ls

cars = []




@app.route("/", methods=["GET"])
def index():
    return("КНИГИ" + " - " + "GET " + "http://localhost:3005/api/books" + " - "  "POST " +  "http://localhost:3005/api/books" + " - " + "PUT " +  "http://localhost:3005/api/books/0" + " - "  + "DELETE " +  "http://localhost:3005/api/books/0" + "МАШИНЫ" + " - " + "GET " + "http://localhost:3005/api/cars" + " - "  "POST " +  "http://localhost:3005/api/cars" + " - " + "PUT " +  "http://localhost:3005/api/cars/0" + " - "  + "DELETE " +  "http://localhost:3005/api/cars/0"
    )


@app.route("/api/cars", methods=["GET"])
def GetC():
    car = ""; per = ""; quantity = 0
    for i in cars:
        quantity = quantity + 1
        car = i.brand + " - " + i.title + " - " + i.cost + " - " + i.year + " - " + i.mileage + " - " + i.numofown + " - " + i.ls
        per = per + car
    return per, 200


@app.route("/api/cars/", methods=["POST"])
def PostC():
    brand, title, cost, year, mileage, numofown, ls = None, None, None, None, None, None, None
    zapros = request.get_json()
    if zapros:
        if "brand" in zapros:
            brand = zapros["brand"]
        else:
            return "Введите название марки машины"
        if "title" in zapros:
            title = zapros["title"]
        else:
            return "Введите модель машины"
        if "cost" in zapros:
            cost = zapros["cost"]
        else:
            return "Введите стоимость машины"
        if "year" in zapros:
            year = zapros["year"]
        else:
            return "Введите год выпуска машины"
        if "mileage" in zapros:
            mileage = zapros["mileage"]
        else:
            return "Введите пробег машины"
        if "numofown" in zapros:
            numofown = zapros["numofown"]
        else:
            return "Укажите количество владельцев машины"
        if "ls" in zapros:
            ls = zapros["ls"]
        else:
            return "Укажите количество Л/С машины"
    else:
        return "Ошибка, запрос не отправлен"
    if brand and title and cost and year and mileage and numofown and ls:
        car = Car(brand, title, cost, year, mileage, numofown, ls)
        cars.append(car)
        return "Машина добавлена", 201


@app.route("/api/cars/<int:IdC>", methods=["PUT"])
def PutC(IdC):
    zapros = request.get_json()
    if zapros:
        if 'brand' in zapros:
            cars[IdC].brand = zapros['brand']
        if 'title' in zapros:
            cars[IdC].title = zapros['title']
        if 'cost' in zapros:
            cars[IdC].cost = zapros['cost']
        if 'year' in zapros:
            cars[IdC].year = zapros['year']
        if 'mileage' in zapros:
            cars[IdC].mileage = zapros['mileage']
        if 'numofown' in zapros:
            cars[IdC].numofown = zapros['numofown']
        if 'ls' in zapros:
            cars[IdC].ls = zapros['ls']
    else:
        return "Ошибка, запрос не отправлен", 403
    return "Машина отредактирована", 200



@app.route("/api/cars/<int:IdC>", methods=["DELETE"])
def DeleteC(IdC):
    try:
        cars.pop(IdC)
        return "Машина удалена", 200
    except:
        return "Ошибка"


if __name__ == "__main__":
    app.run(port=3005)

