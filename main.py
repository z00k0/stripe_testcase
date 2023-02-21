from dotenv import load_dotenv
import os
import stripe


load_dotenv()
API_KEY = os.getenv("SECRET_KEY")
stripe.api_key = API_KEY
session = stripe.checkout.Session.create(
    line_items=[
        {
            "price_data": {
                "currency": "usd",
                "product_data": {"name": "T-shirt"},
                "unit_amount": 2500,
            },
            "quantity": 2,
        }
    ],
    mode="payment",
    success_url="http://localhost:4242/success",
    cancel_url="http://localhost:4242/cancel",
)
# print(session)
print(f"{session.id=}")
print(f"{session.stripe_id=}")
