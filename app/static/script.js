// Toggle chat window visibility and save the state
function toggleChat() {
  const chatWindow = document.getElementById("chat-window");
  const isCurrentlyVisible = chatWindow.style.display === "block";

  if (isCurrentlyVisible) {
    chatWindow.style.display = "none";
    sessionStorage.setItem("chatWindowState", "closed");
  } else {
    chatWindow.style.display = "block";
    sessionStorage.setItem("chatWindowState", "open");
  }
}
// Load chat window state from session storage
function loadChatWindowState() {
  const chatWindow = document.getElementById("chat-window");
  const chatWindowState = sessionStorage.getItem("chatWindowState");

  if (chatWindowState === "open") {
    chatWindow.style.display = "block";
  } else {
    chatWindow.style.display = "none";
  }
}

// Display a new chat message in the chat window
function displayMessage(sender, message) {
  const chatBox = document.getElementById("chat-box");
  const messageElem = document.createElement("div");
  messageElem.classList.add("mt-2");
  messageElem.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatBox.appendChild(messageElem);
  chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
}

// Save chat message to session storage
function saveMessageToStorage(sender, message) {
  const chatHistory = JSON.parse(sessionStorage.getItem("chatHistory")) || [];
  chatHistory.push({ sender, message });
  sessionStorage.setItem("chatHistory", JSON.stringify(chatHistory));
}

// Load chat history from session storage
function loadChatHistory() {
  const chatHistory = JSON.parse(sessionStorage.getItem("chatHistory")) || [];
  chatHistory.forEach(({ sender, message }) => {
    displayMessage(sender, message);
  });
}

// Send message to FastAPI chatbot backend
async function sendMessage() {
  const userMessageElem = document.getElementById("user-message");
  const userMessage = userMessageElem.value;
  displayMessage("User", userMessage); // Show user message in chat
  userMessageElem.value = ""; // Clear input field

  try {
    const response = await fetch("http://localhost:8000/chat/", {
      // Update to the correct URL and port
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userMessage }), // Ensure the key matches the API
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    displayMessage("Bot", data.response); // Show bot response in chat
    saveMessageToStorage("Bot", data.response); // Save bot response to session storage
  } catch (error) {
    console.error("Error:", error); // Log any errors that occur
    displayMessage("Bot", "Sorry, there was an error processing your request."); // Inform the user

    // Save message to session storage
    saveMessageToStorage("User", userMessage);
  }
}

// Listen for Enter key on the message input field
document
  .getElementById("user-message")
  .addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      event.preventDefault();
      sendMessage(); // Call sendMessage on Enter press
    }
  });

// Load chat history and chat window state when the page loads
window.onload = function () {
  loadChatWindowState(); // Ensure chat window state persists
  loadChatHistory(); // Load previous chat messages
};
