from django.core.mail import send_mail


def user_mail():
    send_mail('Your order has been confirm', 'Thanks for confirming oder.',
              'raj.kanani@plutustec.com',  # sender
              ['raj.kanani1487@gmail.com'],  # receiver
              fail_silently=False
              )
    print('mail sent successfully passed away from terminal..')
    return None
