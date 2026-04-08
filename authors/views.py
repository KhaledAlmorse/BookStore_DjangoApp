from django.shortcuts import render


authors = [
    {"id": 1, "name": "F. Scott Fitzgerald", "bio": "An American novelist and short story writer.", "image": "1.jpg"},
    {"id": 2, "name": "Harper Lee", "bio": "An American novelist widely known for To Kill a Mockingbird.", "image": "2.jpg"},
    {"id": 3, "name": "George Orwell", "bio": "An English novelist and essayist, journalist and critic.", "image": "3.jpg"},
]

def index(request):
    return render(request, "authors/index.html", context={"authors": authors})
