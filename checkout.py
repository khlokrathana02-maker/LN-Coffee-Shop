import requests
from flask import Flask
from flask_mail import Mail, Message
import random
from datetime import datetime

# ==========================
# 🔧 Configuration
# ==========================

# Telegram Bot Settings
BOT_TOKEN = "7505360983:AAHxFM0m00Pp5AH57fJRvPupVenqw9ANDt4"
CHAT_ID = "@na_su33_channel"

# Currency rate USD → KHR
USD_TO_KHR = 4100

# Flask-Mail config - example for Gmail SMTP
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'lncoffee005@gmail.com'
MAIL_PASSWORD = 'fbnb pypv rozw bjhc'
MAIL_DEFAULT_SENDER = 'lncoffee005@gmail.com'

# ==========================
# 🚀 Flask App Setup
# ==========================
app = Flask(__name__)

# Configure mail
app.config.update(
    MAIL_SERVER=MAIL_SERVER,
    MAIL_PORT=MAIL_PORT,
    MAIL_USE_TLS=MAIL_USE_TLS,
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_DEFAULT_SENDER=MAIL_DEFAULT_SENDER,
)

mail = Mail(app)


# ==========================
# 🔧 Helper Function
# ==========================
def to_number(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0


def generate_numeric_order_id(length=8):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


order_id = generate_numeric_order_id()

now = datetime.now()

# Format as DD/MM/YY HH:MM
formatted_date = now.strftime("%d/%m/%y %H:%M")


# ==========================
# 🛒 Checkout Function
# ==========================
def process_checkout(data):
    cart_items = data.get("renderCartList", [])
    sub_qty = sum((item['qty']) for item in cart_items)
    total_usd = sum(to_number(item['qty']) * to_number(item['price']) for item in cart_items)
    shipping_usd = 2.0
    grand_total_usd = total_usd + shipping_usd
    total_khr = grand_total_usd * USD_TO_KHR

    product_lines = ""
    for item in cart_items:
        line_total = to_number(item['qty']) * to_number(item['price'])
        product_lines += f"{item['title']} x {item['qty']} = ${line_total:.2f}\n"

    message = f"""
===== 🥤 Order 🥤 =====
🆔 Order ID: {order_id}
💵 Payment Method: Cash
📅 Date & Time: {formatted_date}

👤 Customer Name: {data.get('first_name', '')} {data.get('last_name', '')}
📞 Phone Number: {data.get('phone', '')}
📧 Email: {data.get('email', '')}
📍 Address: {data.get('address', '')}
📝 Notes: {data.get('notes', '')}

---- ☕ 🍹 Order Summary 🍹 ☕ ----
{product_lines}
------------------------------------
Sub Qty: {sub_qty}
Sub Total USD: ${total_usd:.2f}
Shipping: ${shipping_usd:.2f}
------------------------------------
Grand Total USD: ${grand_total_usd:.2f}
Grand Total KHR: ៛{total_khr:,.2f}
"""

    status = {"telegram": "pending", "email": "pending"}

    # Send Telegram
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        status["telegram"] = "success"
    except Exception as e:
        status["telegram"] = f"failed: {e}"

    # Send Email
    try:
        with app.app_context():
            msg = Message(
                subject="Your Order Confirmation",
                recipients=[data.get('email')],
                body=message
            )
            mail.send(msg)
        status["email"] = "success"
    except Exception as e:
        status["email"] = f"failed: {e}"

    return status


# ==========================
# ✅ Example Usage
# ==========================
if __name__ == "__main__":
    sample_order = {
        "first_name": "John",
        "last_name": "Doe",
        "address": "123 Street",
        "city": "Phnom Penh",
        "country": "Cambodia",
        "zip": "12000",
        "email": "customer@example.com",
        "phone": "0123456789",
        "cart": [
            {"title": "T-shirt", "qty": 2, "price": 10.5, "image": "https://example.com/tshirt.jpg"},
            {"title": "Shoes", "qty": 1, "price": 45.0, "image": "https://example.com/shoes.jpg"}
        ]
    }

    result = process_checkout(sample_order)
    print(result)
