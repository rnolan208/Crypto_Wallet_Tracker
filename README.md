# Crypto Wallet Tracker

A full-stack cryptocurrency wallet tracking application built with Python, Flask, HTML, CSS and JavaScript.

🔗 **Live Demo:** https://rnolan208.github.io/Crypto_Wallet_Tracker/

🔗 **Backend API:** https://crypto-wallet-tracker-3i7z.onrender.com/

## Overview

Crypto Wallet Tracker is a full-stack portfolio project that retrieves live Ethereum wallet data and calculates the current value of a wallet in EUR.

The application uses a JavaScript frontend hosted on GitHub Pages and a Python Flask API hosted on Render. The backend retrieves an Ethereum wallet balance through the Alchemy API and the current ETH/EUR market price through the CoinGecko API before calculating the wallet's estimated EUR value.

The project was built to strengthen practical experience with Python, Flask, REST APIs, JSON-RPC, asynchronous JavaScript, environment variables, error handling and deploying a frontend and backend separately.

> **Project Status:** Completed

## Features

- **Ethereum Wallet Lookup:** enter a public Ethereum wallet address to retrieve its current ETH balance.
- **Live ETH Price:** retrieves the current Ethereum price in EUR using the CoinGecko API.
- **Wallet Valuation:** calculates the approximate EUR value of the wallet's ETH balance.
- **Address Validation:** checks the basic structure and hexadecimal format of Ethereum addresses before making external API requests.
- **Loading State:** displays a loading spinner while wallet data is being retrieved.
- **Error Handling:** provides user-friendly messages for invalid wallet addresses, API failures and connection problems.
- **Responsive Design:** adapts the interface for desktop and mobile screen sizes.
- **Secure API Configuration:** API credentials are stored using environment variables rather than exposed in the frontend or repository.
- **Automatic Deployment:** GitHub Actions automatically deploys the frontend to GitHub Pages when changes are pushed to the `main` branch.

## Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript
- Fetch API

### Backend

- Python
- Flask
- Flask-CORS
- Requests
- Gunicorn
- python-dotenv

### APIs

- **Alchemy Ethereum API** — retrieves Ethereum wallet balances using Ethereum JSON-RPC.
- **CoinGecko API** — retrieves the current Ethereum market price in EUR.

### Deployment & Development

- Git
- GitHub
- GitHub Actions
- GitHub Pages
- Render

## How It Works

The user enters a public Ethereum wallet address into the frontend. JavaScript sends an HTTPS request to the Flask API hosted on Render.

The Flask backend validates the wallet address and then makes two external API requests:

1. Alchemy's Ethereum API is queried using the `eth_getBalance` JSON-RPC method.
2. CoinGecko is queried for the current Ethereum price in EUR.

Ethereum balances returned by the blockchain are represented in Wei. The backend converts the hexadecimal balance to an integer and then converts Wei to ETH.

The wallet value is calculated using:

`ETH Balance × Current ETH Price = Estimated Wallet Value`

The backend returns the wallet address, ETH balance, ETH/EUR price and calculated wallet value as JSON. JavaScript processes the response and updates the interface.

## Application Architecture

```text
┌─────────────────────────────┐
│        GitHub Pages         │
│    HTML / CSS / JavaScript  │
└──────────────┬──────────────┘
               │
               │ HTTPS / Fetch
               ▼
┌─────────────────────────────┐
│      Render Web Service     │
│       Flask + Gunicorn      │
└──────────────┬──────────────┘
               │
         ┌─────┴─────┐
         ▼           ▼
┌──────────────┐ ┌──────────────┐
│   Alchemy    │ │  CoinGecko   │
│ ETH Balance  │ │ ETH/EUR Price│
└──────────────┘ └──────────────┘
```

The frontend never communicates directly with Alchemy or CoinGecko using private API credentials. External API requests are handled by the Flask backend, allowing API keys to remain server-side.

## API Endpoint

The application exposes a dynamic wallet endpoint:

```text
GET /api/wallet/<wallet_address>
```

For example:

```text
/api/wallet/0x604D38E27E8168731ab61722A0348F1823103FD1
```

A successful request returns JSON containing:

```json
{
  "wallet_address": "0x...",
  "eth_balance": 0.0,
  "wallet_value": 0.0,
  "eth_price_eur": 0.0
}
```

Invalid wallet addresses return an error response rather than making unnecessary external API requests.

## Error Handling and Validation

The backend performs basic Ethereum address validation before requesting wallet data. Addresses must:

- Begin with `0x`
- Contain 42 characters
- Contain valid hexadecimal characters after the `0x` prefix

External HTTP requests use timeouts and HTTP status checking. Errors from external services are logged by the backend while the public API returns a generic error message.

The frontend separately handles API errors and network connection failures and resets previously displayed wallet values before each new request.

## Running Locally

Clone the repository:

```bash
git clone https://github.com/rnolan208/Crypto_Wallet_Tracker.git
```

Navigate to the project:

```bash
cd Crypto_Wallet_Tracker
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```text
ALCHEMY_URL=your_alchemy_endpoint
COINGECKO_API_KEY=your_coingecko_api_key
```

API credentials are required to retrieve live blockchain and pricing data. The `.env` file is excluded from Git version control and should never be committed to the repository.

Start the Flask backend:

```bash
python backend/app.py
```

For local development, the frontend API URL in `frontend/js/app.js` can be pointed to:

```text
http://127.0.0.1:5000/api/wallet/
```

Then serve the `frontend` directory using a local development server.

## Project Structure

```text
Crypto_Wallet_Tracker/
│
├── .github/
│   └── workflows/
│       └── pages.yml
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── app.js
│   └── index.html
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

> `.env` is used locally but is excluded from the GitHub repository.

## Deployment

The project uses separate deployment services for the frontend and backend.

The **frontend** is hosted using GitHub Pages. A GitHub Actions workflow publishes the contents of the `frontend` directory whenever changes are pushed to the `main` branch.

The **backend** is deployed as a Python web service on Render and runs the Flask application using Gunicorn. Production API credentials are configured using Render environment variables.

This keeps the static frontend separate from the Python API while allowing the publicly hosted application to communicate with the backend over HTTPS.

## Skills Demonstrated

- Python programming
- Flask API development
- JavaScript Fetch API
- Asynchronous JavaScript and Promises
- REST-style API integration
- Ethereum JSON-RPC
- Working with JSON data
- HTTP GET and POST requests
- Environment variables and API key management
- Input validation
- Exception and error handling
- DOM manipulation
- Responsive HTML and CSS
- Frontend/backend architecture
- CORS configuration
- Git and GitHub version control
- GitHub Actions
- GitHub Pages deployment
- Render deployment
- Gunicorn production server configuration
- Debugging external API and deployment issues

## Future Improvements

Possible future improvements include:

- ERC-20 token balance tracking
- Support for additional fiat currencies
- Ethereum address checksum validation
- Wallet transaction history
- Historical ETH price charts
- Improved wallet portfolio breakdown
- Additional blockchain networks

## Author

**Robert Nolan**

Software Development Graduate  
Ireland