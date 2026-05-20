from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('users.urls')),

    path('expenses/', include('expenses.urls')),

    path('dashboard/', include('analytics_app.urls')),

    path('budgets/', include('budgets.urls')),

    path('income/', include('income.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )