from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Product,Collection
from .serializers import ProductSerializer,CollectionSerializer
from django.db.models import Count
from rest_framework import status

# Create your views here.
# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET':
#         qs = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(qs,many=True,context={'request':request}) # to convert queryset into json format
#         return Response(serializer.data)
#     elif request.method=='POST' :
#         serializer = ProductSerializer(data=request.data) #deserializing data that we get from client
       
#         # if serializer.is_valid():
#         #     serializer.validated_data
#         #     return Response('OK')
#         # else:
#         #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#         # or

#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         #serializer.validated_data
#         return Response({"status":"ok","response":serializer.data})
        


# #to handle error can put the code int  the try catch
# #also in place of try catch we can use 
# @api_view(['GET','PUT','DELETE'])
# def product_details(request,id):
#     
#     if request.method == 'GET':
#         serialize = ProductSerializer(product)
#         return Response(serialize.data)
#     elif request.method == "PUT":
#         serialize = ProductSerializer(product,data=request.data)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response({"status":"ok","response_data":serialize.data})
#     elif request.method == "DELETE":
#         if product.orderitem_set.count()>0:
#             return Response({'error':"product cannot be deleted becauser it ois associated with some other item"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response({"status":"Deleted"},status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET','PUT','DELETE'])
# def collection_details(request,pk):
#         collection = get_object_or_404(Collection.objects.annotate(
#             products_count=Count("product")
#         ),pk=pk)
#         if request.method=='GET' :
#             serialize = CollectionSerializer(collection)
#             return Response(serialize.data)
#         elif request.method == 'PUT':
#             serializer = CollectionSerializer(collection,data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response({"status":"updated"},status=status.HTTP_200_OK)
#         elif request.method == 'DELETE':
#             if collection.product_set.count() >0:
#                 return Response({'error':"product cannot be deleted becauser it ois associated with some other item"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#             collection.delete()
#             return Response({'message':'deleted'}, status=status.HTTP_204_NO_CONTENT)

    
        

# @api_view(['GET','POST'])
# def collection_list(request):
#     if request.method == 'GET':
#         qs =Collection.objects.annotate(products_count=Count('product')).all()
#         serialize = CollectionSerializer(qs,many=True)
#         return Response(serialize.data)
#     elif request.method == 'POST':
#         serialize = CollectionSerializer(data=request.data)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response({'message':'success','inserted_record':serialize.data},status=status.HTTP_201_CREATED)
    


# class based views
# class ProductList(APIView):
#     def get(self,request):
#         qs = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(qs,many=True,context={'request':request}) # to convert queryset into json format
#         return Response(serializer.data)

 #   def post(self,request):
    #         serializer = ProductSerializer(data=request.data) #deserializing data that we get from client
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response({"status":"ok","response":serializer.data})

# class collectionList(APIView):

#     def get(self,request):
#         qs =Collection.objects.annotate(products_count=Count('product')).all()
#         serialize = CollectionSerializer(qs,many=True)
#         return Response(serialize.data)
    
#     def post(self,request):
#         serialize = CollectionSerializer(data=request.data)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response({'message':'success','inserted_record':serialize.data},status=status.HTTP_201_CREATED)


# class collectionDetails(APIView):

#     def get(self,request,pk):
#         collection = get_object_or_404(Collection.objects.annotate(
#              products_count=Count("product")
#          ),pk=pk)
        
#         serialize = CollectionSerializer(collection)
#         return Response(serialize.data)
    
#     def put(self,request,pk):
#         collection = get_object_or_404(Collection.objects.annotate(
#              products_count=Count("product")
#          ),pk=pk)
#         serializer = CollectionSerializer(collection,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"status":"updated"},status=status.HTTP_200_OK)
    
#     def delete(self,request,pk):
#         collection = get_object_or_404(Collection.objects.annotate(
#              products_count=Count("product")
#          ),pk=pk)
#         if collection.product_set.count() >0:
#             return Response({'error':"product cannot be deleted becauser it ois associated with some other item"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response({'message':'deleted'}, status=status.HTTP_204_NO_CONTENT)



# class ProductDetails(APIView):
#     def get(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         serialize = ProductSerializer(product)
#         return Response(serialize.data)
    
#     def put(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         serialize = ProductSerializer(product,data=request.data)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response({"status":"ok","response_data":serialize.data})
    
#     def delete(self,request,id):
#         product = get_object_or_404(Product, pk=id)
#         if product.orderitem_set.count()>0:
#             return Response({'error':"product cannot be deleted becauser it ois associated with some other item"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response({"status":"Deleted"},status=status.HTTP_204_NO_CONTENT)


#using generics
class ProductList(ListCreateAPIView):
     queryset = Product.objects.select_related('collection').all()
     serializer_class = ProductSerializer

     def get_parser_context(self):
         return {'request':self.request}

     
class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer

    def delete(self,request,pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitem_set.count()>0:
            return Response({'error':"product cannot be deleted becauser it ois associated with some other item"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response({"status":"Deleted"},status=status.HTTP_204_NO_CONTENT)





class collectionList(ListCreateAPIView):
   queryset = Collection.objects.annotate(products_count=Count('product')).all()
   serializer_class = CollectionSerializer


class collectionDetails(RetrieveUpdateDestroyAPIView):
    queryset = get_object_or_404(Collection.objects.annotate(
        products_count=Count("product")
        ))
    serializer_class = CollectionSerializer

    def delete(self,request,pk):
        collection = get_object_or_404(Collection.objects.annotate(
             products_count=Count("product")
         ),pk=pk)
        if collection.product_set.count() >0:
            return Response({'error':"product cannot be deleted becauser it ois associated with some other item"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response({'message':'deleted'}, status=status.HTTP_204_NO_CONTENT)






        


        

        
        



