from django.contrib import admin
from .models import Usuario
from .models import Produto
from .models import Preco_Produto
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Produto)
admin.site.register(Preco_Produto)