from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from django.http import HttpResponse
from .models import Compra

def exportar_compras_pdf(compras):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    # Título
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, "Reporte de Compras")
    
    # Tabla de compras
    data = [['ID', 'Cliente', 'Fecha', 'Total']]
    for compra in compras:
        data.append([str(compra.id), str(compra.cliente), compra.fecha.strftime('%Y-%m-%d %H:%M'), f"${compra.total}"])
    
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    table.wrapOn(p, 400, 200)
    table.drawOn(p, 100, 600)
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer

def generar_pdf_compras(request):
    compras = Compra.objects.all()
    buffer = exportar_compras_pdf(compras)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_compras.pdf"'
    response.write(buffer.getvalue())
    
    return response