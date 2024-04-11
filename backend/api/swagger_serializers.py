from rest_framework import serializers


class ContactsSearchSerializer(serializers.Serializer):
    page = serializers.IntegerField(help_text='페이지 번호', required=False, default=1)
    pagesize = serializers.IntegerField(help_text='한 페이지 당 갯수', required=False, default=10)
    order = serializers.ChoiceField(choices=('name', 'email', 'phone'), help_text='정렬', required=False, default='id')


class ContactCreatableSerializer(serializers.Serializer):
    profile_image = serializers.CharField(help_text='프로필 이미지', required=False)
    name = serializers.CharField(help_text='이름', max_length=100)
    email = serializers.CharField(help_text='이메일', max_length=100, required=False)
    phone = serializers.CharField(help_text='전화번호', max_length=20, required=False)
    label = serializers.ListField(help_text='라벨', required=False)
    company = serializers.CharField(help_text='회사', max_length=20, required=False)
    position = serializers.CharField(help_text='직책', max_length=20, required=False)
    memo = serializers.CharField(help_text='메모', required=False)
    address = serializers.CharField(help_text='주소', required=False)
    birthday = serializers.DateTimeField(help_text='생일', required=False)
    website = serializers.CharField(help_text='웹사이트', required=False)
