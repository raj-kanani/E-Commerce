from order.models import Order, OrderList
from payment.models import Payment
from io import BytesIO
from rest_framework.response import Response
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template
from .serializers import *
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from django.conf import settings


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    print(pdf, '--******--')
    if not pdf.err:
        return result.getvalue()
    return None


class GenerateInvoice(APIView):
    def post(self, request, *args, **kwargs):
        template = get_template('pdf.html')
        data = request.data
        order_id = data['order_id']
        order = Order.objects.get(id=order_id)
        payment = Payment.objects.get(order_id=order)
        user = Order.user
        order_item = OrderList.objects.filter(order=order)
        pdf = render_to_pdf('pdf.html', {'order_item': order_item, 'payment': payment,
                                         'user': user, 'order': order})
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadInvoice(APIView):
    def post(self, request):
        # template = get_template('pdf.html')
        data = request.data
        order_id = data['order_id']
        order = Order.objects.get(id=order_id)
        payment = Payment.objects.get(order_id=order)
        user = order.user
        invoice = Invoice(user=user, order_id=order_id, payment_method=payment.payment_type,
                          payment_status=payment.status, total_amount=payment.payment_price)
        invoice.save()
        order_items = OrderList.objects.filter(order=order)
        for i in order_items:
            InvoiceItem.objects.create(invoice=invoice, product=i.product, product_amount=i.price)

        pdf = render_to_pdf('pdf.html',
                            {'invoice': invoice, 'order_item': order_items, 'payment': payment, 'user': user,
                             'order': order})
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % (data['order_id'])
            # content = "inline; filename = '%s'" % (filename)
            content = "attachment; filename = '%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("not found")


class ShareInvoice(APIView):
    def post(self, request):
        template = get_template('pdf.html')
        data = request.data
        order_id = data['order_id']
        order = Order.objects.get(id=order_id)
        payment = Payment.objects.get(order_id=order)
        user = order.user
        invoice = Invoice(user=user, order_id=order_id, payment_method=payment.payment_type,
                          payment_status=payment.status, total_amount=payment.payment_price)
        invoice.save()
        order_items = OrderList.objects.filter(order=order)
        for i in order_items:
            InvoiceItem.objects.create(invoice=invoice, product=i.product, product_amount=i.price)

        pdf = render_to_pdf('pdf.html',
                            {'invoice': invoice, 'order_item': order_items, 'payment': payment, 'user': user,
                             'order': order})

        if pdf:
            mail_subject = "Your order process has been success !!"
            email = EmailMessage(mail_subject, 'this is a message', settings.EMAIL_HOST_USER, [user.email])
            email.attach('order.pdf', pdf, "application/pdf")
            email.send()
        return Response({'msg': 'Invoice generated! & send mail your account'})

