{"filter":false,"title":"admin.py","tooltip":"/checkout/admin.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.contrib import admin","","# Register your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":12,"column":38},"action":"insert","lines":["from django.contrib import admin","from .models import Order, OrderLineItem","","","class OrderLineAdminInline(admin.TabularInline):","    model = OrderLineItem","","","class OrderAdmin(admin.ModelAdmin):","    inlines = (OrderLineAdminInline, )","","","admin.site.register(Order, OrderAdmin)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":12,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588587188670,"hash":"be9014533c6f0b97962e8c6e295b02007fc03b1f"}