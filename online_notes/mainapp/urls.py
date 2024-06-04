from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import StartPage, register, login_page, notes_list, logout_view, add_notes
urlpatterns = [
    path('', StartPage.as_view(), name='start_page'),
    path('home', StartPage.as_view(), name='start_page'),
    path('home/', StartPage.as_view(), name='start_page'),
    path('reg/', register, name='registration'),
    path('reg', register, name='registration'),
    path('login', login_page, name='login'),
    path('login/', login_page, name='login'),
    path('logout', logout_view, name='logout'),
    path('logout/', logout_view, name='logout'),
    path('notes', notes_list, name='notes'),
    path('notes/', notes_list, name='notes'),
    path('add_notes', add_notes, name='add_notes'),
    path('add_notes/', add_notes, name='add_notes'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
