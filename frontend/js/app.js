const walletInput = document.getElementById("wallet-address");
const ethBalance = document.getElementById("eth-balance");
const ethPrice = document.getElementById("eth-price");
const walletValue = document.getElementById("wallet-value");
const errorMessage = document.getElementById("error-message");
const walletForm = document.getElementById("wallet-form");
const loadingSpinner = document.getElementById("loading-spinner");


walletForm.addEventListener("submit", function (event) {
    event.preventDefault();
    console.log("Wallet lookup submitted");

    const walletAddress = walletInput.value;
    errorMessage.textContent = "";
    ethBalance.textContent = "--";
    ethPrice.textContent = "--";
    walletValue.textContent = "--";
    loadingSpinner.style.display = "block";

    console.log(walletAddress);

    const apiUrl = "http://127.0.0.1:5000/api/wallet/" + walletAddress;
    console.log(apiUrl);

    fetch(apiUrl)

        .then(function (response) {
            return response.json();

        })

        .then(function (data) {
            if (data.error) {
                errorMessage.textContent = data.error;
                console.log(data.error);
                return;
            }
            console.log(data);
            ethBalance.textContent = data.eth_balance.toFixed(6);
            ethPrice.textContent = data.eth_price_eur;
            walletValue.textContent = data.wallet_value.toFixed(2);
        })

        .catch(function (error) {
            errorMessage.textContent = "Unable to connect to the wallet service. Please try again later.";
            console.log(error);
        })

        .finally(function () {
            loadingSpinner.style.display = "none";
        });
});