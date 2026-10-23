from pyscript import document

# Unit prices per product
RATES = {
    "cards": 0.15,
    "flyers": 0.35,
    "posters": 2.50
}

PRODUCT_NAMES = {
    "cards": "Business cards",
    "flyers": "Flyers",
    "posters": "Posters"
}

def calculate_estimate(event):
    product_select = document.querySelector("#product")
    quantity_input = document.querySelector("#quantity")
    estimate_output = document.querySelector("#estimate")
    
    product_key = product_select.value
    
    try:
        qty = int(quantity_input.value)
        if qty <= 0:
            estimate_output.innerText = "Please enter a quantity greater than 0."
            return
            
        unit_price = RATES.get(product_key, 0.20)
        total = qty * unit_price
        product_name = PRODUCT_NAMES.get(product_key, "Items")
        
        estimate_output.innerText = f"Estimated total for {qty:,} {product_name}: ${total:,.2f}"
    except ValueError:
        estimate_output.innerText = "Please enter a valid numeric quantity."