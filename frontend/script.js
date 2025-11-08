const socket = io("http://localhost:5000"); // Replace later with your Render backend URL
const SECRET = "supersecretkey123"; // same key used by both clients

let username = "";

function joinChat() {
  username = document.getElementById("username").value.trim();
  if (!username) return alert("Enter your name first!");

  document.getElementById("login-screen").classList.add("hidden");
  document.getElementById("chat-screen").classList.remove("hidden");
}

function encryptMessage(message) {
  return CryptoJS.AES.encrypt(message, SECRET).toString();
}

function decryptMessage(ciphertext) {
  try {
    return CryptoJS.AES.decrypt(ciphertext, SECRET).toString(CryptoJS.enc.Utf8);
  } catch {
    return "[Decryption Error]";
  }
}

function sendMessage() {
  const msg = document.getElementById("message").value.trim();
  if (!msg) return;

  const encrypted = encryptMessage(msg);
  socket.emit("message", { user: username, message: encrypted });
  document.getElementById("message").value = "";
}

socket.on("message", (data) => {
  const decrypted = decryptMessage(data.message);
  const messagesDiv = document.getElementById("messages");
  const msgElem = document.createElement("div");
  msgElem.classList.add("message");
  msgElem.innerHTML = `<b>${data.user}:</b> ${decrypted}`;
  messagesDiv.appendChild(msgElem);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
});
