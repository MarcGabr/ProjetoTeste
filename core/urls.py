from django.urls import path, re_path, include
from .views import( home, lista_pessoas, lista_veiculos,
lista_movrotativos, lista_mensalistas, lista_movmensalistas,
pessoa_novo, veiculo_novo, movrotativo_novo, mensalista_novo,
pessoa_update, pessoa_delete, veiculo_update )

urlpatterns = [
    path('/', home ,name='core_home'),
    path('pessoas/', lista_pessoas ,name='core_lista_pessoas'),
    path('pessoas-novo/', pessoa_novo ,name='core_pessoa_novo'),
    re_path(r'^pessoa-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),
    re_path(r'^pessoa-delete/(?P<id>\d+)/$', pessoa_delete, name='core_pessoa_delete'),
    path('veiculos/', lista_veiculos ,name='core_lista_veiculos'),
    re_path(r'^veiculo-update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    path('veiculos-novo/', veiculo_novo ,name='core_veiculo_novo'),
    path('mov-rot-list/', lista_movrotativos ,
    name='core_lista_movrotativos'),
    path('mov-rot-list-novo/', movrotativo_novo ,name='core_movrotativo_novo'),
    path('mensalistas/', lista_mensalistas , name='core_lista_mensalistas'),
    path('mensalistas-novo/', mensalista_novo ,name='core_mensalista_novo'),
    path('movmensalitas/', lista_movmensalistas , name='core_lista_movmensalistas'),
    #re_path(r'^$',home ,name='core_home')
]
