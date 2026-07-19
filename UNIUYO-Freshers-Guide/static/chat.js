// ==============================
// ELEMENTS
// ==============================

const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const typing = document.getElementById("typing");
const suggestions = document.querySelectorAll(".suggestion");

// ==============================
// AUTO RESIZE TEXTAREA
// ==============================

userInput.addEventListener("input", () => {
    userInput.style.height = "auto";
    userInput.style.height = userInput.scrollHeight + "px";
});

// ==============================
// CREATE MESSAGE
// ==============================

function addMessage(message, sender){

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");
    messageDiv.classList.add(sender);

    const bubble = document.createElement("div");

    bubble.classList.add("bubble");

    bubble.innerHTML = message.replace(/\n/g, "<br>");

    messageDiv.appendChild(bubble);

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;

}

// ==============================
// SHOW TYPING
// ==============================

function showTyping(){

    typing.style.display = "block";

    chatBox.scrollTop = chatBox.scrollHeight;

}

function hideTyping(){

    typing.style.display = "none";

}

// ==============================
// SEND MESSAGE
// ==============================

async function sendMessage(){

    const message = userInput.value.trim();

    if(message === "")
        return;

    addMessage(message,"user");

    userInput.value = "";

    userInput.style.height = "55px";

    showTyping();

    try{

        const response = await fetch("/chat",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                message:message
            })

        });

        const data = await response.json();

        hideTyping();

        addMessage(data.reply,"ai");

    }

    catch(error){

        hideTyping();

        addMessage(
            "Sorry, I couldn't connect to the AI server. Please try again.",
            "ai"
        );

        console.error(error);

    }

}

// ==============================
// SEND BUTTON
// ==============================

sendBtn.addEventListener("click",sendMessage);

// ==============================
// ENTER TO SEND
// ==============================

userInput.addEventListener("keydown",function(event){

    if(event.key==="Enter" && !event.shiftKey){

        event.preventDefault();

        sendMessage();

    }

});

// ==============================
// SUGGESTION BUTTONS
// ==============================

suggestions.forEach(button=>{

    button.addEventListener("click",()=>{

        userInput.value = button.innerText;

        sendMessage();

    });

});