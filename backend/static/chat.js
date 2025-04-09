function sendQuestion() {
    let question = document.getElementById("question").value;

    let chatBox = document.getElementById("chat-box");
    let userMessage = `<div class="chat-message user-message">${question}</div>`;
    chatBox.innerHTML += userMessage;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = `<div class="chat-message bot-message">${data.reponse}</div>`;
        chatBox.innerHTML += botMessage;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    document.getElementById("question").value = "";
}
