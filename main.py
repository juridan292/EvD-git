from pyscript import document

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

FINISH_MULTIPLIERS = {
    "standard": 1.0,
    "matte": 1.2,
    "velvet": 1.4,
    "gold": 1.8
}

FINISH_NAMES = {
    "standard": "Standard Matte",
    "matte": "Premium Silk",
    "velvet": "Velvet Soft-Touch",
    "gold": "Gold Foil Accent"
}

def calculate_estimate(event):
    product_select = document.querySelector("#product")
    finish_select = document.querySelector("#finish")
    quantity_input = document.querySelector("#quantity")
    estimate_output = document.querySelector("#estimate")
    
    product_key = product_select.value
    finish_key = finish_select.value
    
    try:
        qty = int(quantity_input.value)
        if qty <= 0:
            estimate_output.innerText = "Please enter a quantity greater than 0."
            return
            
        unit_price = RATES.get(product_key, 0.20)
        multiplier = FINISH_MULTIPLIERS.get(finish_key, 1.0)
        total = (qty * unit_price) * multiplier
        
        product_name = PRODUCT_NAMES.get(product_key, "Items")
        finish_name = FINISH_NAMES.get(finish_key, "Standard")
        
        estimate_output.innerText = f"Estimated total for {qty:,} {product_name} ({finish_name}): ${total:,.2f}"
    except ValueError:
        estimate_output.innerText = "Please enter a valid numeric quantity."