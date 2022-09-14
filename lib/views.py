from .models import Book
from .serializers import BookSerializers, AddBookSerializers, UpdateBookSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class Books(APIView):
    # permission_classes = (IsAuthenticated,) 
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializers(books,many=True)

        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookById(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request, id):
        book = Book.objects.filter(id=id)
        serializer = BookSerializers(book,many=True)

        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddBook(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.data["created_by"] = str(request.user)
        serializer = AddBookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class UpdateBook(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self, request, id):
        book = Book.objects.filter(id=id)
        if not book.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        request.data["updated_by"] = str(request.user)
        request.data["id"] = id
        serializer = UpdateBookSerializers(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        try:
            Book.objects.filter(id=id).update(updated_by=request.data["updated_by"])
            Book.objects.filter(id=id).update(name=request.data["name"])
            Book.objects.filter(id=id).update(author_name=request.data["author_name"])
            Book.objects.filter(id=id).update(published_year=request.data["published_year"])
            Book.objects.filter(id=id).update(pages=request.data["pages"])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeleteBook(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, id):
        book = Book.objects.filter(id=id)
        if not book.exists():
            return Response({"book":"not_found"}, status=status.HTTP_404_NOT_FOUND)
        if book.delete():
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
