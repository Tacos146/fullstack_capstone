from django.contrib import admin
from .models import CarMake, CarModel

# Registering models with their respective admins
# admin.site.register(CarMake)
# admin.site.register(CarModel)


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
# CarMake を管理サイトに登録
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # 一覧ページで表示する項目

# CarModel を管理サイトに登録
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')  # 一覧ページで表示する項目
    list_filter = ('car_make', 'type', 'year')  # フィルタリング機能を追加
    search_fields = ('name',)  # 検索バーで検索可能にする

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)