from pyscript import web, when

# Sample per-item rates for demonstration only.
rates = {
    "cards": 0.18,
    "flyers": 0.12,
    "posters": 2.50,
}

@when("click", "#estimate-button")
def calculate_estimate(event):
    product = web.page["product"].value
    quantity_text = web.page["quantity"].value

    try:
        quantity = int(quantity_text)
        if quantity < 1:
            raise ValueError
    except (TypeError, ValueError):
        web.page["estimate"].innerText = "Enter a quantity of 1 or more."
        return

    total = quantity * rates[product]
    web.page["estimate"].innerText = (
        f"Sample estimate: ${total:,.2f} "
        f"for {quantity:,} {product.replace('-', ' ')}."
    )