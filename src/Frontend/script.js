function hamburgerClick() {
  let navbar = document.getElementById("navbar");
  let leftNavbar = document.getElementById("left-navbar");
  let navbarOptions = document.getElementById("navbar-option");

  if (navbar.className === "navbar") {
    navbar.className += " responsive";
    leftNavbar.className += " responsive";
    navbarOptions.className += " responsive";
  } else {
    navbar.className = "navbar";
    leftNavbar.className = "left-navbar";
    navbarOptions.className = "navbar-option";
  }
}

// Load header & footer
document.addEventListener("DOMContentLoaded", () => {
  fetch("header.html")
    .then((response) => response.text())
    .then((data) => {
      document.getElementById("header").innerHTML = data;
    });

  fetch("footer.html")
    .then((response) => response.text())
    .then((data) => {
      document.getElementById("footer").innerHTML = data;
    });
});

// Payment info
function toggleEditInfo() {
  const editInfo = document.getElementById("edit-info");
  editInfo.classList.toggle("hidden");
  if (!editInfo.classList.contains("hidden")) {
    editInfo.scrollIntoView({ behavior: "smooth" });
  }
}

function saveInfo() {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  alert(`Info Saved:\nName: ${name}\nEmail: ${email}`);
}

function toggleAddPaymentForm() {
  const addPayment = document.getElementById("add-payment");
  addPayment.classList.toggle("hidden");
  if (!addPayment.classList.contains("hidden")) {
    addPayment.scrollIntoView({ behavior: "smooth" });
  }
}

function addPaymentOption() {
  const cardName = document.getElementById("card-name").value;
  const cardNumber = document.getElementById("card-number").value;
  const maskedCard = `**** ${cardNumber.slice(-4)}`;

  const paymentOptions = document.getElementById("payment-options");
  const newOption = document.createElement("div");
  newOption.classList.add("payment-option");
  newOption.innerHTML = `
            <span>${cardName} ${maskedCard}</span>
            <button onclick="removePaymentOption(this)">Remove</button>
        `;
  paymentOptions.appendChild(newOption);

  // Clear form
  document.getElementById("payment-form").reset();
  toggleAddPaymentForm();
}

function removePaymentOption(button) {
  const option = button.parentElement;
  option.remove();
}

function logout() {
  localStorage.removeItem("user");
  alert("You have been logged out");
  window.localStorage.href = "login.html";
}

// Simulate retrieving saved credit card details from the server
const savedCardDetails = {
  last4: "1234", // Example last 4 digits of the card
};

window.onload = function () {
  // Display saved card details if they exist
  if (savedCardDetails && savedCardDetails.last4) {
    document.getElementById("savedPaymentOption").style.display = "block";
    document.getElementById("cardLast4").textContent = savedCardDetails.last4;
  }
};

document
  .getElementById("bookingForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    // Collect form data
    const formData = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      roomType: document.getElementById("roomType").value,
      checkIn: document.getElementById("checkIn").value,
      checkOut: document.getElementById("checkOut").value,
      paymentOption:
        document.querySelector('input[name="paymentOption"]:checked')?.value ||
        "new",
      cardNumber: document.getElementById("cardNumber").value,
      expiryDate: document.getElementById("expiryDate").value,
      cvv: document.getElementById("cvv").value,
      saveCard: document.getElementById("saveCard").checked,
    };

    // Submit data to the backend
    const response = await fetch("/book-room", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });

    if (response.ok) {
      alert("Room booked successfully!");
      // Optionally redirect to another page
    } else {
      alert("Failed to book the room. Please try again.");
    }
  });
