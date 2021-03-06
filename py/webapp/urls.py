from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^robertsTest/messages$', 'robertsTest.views.all_messages'),
#    url(r'^robertsTest/', include(robertsTest.urls.urlpatterns)),

    # Examples:
    url(r'^$', 'sign_server.views.hello_world'),
    url(r'^miniBoard/$', 'sign_server.views.mini_board'),


    #debug
    url(r'^board_test/$', 'sign_server.views.board_test'),
    url(r'^calibrate_displays/$', 'sign_server.views.calibrate_displays'),
    url(r'^file_test/$', 'sign_server.views.file_test'),
    url(r'^file_test/(?P<file>\w+)$', 'sign_server.views.specific_file_test'),

    url(r'^random_file/$', 'sign_server.views.random_file_test'),

    url(r'^clear_board/$', 'sign_server.views.clear_board'),
    url(r'^time_stamp/$', 'sign_server.views.time_stamp'),
    url(r'^twitter_board/$', 'sign_server.views.twitter_panel'),
    url(r'^info_board/$', 'sign_server.views.info_panel'),
    url(r'^network_status/$', 'sign_server.views.network_status'),

    url(r'^announcements_panel/$', 'sign_server.views.announcements_panel'),
    url(r'^view_announcements/$', 'sign_server.views.view_announcements'),
    url(r'^update_announcements/$', 'sign_server.views.update_announcements'),
    url(r'^char_test/$', 'sign_server.views.char_test'),
    url(r'^test_chars/$', 'sign_server.views.test_chars'),

    url(r'^raw/(?P<row>.*)/(?P<col>.*)/(?P<msg>.*)', 'sign_server.views.rawInterface'),
    url(r'^rawBox/(?P<row>.*)-(?P<rowlimit>.*)/(?P<col>.*)-(?P<collimit>.*)/(?P<msg>.*)', 'sign_server.views.rawRegionInterface'),
    url(r'^mini/(?P<row>.*)/(?P<col>.*)/(?P<msg>.*)', 'sign_server.views.miniWrite'),
    url(r'^miniTimeTemp/$', 'sign_server.views.miniTimeTemp'),

    url(r'^google/logo/$', 'sign_server.views.google_logo'),
    url(r'^google/drawbox/$', 'sign_server.views.google_search_box'),
    url(r'^google/search/(?P<searchTerm>.*)$', 'sign_server.views.google_do_search'),
    url(r'^google/search$', 'sign_server.views.google_search_page'),



    url(r'^peggy/get_lease$', 'sign_server.peggy.get_lease'),
    url(r'^peggy/get_lease/(?P<term>.*)', 'sign_server.peggy.get_lease'),
    url(r'^peggy/clear/(?P<lease_code>.*)/(?P<row>.*)', 'sign_server.peggy.clear_board'),
    url(r'^peggy/clear$', 'sign_server.peggy.clear_board'),
    url(r'^peggy/clear/(?P<lease_code>.*)', 'sign_server.peggy.clear_board'),
    url(r'^peggy/write$', 'sign_server.peggy.write_to_board'),
    url(r'^peggy/write/(?P<lease_code>.*)/(?P<row>.*)/(?P<col>.*)/(?P<msg>.*)', 'sign_server.peggy.write_to_board'),
    url(r'^peggy/set_color$', 'sign_server.peggy.set_color'),
    url(r'^peggy/set_color/(?P<lease_code>.*)/(?P<color>.*)', 'sign_server.peggy.set_color'),

    url(r'^peggy/2/get_lease/(?P<term>\d+)/(?P<top_row>\d*)/(?P<left_col>\d*)/(?P<bottom_row>\d*)/(?P<right_col>\d*)', 'sign_server.peggy2.get_lease'),
    url(r'^peggy/2/get_lease/(?P<term>\d+)', 'sign_server.peggy2.get_lease'),
    url(r'^peggy/2/get_lease', 'sign_server.peggy2.get_lease'),
    url(r'^peggy/2/renew_lease/(?P<lease_code>.+)/(?P<term>\d+)', 'sign_server.peggy2.renew_lease'),
    url(r'^peggy/2/expire_lease/(?P<lease_code>.+)', 'sign_server.peggy2.expire_lease'),
    url(r'^peggy/2/write/(?P<lease_code>.+)/(?P<row>\d*)/(?P<col>\d*)/(?P<msg>.*)', 'sign_server.peggy2.write_to_board'),
    url(r'^peggy/2/clear/(?P<lease_code>.+)', 'sign_server.peggy2.clear_board'),
    url(r'^peggy/2/set_color/(?P<lease_code>.+)/(?P<color>.+)', 'sign_server.peggy2.set_color'),


    # url(r'^sign_server/', include('sign_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
