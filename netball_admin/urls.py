from django.conf.urls import url,include
from django.contrib import admin
from netball import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^netball/',include('netball.urls',namespace='netball')),
    url(r'^AdminDashboard/', views.index),
    # url(r'^demo/', views.demo),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
