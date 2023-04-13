// Eye following code
document.addEventListener('DOMContentLoaded', function() {
    function getCenter(element) {
        const {left, top, width, height} = element.getBoundingClientRect();
        return {x: left + width / 2, y: top + height / 2}
    }
    
    const leftEye = document.querySelector(".leftEye");
    const leftEyeCenter = getCenter(leftEye);
    addEventListener("mousemove", ({clientX, clientY}) => {
        if (leftEye.dataset.staring == "false") {
            const angle = Math.atan2(clientY - leftEyeCenter.y, clientX - leftEyeCenter.x);
            leftEye.style.transform = `rotate(${angle}rad)`;
        }
    });

    const rightEye = document.querySelector(".rightEye");
    const rightEyeCenter = getCenter(rightEye);
    addEventListener("mousemove", ({clientX, clientY}) => {
        if (rightEye.dataset.staring == "false") {
            const angle = Math.atan2(clientY - rightEyeCenter.y, clientX - rightEyeCenter.x);
            rightEye.style.transform = `rotate(${angle}rad)`;
        }
    });
});

// Message adding
document.addEventListener('DOMContentLoaded', function() {
    const enterButton = document.getElementById("enterButton");
    const inputText = document.getElementById("inputText");
    const messagesDiv = document.getElementById("messages");

    function addBotMessage(responseText) {
        const userMessageDiv = document.createElement("div");
        userMessageDiv.classList.add("message");
        userMessageDiv.classList.add("botMessage");
        messagesDiv.appendChild(userMessageDiv);
    
        const mouthWaves = mouth.querySelectorAll(".mouthWave");
        for (let i = 0; i < mouthWaves.length; i++) {
            const mouthWave = mouthWaves[i];
            mouthWave.style.opacity = 1;
        }
        const smile = mouth.querySelector(".smile");
        smile.style.opacity = 0;
        inputText.disabled = true;
    
        var response;
        response = "My name is PARAM, and I am an example of \"Parthificial Intelligence.\" This type of AI is based on the niche micro-celebrity you all know and love: \"Parth Shah,\" which means that my intelligence is modeled after his.";
        let index = 0;
    
        const typingInterval = setInterval(function() {
            if (index === response.length) {
                clearInterval(typingInterval);
                const mouthWaves = mouth.querySelectorAll(".mouthWave");
                for (let i = 0; i < mouthWaves.length; i++) {
                    const mouthWave = mouthWaves[i];
                    mouthWave.style.opacity = 0;
                }
                inputText.disabled = false;
                smile.style.opacity = 1;
                return;
            }
            const character = response[index];
            const space = /^\s*$/.test(character) ? "&nbsp;" : character;
            userMessageDiv.innerHTML += space;
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
            index++;
        }, 100);
    }
    
             

    function addUserMessage() {
        if (inputText.value.length > 0) {
            const userMessageDiv = document.createElement("div");
            userMessageDiv.classList.add("message");
            userMessageDiv.classList.add("userMessage");
            userMessageDiv.innerText = inputText.value;
            messagesDiv.appendChild(userMessageDiv);
            addBotMessage();
            inputText.value = '';
        }
        messagesDiv.scrollTop = messagesDiv.scrollHeight;

    }

    enterButton.addEventListener("click", addUserMessage);
    inputText.addEventListener("keydown", function(event) {
        if (event.keyCode === 13) {
            addUserMessage();
        }
    });
});

// Color mode
document.addEventListener('DOMContentLoaded', function() {
    var colorMode = document.getElementById("colorMode");
    
    colorMode.addEventListener("click", function(){
        if (colorMode.innerText == "Dark Mode") {
            document.documentElement.style.setProperty('--paramBGColor', '#313333');
            document.documentElement.style.setProperty('--panelColor', '#0f0f0f');
            document.documentElement.style.setProperty('--chatColor', '#4d4f4f');
            document.documentElement.style.setProperty('--userMessageColor', '#262638');
            document.documentElement.style.setProperty('--botMessageColor', '#3b2438');
            document.documentElement.style.setProperty('--messageTextColor', '#ffffff');
            colorMode.innerText = "Light Mode"
        } else {
            document.documentElement.style.setProperty('--paramBGColor', '#c4cccc');
            document.documentElement.style.setProperty('--panelColor', '#a8a7a7');
            document.documentElement.style.setProperty('--chatColor', '#e3e8e8');
            document.documentElement.style.setProperty('--userMessageColor', '#6a6b9e');
            document.documentElement.style.setProperty('--botMessageColor', '#ba72b0');
            document.documentElement.style.setProperty('--messageTextColor', '#000000');
            colorMode.innerText = "Dark Mode"
        }
    });
});

// Scary mode
document.addEventListener('DOMContentLoaded', function() {
    var scaryMode = document.getElementById("scaryMode");
    var leftEye = document.getElementById("leftEye");
    var rightEye = document.getElementById("rightEye");
    var mouth = document.getElementById("mouth");
    var smile = document.getElementById("smile");
    
    if (scaryMode && leftEye && rightEye && mouth && smile) {
        scaryMode.addEventListener("click", function(){
            if (scaryMode.innerText == "Scary Mode") {
                leftEye.style.boxShadow = "none";
                rightEye.style.boxShadow = "none";
                leftEye.style.backgroundImage = "url('realisticEye.png')";
                rightEye.style.backgroundImage = "url('realisticEye.png')";
                leftEye.dataset.staring = "true";
                rightEye.dataset.staring = "true";
                smile.src = "realisticSmile.png";
                smile.style.width = "70%";
                smile.style.bottom = "-10%";
                mouth.style.filter = "none";
                scaryMode.innerText = "Normal Mode"
            } else {
                rightEye.style.boxShadow = "10px 0px 5px inset white";
                leftEye.style.boxShadow = "10px 0px 5px inset white";
                leftEye.style.backgroundImage = "url('')";
                rightEye.style.backgroundImage = "url('')";
                leftEye.dataset.staring = "false";
                rightEye.dataset.staring = "false";
                smile.src = "smile.svg";
                smile.style.bottom = "10%";
                smile.style.width = "100%";
                mouth.style.filter = "filter: grayscale(100%) invert(0%)";
                scaryMode.innerText = "Scary Mode"
            }
        });
    }
});
