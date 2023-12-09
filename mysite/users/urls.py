from users import views
from django.urls import path

app_name = 'users'

urlpatterns = [

    #Orders
    
    path('orders/<int:id>/<int:pdcd>/<str:user>/' , views.Orders , name = 'orders'),
    
    # updating customer orders

    path('upd_orders/<int:id>/<int:upd_order_id>/', views.update_orders, name='upd_orders'),

    #Ratings and Feedback

    path('crf/<int:it_id>/<int:pc>/', views.CusRatFeed , name='CusRatFeed'),


    # update Ratings and Feedback

    path('crf_upd/<int:details_id>/<int:crf_id>/',views.update_crf , name='upd_crf'),

    # delete Ratings and Feedback

    path('crf_del/<int:details_id>/<int:crf_id>/',views.delete_crf , name='del_crf'),

    # Paypal Button

    path('buy/<int:amt>/<int:qnt>/' , views.Payment , name='buy'),

    # Payment Approve

    path('oa/' , views.OnApprove , name='oa'),

    # Payment Success

    path('ps/' , views.PaymentSuccess , name='ps')
]