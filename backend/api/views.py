from django.core.paginator import Paginator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactsSearchSerializer, ContactCreateSerializer, ContactsSerializer, ContactSerializer
from apps.models import Contact


# Create your views here.


class ContactsAPIView(APIView):
    @swagger_auto_schema(tags=['연락처 검색'], query_serializer=ContactsSearchSerializer)
    def get(self, request):
        params = request.GET.dict()
        order = params.get('order', 'id')
        page = int(params.get('page', 1))
        page_size = int(params.get('pagesize', 10))

        contacts = Contact.objects.all().order_by(order)
        if contacts.exists():
            paginator = Paginator(contacts, page_size)
            contacts = paginator.get_page(page)

            serializers = ContactsSerializer(contacts, many=True)
            return Response(serializers, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(tags=['연락처 생성'], query_serializer=ContactCreateSerializer)
    def post(self, request):
        return Response('연락처가 저장되었습니다.', status=status.HTTP_201_CREATED)


class ContactAPIView(APIView):
    contact_id = openapi.Parameter('contact_id', openapi.IN_PATH, description='Contact Id', required=True, type=openapi.TYPE_NUMBER)

    @swagger_auto_schema(tags=['연락처 상세정보'], manual_parameters=[contact_id])
    def get(self, request, contact_id):
        contacts = Contact.objects.filter(id=contact_id)
        if contacts.exists():
            serializers = ContactSerializer(contacts)
            return Response(serializers, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
