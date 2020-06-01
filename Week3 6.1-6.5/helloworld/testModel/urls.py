from django.conf.urls import url, include
from . import views, testdb

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^index/', bv.index)
# ]

urlpatterns = [
    url(r'^testAddOneRecord/', testdb.testdb),
    url(r'^testSearch/', testdb.testSerch),
    url(r'^index/', views.index),
]
