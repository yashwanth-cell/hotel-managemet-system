from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Rooms listing route
@app.route('/rooms')
def rooms():
    return render_template('rooms.html')

# Booking page route
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        room_type = request.form['room_type']
        nights = request.form['nights']
        
        # This would be saved to a database in a real application
        booking_details = {
            'name': name,
            'room_type': room_type,
            'nights': nights,
            'total_price': calculate_price(room_type, int(nights))
        }
        
        return render_template('confirm_booking.html', booking=booking_details)
    return render_template('booking.html')

# Booking confirmation route
@app.route('/confirm-booking', methods=['POST'])
def confirm_booking():
    name = request.form['name']
    room_type = request.form['room_type']
    nights = request.form['nights']
    
    # Calculate the total price (basic pricing)
    total_price = calculate_price(room_type, int(nights))
    
    return render_template('confirm_booking.html', name=name, room_type=room_type, nights=nights, total_price=total_price)

# Function to calculate total price based on room type and nights
def calculate_price(room_type, nights):
    prices = {'single': 100, 'double': 150, 'suite': 250}
    return prices.get(room_type, 0) * nights

if __name__ == '__main__':
    app.run(debug=True)
