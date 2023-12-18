from django.urls import path
from myapp.views import products,detail,cart_view,return_view,cancel_view,order,grocery,review,send_email,category,contact_us,contact_us_success,faq_list
app_name='myapp'
urlpatterns = [
    path('',category,name='category'),
    path('products/<int:product_id>/<slug:slug>',products,name='products'),
    path('<int:product_id>/<slug:slug>',detail,name='detail'),
    path('cart/',cart_view, name='cart_view'),
    path('order/',order,name='order'),
    path('success/',return_view,name='return_view'),
    path('cancel/',cancel_view,name='cancel_view'),
    path('<int:product_id>/<int:pk>/review/',review,name='review'),
    path('sendmail/',send_email,name='send_email'),
    path('contact/', contact_us, name='contact_us'),  # Define the URL pattern for contact_us
    path('contact/success/', contact_us_success, name='contact_us_success'),  # Success page after submitting contact form
    path('faqs/', faq_list, name='faq_list'),
]




    
