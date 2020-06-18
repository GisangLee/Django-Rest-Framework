from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer


class PostListApiView(generics.ListAPIView):
    queryset = Post.objects.filter(is_public=True)
    serializer_class = PostSerializer


class PublicPostListApiView(APIView):

    def get(self, request):
        queryset = Post.objects.filter(is_public=True)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


public_post_list = PublicPostListApiView.as_view()

# @api_view(['GET'])
# def public_post_list(request):
#     queryset = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(queryset, many=True)
#     return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body :", request.body)
    #     print("request.POST :", request.POST)  # print 비추 logger 추천
    #     return super().dispatch(request, *args, **kwargs)
