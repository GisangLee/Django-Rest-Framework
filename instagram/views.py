from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
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

    @action(detail=False, methods=["GET"])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["PATCH"])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body :", request.body)
    #     print("request.POST :", request.POST)  # print 비추 logger 추천
    #     return super().dispatch(request, *args, **kwargs)
