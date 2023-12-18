from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_receipt(customer_name, amount_paid, payment_method, items_purchased):
    file_name = "payment_receipt_table.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []

    gst_percentage = 10  
    discount = 5 

    data = [
        ["Item", "Price", "GST", "Discount", "Total"]
    ]

    total_amount = 0

    for item, price in items_purchased.items():
        gst_amount = (price * gst_percentage) / 100
        total = price + gst_amount - discount
        total_amount += total

        data.append([item, f"${price:.2f}", f"${gst_amount:.2f}", f"${discount:.2f}", f"${total:.2f}"])

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ])

    table = Table(data)
    table.setStyle(table_style)

    styles = getSampleStyleSheet()
    elements.append(Paragraph("Payment Receipt", styles['Title']))
    elements.append(Paragraph(f"Customer Name: {customer_name}", styles['Normal']))
    elements.append(Paragraph(f"Amount Paid: ${amount_paid:.2f}", styles['Normal']))
    elements.append(Paragraph(f"Payment Method: {payment_method}", styles['Normal']))
    elements.append(table)
    elements.append(Paragraph(f"Total Amount: ${total_amount:.2f}", styles['Normal']))

    doc.build(elements)
    return file_name

customer_name = "Gaurav"
amount_paid = 150.00
payment_method = "Paytm UPI"
items = {
    "Shirt": 50.00,
    "Pants": 70.00,
    "Shoes": 40.00
}

receipt_file = generate_receipt(customer_name, amount_paid, payment_method, items)
print(f"Payment receipt with table generated: {receipt_file}")
