from rest_framework import serializers
from . models import Tables, Product,PO
from datetime import date, datetime, timedelta


class Tableserializer(serializers.ModelSerializer):

    class Meta:
        model = Tables
        exclude = ('author',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class TableCreateUpdateserializer(serializers.ModelSerializer):

    tablerequireDate = serializers.DateField()
    tablerequiretime = serializers.CharField()

    class Meta:
        model = Tables
        fields = ['foodliketoeat', 'totalpersons',
                  'tablerequireDate', 'tablerequiretime']

    def validate(self, data):
        if data['tablerequireDate'] < date.today():
            raise serializers.ValidationError(
                "Date must be today or within 7 days")
        if data['tablerequireDate'] > (date.today()+timedelta(days=7)):
            raise serializers.ValidationError(
                "Date must be today or within 7 days")
        tablestrengthofhour = Tables.objects.filter(tablerequireDate=data['tablerequireDate']).filter(
            tablerequiretime=data['tablerequiretime']).count()
        if tablestrengthofhour > 20:
            raise serializers.ValidationError("reached peak time")
        return data

class POAdminserializer(serializers.ModelSerializer):
    class Meta:
        model=PO
        fields='__all__'


class POserializer(serializers.ModelSerializer):
    class Meta:
        model=PO
        exclude=('created','accepted','delivered','rejected','rejected_reason')