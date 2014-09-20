from django.conf.urls import patterns, include, url
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from aslgc.aslgc.urls import *
from library.views import *
from valuation.views import *
urlpatterns = patterns('',
	url(r'^$','library.views.index'),	
    
    url(r'^aimqa/$','valuation.views.aimqa'),
    url(r'^aslgc/$','library.views.aslgc'),

	url(r'^aimqaapp/$','valuation.views.loginpage'),	
    url(r'^aslgcapp/$','library.views.loginpage'),
    
    url(r'^login/','library.views.login_check'),
    url(r'^mhome/','library.views.mhome'),
    url(r'^muser/','library.views.muser'),
    url(r'^mstock/','library.views.mstock'),    
    url(r'^home/','library.views.home'),    
    url(r'^euser/','library.views.euser'),
    url(r'^ebook/','library.views.ebook'),
    url(r'^issue/','library.views.issue'),
    url(r'^meissue/','library.views.meissue'),
    url(r'^issued/','library.views.issued'),
    url(r'^bookdetails/','library.views.bookdetails'),
    url(r'^stockdetails/','library.views.stockdetails'),
    url(r'^stocks/','library.views.stocks'),
    url(r'^bookreturn/','library.views.bookreturn'),
    url(r'^bookreturns/','library.views.bookreturns'),
    url(r'^returns/','library.views.returns'),
    url(r'^stock/','library.views.stock'),
    url(r'^user/','library.views.userd'),
    url(r'^uhistory/','library.views.uhistory'),
    url(r'^bhistory/','library.views.bhistory'),
    url(r'^userdetails/','library.views.userdetails'),
    url(r'^uedit/','library.views.uedit'),
    url(r'^modify/','library.views.modify'),
    url(r'^delete/','library.views.delete'),
    url(r'^bdelete/','library.views.bdelete'),
    url(r'^bedit/','library.views.bedit'),
    url(r'^udelete/','library.views.udelete'),
    url(r'^logout/','library.views.logout_view'),  
    
    
    url(r'^flogin/','valuation.views.login_check'),
    url(r'^fhome/', 'valuation.views.home'),

    url(r'^registration/', 'valuation.views.registration'),
    url(r'^about/$','valuation.views.about'),
    url(r'^attendance/', 'valuation.views.attendance'),
    url(r'^members/', 'valuation.views.members'),
    url(r'^checkAttendance/', 'valuation.views.checkAttendance'),
    url(r'^classlist/', 'valuation.views.classlist'),
    url(r'^familydisplay/','valuation.views.familydisplay'),
    url(r'^AddEvent/','valuation.views.AddEvent'),
    url(r'^addFamilyToEvent/','valuation.views.addFamilyToEvent'),
    url(r'^display/','valuation.views.display'),
    url(r'^update/','valuation.views.update'),
    url(r'^memdis/','valuation.views.memdis'),
    url(r'^memdisplay/','valuation.views.memdisplay'),
    url(r'^memdelete/', 'valuation.views.memdelete'),
    url(r'^getMembers/','valuation.views.getMembers'),
    url(r'^saveStudentData/','valuation.views.saveStudentData'),
    url(r'^getEvents/','valuation.views.getEvents'),  
    url(r'^new/','valuation.views.new'),
    url(r'^flogout','valuation.views.flogout_view'),
    url(r'^addclass/','valuation.views.addClass'),
    url(r'^family/', 'valuation.views.family'),
    url(r'^getStudents/', 'valuation.views.getStudents'),
    url(r'^saveAttendance/', 'valuation.views.saveAttendance'),
    url(r'^ListAllStudents/', 'valuation.views.ListAllStudents'),
    url(r'^DisplayEventFamily/', 'valuation.views.DisplayEventFamily'),
    url(r'^DeleteFamily/', 'valuation.views.DeleteFamily'),
    url(r'^rationid_details/', 'valuation.views.rationid_details'),


    
    
    # Examples:
    # url(r'^$', 'Aimqa.views.home', name='home'),
    # url(r'^Aimqa/', include('Aimqa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
