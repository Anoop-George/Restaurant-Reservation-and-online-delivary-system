from rest_framework import generics, permissions
from .models import Tables, Product,PO
from .serializers import Tableserializer, ProductSerializer,TableCreateUpdateserializer,POserializer,POAdminserializer
from .permissions import IsAuthor
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import datetime
from rest_framework.exceptions import ValidationError


# class Tablecreateview(APIView):

#     def post(self, request, format=None):
#         permission_classes = [permissions.IsAuthenticated]
#         serializer = Tableserializer(data=request.data)
#         x = datetime.datetime.now()
#         date=x.strftime("%x")
#         author = self.request.user
#         if serializer.is_valid():
#             serializer.save(author=author)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Tablecreateview(generics.CreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TableCreateUpdateserializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        request_user = self.request.user
        dataset = Tables.objects.filter(author = request_user).filter(created = datetime.date.today() ).count()
        if dataset >=3:
            raise ValidationError("You have already booked 3 tables,delete booked table or contact us if you want to book more")       
        serializer.save(author=request_user)


class TableDetails(generics.DestroyAPIView):
    queryset = Tables.objects.all()
    serializer_class = Tableserializer
    permission_classes = [IsAuthor]


class TablesDetailsall(APIView):

    def get(self, request, format=None):
        permission_classes = [IsAuthor]
        Order_details = Tables.objects.filter(author=request.user.id)
        serializer = Tableserializer(Order_details, many=True)
        return Response(serializer.data)

class TotalTables(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = Tableserializer
    permission_classes = [permissions.IsAdminUser]

class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class POcreate(generics.CreateAPIView):
    queryset = PO.objects.all()
    
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return POAdminserializer
        return POserializer
    

class POlist(generics.ListAPIView):
    queryset = PO.objects.all()
    serializer_class = POserializer
    permission_classes = [permissions.IsAdminUser]

class POdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PO.objects.all()
    serializer_class = POserializer
    permission_classes = [permissions.IsAdminUser]
