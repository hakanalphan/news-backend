from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import News, Category
from .serializers import NewsSerializer, CategorySerializer

# Özel Sayfalama Sınıfı
class CustomPagination(PageNumberPagination):
    page_size = 12  # Sayfa başına 12 haber göster
    page_size_query_param = "page_size"
    max_page_size = 50  # Maksimum 50 haber sayfalanabilir

# Haber Listeleme ve Oluşturma
class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all().order_by("-published_at")
    serializer_class = NewsSerializer
    pagination_class = CustomPagination  # Sayfalama ekleme

# Haber Detay, Güncelleme ve Silme
class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def put(self, request, *args, **kwargs):
        news = self.get_object()
        serializer = NewsSerializer(news, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        news = self.get_object()
        news.delete()
        return Response({"message": "News deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# Kategori Listeleme ve Oluşturma
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Kategori Detay, Güncelleme ve Silme
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def put(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategorySerializer(category, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()
        return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
