```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crewmembers/', views.CrewMemberListView.as_view(), name='crewmembers'),
    path('crewmembers/<int:pk>', views.CrewMemberDetailView.as_view(), name='crewmember-detail'),
    path('certs/', views.CertListView.as_view(), name='certs'),
    path('certs/<int:pk>', views.CertDetailView.as_view(), name='cert-detail'),
    path('qualifications/', views.QualificationListView.as_view(), name='qualifications'),
    path('qualifications/<int:pk>', views.QualificationDetailView.as_view(), name='qualification-detail'),
    path('ships/', views.ShipListView.as_view(), name='ships'),
    path('ships/<int:pk>', views.ShipDetailView.as_view(), name='ship-detail'),
    path('positions/', views.PositionListView.as_view(), name='positions'),
    path('positions/<int:pk>', views.PositionDetailView.as_view(), name='position-detail'),
    path('assignments/', views.AssignmentListView.as_view(), name='assignments'),
    path('assignments/<int:pk>', views.AssignmentDetailView.as_view(), name='assignment-detail'),
    path('shipcrewallowances/', views.ShipCrewAllowanceListView.as_view(), name='shipcrewallowances'),
    path('shipcrewallowances/<int:pk>', views.ShipCrewAllowanceDetailView.as_view(), name='shipcrewallowance-detail'),
]
```