from flask import Flask, request


app = Flask(__name__)
app.debug = True


class Book(object):
    def __init__(self, title, writer, description, pubhouse, series, year):
        self.title, self.writer, self.description, self.pubhouse, self.series, self.year = title, writer, description, pubhouse, series, year

books = []




@app.route("/", methods=["GET"])
def index():
    return("КНИГИ" + " - " + "GET " + "http://localhost:3005/api/books" + " - "  "POST " +  "http://localhost:3005/api/books" + " - " + "PUT " +  "http://localhost:3005/api/books/0" + " - "  + "DELETE " +  "http://localhost:3005/api/books/0" + "МАШИНЫ" + " - " + "GET " + "http://localhost:3005/api/cars" + " - "  "POST " +  "http://localhost:3005/api/cars" + " - " + "PUT " +  "http://localhost:3005/api/cars/0" + " - "  + "DELETE " +  "http://localhost:3005/api/cars/0"
    )


@app.route("/api/books", methods=["GET"])
def GetB():
    book = ""; per = ""; quantity = 0
    for i in books:
        quantity = quantity + 1
        book = i.title + " - " + i.writer + " - " + i.description + " - " + i.pubhouse + " - " + i.series + " - " + i.year
        per = per + book
    return per, 200


@app.route("/api/books/", methods=["POST"])
def PostB():
    title, writer, description, pubhouse, series, year = None, None, None, None, None, None
    zapros = request.get_json()
    if zapros:
        if "title" in zapros:
            title = zapros["title"]
        else:
            return "Введите название книги"
        if "writer" in zapros:
            writer = zapros["writer"]
        else:
            return "Добавьте автора книги"
        if "description" in zapros:
            description = zapros["description"]
        else:
            return "Добавьте описание книги"
        if "pubhouse" in zapros:
            pubhouse = zapros["pubhouse"]
        else:
            return "Укажите издательство книги"
        if "series" in zapros:
            series = zapros["series"]
        else:
            return "Укажите серию книги"
        if "year" in zapros:
            year = zapros["year"]
        else:
            return "Укажите год издания книги"
    else:
        return "Ошибка, запрос не отправлен"
    if title and writer and description and pubhouse and series and year:
        book = Book(title, writer, description, pubhouse, series, year)
        books.append(book)
        return "Книга добавлена", 201


@app.route("/api/books/<int:IdB>", methods=["PUT"])
def PutB(IdB):
    zapros = request.get_json()
    if zapros:
        if 'title' in zapros:
            books[IdB].title = zapros['title']
        if 'writer' in zapros:
            books[IdB].writer = zapros['writer']
        if 'description' in zapros:
            books[IdB].description = zapros['description']
        if 'pubhouse' in zapros:
            books[IdB].pubhouse = zapros['pubhouse']
        if 'series' in zapros:
            books[IdB].series = zapros['series']
        if 'year' in zapros:
            books[IdB].year = zapros['year']
    else:
        return "Ошибка, запрос не отправлен", 403
    return "Книга отредактирована", 200



@app.route("/api/books/<int:IdB>", methods=["DELETE"])
def DeleteB(IdB):
    try:
        books.pop(IdB)
        return "Книга удалена", 200
    except:
        return "Ошибка"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3005)

