from django.shortcuts import render, redirect

books = []


def initBooks():
    return books

books = [
    {
        'id': "1",
        'name': "红楼梦",
        'type': "古典小说",
        'jiesao': '《红楼梦》是中国文学史上一部长篇小说，被誉为中国封建社会的百科全书。',
        'author': '曹雪芹',
        'count': 10
    },
    {
        'id': "2",
        'name': "西游记",
        'type': "古典小说",
        'jiesao': '《西游记》是一部中国古典小说，以寓言的形式描写了唐僧师徒四人历经九九八十一难的奇幻旅程。',
        'author': '吴承恩',
        'count': 8
    },
    {
        'id': "3",
        'name': "三国演义",
        'type': "古典小说",
        'jiesao': '《三国演义》是中国历史小说，以三国时代的政治斗争为背景，展现了各种英雄豪杰的形象。',
        'author': '罗贯中',
        'count': 7
    },
    {
        'id': "4",
        'name': "水浒传",
        'type': "古典小说",
        'jiesao': '《水浒传》是中国古典小说，讲述了108位英雄好汉的故事，以忠义为主题。',
        'author': '施耐庵',
        'count': 6
    },
    {
        'id': "5",
        'name': "红岩",
        'type': "小说",
        'jiesao': '《红岩》是一部以重庆保卫战为背景的抗战小说，表现了青年学生的爱国情感。',
        'author': '冯雪峰',
        'count': 5
    }
]


def index(request):
    return render(request, 'login.html')


def home(request):
    id = request.GET.get("id")
    name = request.GET.get("name", "")

    filtered_books = []

    if id or name:
        for book in initBooks():
            if (id and book["id"] == id) or (name and name in book["name"]):
                filtered_books.append(book)
    else:

        filtered_books = initBooks()

    return render(request, 'book/index.html', {'books': filtered_books})


def add(request):
    if request.method == 'GET':
        return render(request, 'book/add.html')
    else:
        id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        type = request.POST.get('type', '')
        jiesao = request.POST.get('jiesao', '')
        author = request.POST.get('author', '')
        count = request.POST.get('count', '')

        new_book = {
            'id': id,
            'name': name,
            'type': type,
            'jiesao': jiesao,
            'author': author,
            'count': count
        }
        books.append(new_book)

        return redirect('/book/home')


def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")

        for book in books:
            if book['id'] == id:
                return render(request, 'book/edit.html', {'book': book})

    else:
        id = request.POST.get("id")
        name = request.POST.get('name', '')
        type = request.POST.get('type', '')
        jiesao = request.POST.get('jiesao', '')
        author = request.POST.get('author', '')
        count = request.POST.get('count', '')

        for book in books:
            if book['id'] == id:
                book['name'] = name
                book['type'] = type
                book['jiesao'] = jiesao
                book['author'] = author
                book['count'] = count
                break

        return redirect('/book/home')


def delete(request):
    id = request.GET.get("id")
    for book in books:
        if book['id'] == id:
            books.remove(book)
            break

    return redirect('/book/home')

def to_me(request):
    return render(request, "book/me.html")


borrowing_records = [

]
borrowing_records.append({
    'id': "1",
    'user_name': 'User1',
    'book_name': '红楼梦',
    'borrow_date': '2023-10-01',
    'return_date': '2023-10-10',
    'borrow_count': 5,
})

borrowing_records.append({
    'id': "2",
    'user_name': 'User2',
    'book_name': '红岩',
    'borrow_date': '2023-10-02',
    'return_date': '2023-10-11',
    'borrow_count': 5,
})

borrowing_records.append({
    'id': "3",
    'user_name': 'User3',
    'book_name': '水浒传',
    'borrow_date': '2023-10-03',
    'return_date': '2023-10-12',
    'borrow_count': 5,
})

borrowing_records.append({
    'id': "4",
    'user_name': 'User4',
    'book_name': '三国演义',
    'borrow_date': '2023-10-04',
    'return_date': '2023-10-13',
    'borrow_count': 5,
})

borrowing_records.append({
    'id': "5",
    'user_name': 'User5',
    'book_name': '西游记',
    'borrow_date': '2023-10-05',
    'return_date': '2023-10-14',
    'borrow_count': 5,
})

borrowing_records.append({
    'id': "6",
    'user_name': 'User6',
    'book_name': '红楼梦',
    'borrow_date': '2023-10-06',
    'return_date': '2023-10-15',
    'borrow_count': 5,
})

borrowing_records.append({
    'id': "7",
    'user_name': 'User7',
    'book_name': '三国演义',
    'borrow_date': '2023-10-07',
    'return_date': '2023-10-16',
    'borrow_count': 5,
})


def initBorrowingRecords():
    return borrowing_records


def index_borrow(request):
    return render(request, 'book/borrow.html', {'records': initBorrowingRecords()})
