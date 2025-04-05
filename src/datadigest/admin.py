from django.contrib import admin
from .models import pair_15min, pair_1h, pair_4h, pair_1d, pair_1w

class Pair15MinAdmin(admin.ModelAdmin):
    list_display = ('id', 'pair_name', 'open_price', 'close_price', 'high_price', 'low_price', 'datetime', 'time_db_update')

class Pair1hAdmin(admin.ModelAdmin):
    list_display = ('id', 'pair_name', 'open_price', 'close_price', 'high_price', 'low_price', 'datetime', 'time_db_update')

class Pair4hAdmin(admin.ModelAdmin):
    list_display = ('id', 'pair_name', 'open_price', 'close_price', 'high_price', 'low_price', 'datetime', 'time_db_update')

class Pair1dAdmin(admin.ModelAdmin):
    list_display = ('id', 'pair_name', 'open_price', 'close_price', 'high_price', 'low_price', 'datetime', 'time_db_update')

class Pair1wAdmin(admin.ModelAdmin):
    list_display = ('id', 'pair_name', 'open_price', 'close_price', 'high_price', 'low_price', 'datetime', 'time_db_update')

admin.site.register(pair_15min, Pair15MinAdmin)
admin.site.register(pair_1h, Pair1hAdmin)
admin.site.register(pair_4h, Pair4hAdmin)
admin.site.register(pair_1d, Pair1dAdmin)
admin.site.register(pair_1w, Pair1wAdmin)
