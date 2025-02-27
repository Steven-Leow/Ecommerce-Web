# Ecommerce Demo with Chatbot

This is a eCommerce demo web application built using Flask. It features product listings, a shopping cart, and a chatbot integrated into the UI.

## Features
- **Product Management**: View and browse products.
- **Shopping Cart**: Add products to a cart.
- **User Authentication**: Login functionality (Placeholder).
- **Chatbot**: Interactive chatbot for customer support using FastAPI.
- **Bootstrap UI**: Responsive design with Bootstrap.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (or any preferred database)
- **Chatbot API**: FastAPI (Python)

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/ecommerce-demo.git
cd ecommerce-demo
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Flask Application
```sh
flask run
```

### 5. Run the Chatbot API (FastAPI)
```sh
uvicorn chatbot_api:app --host 0.0.0.0 --port 8000
```

## Usage
1. Open `http://127.0.0.1:5000/` in your browser.
2. Browse products and add them to your cart.
3. Click the chat bubble to interact with the chatbot.

## Chatbot Feature
The chatbot is built with FastAPI and interacts with users through a simple UI in `base.html`. It listens for user messages and responds dynamically based on predefined logic or AI-based responses.

## Future Enhancements
- Implement user authentication and checkout functionality.
- Improve chatbot responses with AI.
- Integrate a payment gateway.

## License
This project is open-source and available under the MIT License.

