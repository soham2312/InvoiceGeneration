# yourapp/views.py
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Invoice

class InvoiceListView(View):
    template_name = 'invoice_list.html'

    def get(self, request):
        invoices = Invoice.objects.all()
        return render(request, self.template_name, {'invoices': invoices})

class InvoiceDetailView(View):
    template_name = 'invoice_detail.html'

    def get(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)
        return render(request, self.template_name, {'invoice': invoice})
