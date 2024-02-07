from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.db.models import Sum

# Create your views here.

@login_required(login_url='user-login')
def index(request):
    invent=Inventory.objects.all()
    purc= Product.objects.all()
    sale_total = Sales.objects.values('product_id').annotate(quantities=Sum('qty'))
    pur_total = Purchas.objects.values('product_id').annotate(qtys=Sum('qty'))
    #av_inventory= pur_total.exclude(pk__in=sale_total)
    context={
        'invent':invent,
        'sale_total': sale_total,
        'pur_total': pur_total,
        'purc' : purc,
        #'av_inventory':av_inventory,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    items=User.objects.all()
    contex={
        'items':items,
    }
    return render(request, 'dashboard/staff.html', contex)

@login_required(login_url='user-login')
def userreport_pdf(request):
    buf= io.BytesIO()
    c=canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob= c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    stocks= User.objects.all()

    lines=[]
    for stock in stocks:
        lines.append(str(stock.username))
        lines.append(str(stock.first_name))
        lines.append(str(stock.last_name))
        lines.append(str(stock.email))
        lines.append(str(stock.date_joined))
        lines.append(" ========================================== ")

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='staffReport.pdf')

@login_required(login_url='user-login')
def inventory(request):
    items= Inventory.objects.all()   #Using ORM

    contex={
        'items':items,
    }
    return render(request, 'dashboard/stock.html', contex)

@login_required(login_url='user-login')
def sales(request):
    items= Sales.objects.all()  #Using ORM
    contex={
        'items':items,
        }
    return render(request, 'dashboard/sale.html',contex)

@login_required(login_url='user-login')
def staff_index(request):
    submitted= False
    if request.method == 'POST':
        form=SalesForm(request.POST, staff=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff_index_sale?submitted=True')
    else:
        staff= request.user
        form= SalesForm(staff=staff)
    return render(request, 'dashboard/staff_index_sale.html',{'form': form, 'submitted':submitted})

@login_required(login_url='user-login')
def salesreport_pdf(request):
    buf= io.BytesIO()
    c=canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob= c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    stocks= Sales.objects.all()

    lines=[]
    for stock in stocks:
        lines.append(str(stock.id))
        lines.append(str(stock.customer_name))
        lines.append(str(stock.customer_mob))
        lines.append(str(stock.qty))
        lines.append(str(stock.price))
        lines.append(str(stock.total_amount))
        lines.append(str(stock.staff))
        lines.append(str(stock.sales_date))
        lines.append("  ")
       
    line_count = len(lines)
    lines_per_page = 50
    pages = line_count // lines_per_page
    if line_count % lines_per_page != 0:
        pages += 1

    for page in range(pages):
        start = page * lines_per_page
        end = start + lines_per_page
        page_lines = lines[start:end]
        for line in page_lines:
            textob.textLine(line)
        c.drawText(textob)
        c.showPage()
        textob = c.beginText()
        textob.setTextOrigin(inch, inch)
        textob.setFont("Helvetica", 14)
    #for line in lines:
     #   textob.textLine(line)
    
    #c.drawText(textob)
    #c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='salesTransactions.pdf')

@login_required(login_url='user-login')
def purchas(request):
    items= Purchas.objects.all()   #Using ORM
    contex={
        'items':items,
        }
    return render(request, 'dashboard/purchase.html', contex)

@login_required(login_url='user-login')
def purchasereport_pdf(request):
    buf= io.BytesIO()
    c=canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob= c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    stocks= Purchas.objects.all()

    lines=[]
    for stock in stocks:
        lines.append(str(stock.id))
        lines.append(str(stock.vendor.name))
        lines.append(str(stock.product.name))
        lines.append(str(stock.qty))
        lines.append(str(stock.price))
        lines.append(str(stock.total_amt))
        lines.append(str(stock.pur_date))
        lines.append("  ")

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='purchaseTransactions.pdf')

@login_required(login_url='user-login')
def stock_delete(request, pk):
    item= Inventory.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-stock')
    
    return render(request, 'dashboard/stock_delete.html')


@login_required(login_url='user-login')
def stock_edit(request, pk):
    item= Inventory.objects.get(id=pk)
    if request.method =='POST':
        form= InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-stock')
    else:
        form=InventoryForm(instance=item)
    contex={
        'form':form,
    }
    return render(request, 'dashboard/stock_edit.html', contex)

@login_required(login_url='user-login')
def stock_pdf(request):
    buf= io.BytesIO()
    c=canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob= c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    stocks= Inventory.objects.all()

    lines=[]
    for stock in stocks:
        lines.append(str(stock.id))
        lines.append(str(stock.product.name))
        lines.append(str(stock.pur_qty))
        lines.append(str(stock.sale_qty))
        lines.append("  ")

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='lastTransactions.pdf')

def av_stock(request):
    products = Product.objects.all()
    context={
        'products':products,
    }
    return render(request, 'dashboard/av_stock.html', context)

def get_available_quantity(product):
    total_sales = Sales.objects.filter(product=product).aggregate(total_sales=Sum('qty'))['total_sales'] or 0
    total_purchase = Purchas.objects.filter(product=product).aggregate(total_purchase=Sum('qty'))['total_purchase'] or 0
    available_quantity = total_purchase - total_sales
    return available_quantity