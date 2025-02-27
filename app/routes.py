from flask import Blueprint, render_template, redirect, url_for, request, session, flash

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

product_data = [
    {"id": 1, "name": "product 1", "price": 79.99, "colors": ["Red", "Blue"], "sizes": ["S", "M", "L", "XL"],
    "description": "description of product 1",
    "image": "images/shoe1.jpg"},

    {"id": 2, "name": "product 2", "price": 79.99, "colors": ["Red", "Blue"], "sizes": ["S", "M", "L", "XL"],
    "description": "description of product 2",
    "image": "images/shoe2.jpg"},
     
    {"id": 3, "name": "product 3", "price": 79.99, "colors": ["Red", "Blue"], "sizes": ["S", "M", "L", "XL"],
    "description": "description of product 3",
    "image": "images/shoe3.jpg"},
      
    {"id": 4, "name": "product 4", "price": 79.99, "colors": ["Red", "Blue"], "sizes": ["S", "M", "L", "XL"],
    "description": "description of product 4",
    "image": "images/shoe4.jpg"},
       
    {"id": 5, "name": "product 5", "price": 79.99, "colors": ["Red", "Blue"], "sizes": ["S", "M", "L", "XL"],
    "description": "description of product 5",
    "image": "images/shoe5.jpg"},
        
    {"id": 6, "name": "product 6", "price": 79.99, "colors": ["Red", "Blue"], "sizes": ["S", "M", "L", "XL"],
    "description": "description of product 6",
    "image": "images/shoe6.jpg"}
]   

@main.route('/products')
def product_listing():
    products = product_data
    return render_template('product_listing.html', products=products)

@main.route('/products/<int:product_id>')
def product_details(product_id):
    # Find the product by its ID
    product = next((item for item in product_data if item["id"] == product_id), None)
    
    if product:
        return render_template('product_details.html', product=product)
    else:
        return "Product not found", 404

@main.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Get product details from product_data
    product = next((p for p in product_data if p['id'] == product_id), None)
    if product:
        # Initialize cart if it doesn't exist
        if 'cart' not in session:
            session['cart'] = {}
        
        cart = session['cart']

        # Check if the product is already in the cart
        if str(product_id) in cart:  # Convert product_id to string if your keys are strings
            cart[str(product_id)]['quantity'] += 1  # Increase quantity
        else:
            cart[str(product_id)] = {
                'name': product['name'],
                'price': product['price'],
                'quantity': 1,
                'image': product.get('image', None) # Add image path
            }
        session.modified = True  # Mark session as modified to save changes
    return redirect(url_for('main.cart_view'))

@main.route('/cart/update/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    # Check if the cart exists in the session
    cart = session.get('cart', {})

    # Get the new quantity from the form
    new_quantity = int(request.form.get('quantity', 1))
    
    # Update the quantity or remove the item if quantity is zero
    if str(product_id) in cart:
        if new_quantity > 0:
            cart[str(product_id)]['quantity'] = new_quantity
        else:
            cart.pop(str(product_id))  # Remove item if quantity is zero
    
    # Update the session with the modified cart
    session['cart'] = cart
    flash('Cart updated successfully.')
    
    return redirect(url_for('main.cart_view'))

@main.route('/cart/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    # Retrieve the cart from the session
    cart = session.get('cart', {})

    # Remove the item from the cart if it exists
    if str(product_id) in cart:
        cart.pop(str(product_id))
        flash('Item removed from the cart.')

    # Update the session with the modified cart
    session['cart'] = cart

    return redirect(url_for('main.cart_view'))

@main.route('/clear_cart', methods=['POST'])
def clear_cart():
    session['cart'] = {}  # Clears the cart dictionary in session
    return redirect(url_for('main.cart_view'))

@main.route('/cart')
def cart_view():
    cart = session.get('cart', {})
    
    # Calculate total price
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    
    return render_template('cart.html', cart=cart, total_price=total_price)

# Checkout Route
@main.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Retrieve user information (e.g., name, address, payment info)
        name = request.form.get('name')
        email = request.form.get('email')
        address = request.form.get('address')
        payment_info = request.form.get('payment_info')
        
        # Process order (e.g., save order in database - here we just flash a message)
        cart = session.get('cart', [])
        
        if not cart:
            flash('Your cart is empty!')
            return redirect(url_for('main.product_listing'))  # Redirect to products if cart is empty
        
        # Here you would normally save order details in a database
        flash(f'Thank you for your purchase, {name}! Your order has been placed.')
        
        # Clear cart after checkout
        session['cart'] = []
        return redirect(url_for('main.order_confirmation'))  # Redirect to confirmation page

    # Render checkout page if GET request
    return render_template('checkout.html')

# Order Confirmation Route
@main.route('/order_confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

# Order Tracking Route
@main.route('/order_tracking')
def order_tracking():
    # Mock order tracking status for demonstration
    
    order_status = "In Transit"
    return render_template('order_tracking.html', status=order_status)