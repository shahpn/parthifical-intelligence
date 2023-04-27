// import '../scripts/scripts.js'
import React, { useState, useEffect } from 'react'
import smile from '../assets/smile.svg';
import wave from '../assets/wave.svg';
import realisticEye from '../assets/realisticEye.png';
import realisticSmile from '../assets/realisticSmile.png';


const Container = () => {
    function getCenter(element) {
        if (element) {
          const { left, top, width, height } = element.getBoundingClientRect();
          return { x: left + width / 2, y: top + height / 2 };
        }
        return { x: 0, y: 0 };
      }
      
      var leftEye = document.querySelector('.leftEye');
      var leftEyeCenter = getCenter(leftEye);
      
      if (leftEye) {
        // eslint-disable-next-line no-restricted-globals
        addEventListener('mousemove', ({ clientX, clientY }) => {
          if (leftEye.dataset.staring === 'false') {
            const angle = Math.atan2(clientY - leftEyeCenter.y, clientX - leftEyeCenter.x);
            leftEye.style.transform = `rotate(${angle}rad)`;
          }
        });
      }
      
      var rightEye = document.querySelector('.rightEye');
      var rightEyeCenter = getCenter(rightEye);
      
      if (rightEye) {
        // eslint-disable-next-line no-restricted-globals
        addEventListener('mousemove', ({ clientX, clientY }) => {
          if (rightEye.dataset.staring === 'false') {
            const angle = Math.atan2(clientY - rightEyeCenter.y, clientX - rightEyeCenter.x);
            rightEye.style.transform = `rotate(${angle}rad)`;
          }
        });
      }
      
    // Message adding
    var scaryMode = document.getElementById("scaryMode");
    // var leftEye = document.getElementById("leftEye");
    // var rightEye = document.getElementById("rightEye");
    
    function addBotMessage(responseText) {
        var mouth = document.getElementById("mouth");
        var enterButton = document.getElementById("enterButton");
        var inputText = document.getElementById("inputText");
        var messagesDiv = document.getElementById("messages");
        const userMessageDiv = document.createElement("div");
        userMessageDiv.classList.add("message");
        userMessageDiv.classList.add("botMessage");
        messagesDiv.appendChild(userMessageDiv);
        userMessageDiv.style.whiteSpace = 'pre-wrap';
    
        const mouthWaves = mouth.querySelectorAll(".mouthWave");
        for (let i = 0; i < mouthWaves.length; i++) {
            const mouthWave = mouthWaves[i];
            mouthWave.style.opacity = 1;
        }
        const smile = mouth.querySelector(".smile");
        smile.style.opacity = 0;
        inputText.disabled = true;
    
        var response = responseText;
        // response = "My name is PARAM, and I am an example of \"Parthificial Intelligence.\" This type of AI is based on the niche micro-celebrity you all know and love: \"Parth Shah,\" which means that my intelligence is modeled after his.";
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
            // const character = response[index];
            // const space = /^\s*$/.test(character) ? "&nbsp;" : character;
            // userMessageDiv.innerHTML += space;
            userMessageDiv.innerHTML += response[index];
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
            index++;
        }, 100);
    }
        
                 
    
    function addUserMessage() {
        var mouth = document.getElementById("mouth");
        var enterButton = document.getElementById("enterButton");
        var inputText = document.getElementById("inputText");
        var messagesDiv = document.getElementById("messages");
        
        var botResponse;
        
        var inputStr = String(inputText.value);

        fetch("/userInput", {
          method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ payload: inputText.value }),
          })
            .then((response) => response.text())
            .then((text) => {
              botResponse = text;
              if (inputText.value.length > 0) {
                  const userMessageDiv = document.createElement("div");
                  userMessageDiv.classList.add("message");
                  userMessageDiv.classList.add("userMessage");
                  userMessageDiv.innerText = inputText.value;
                  messagesDiv.appendChild(userMessageDiv);
                  console.log(botResponse)
                  addBotMessage(botResponse);
                  inputText.value = '';
                  messagesDiv.scrollTop = messagesDiv.scrollHeight;
              }
            })
            .catch((error) => console.error(error));
            return;

        // if (inputStr.includes('courses')) {
        //   fetch("/get_courses", {
        //     method: "POST",
        //     headers: {
        //       "Content-Type": "application/json",
        //     },
        //     body: JSON.stringify({ payload: inputText.value }),
        //   })
        //     .then((response) => response.json())
        //     .then((json) => {
        //       botResponse = json;
        //       if (inputText.value.length > 0) {
        //           const userMessageDiv = document.createElement("div");
        //           userMessageDiv.classList.add("message");
        //           userMessageDiv.classList.add("userMessage");
        //           userMessageDiv.innerText = inputText.value;
        //           messagesDiv.appendChild(userMessageDiv);
        //           console.log(Object.keys(botResponse))
        //           addBotMessage(Object.keys(botResponse).join('\n'));
        //           inputText.value = '';
        //           messagesDiv.scrollTop = messagesDiv.scrollHeight;
        //       }
        //     })
        //     .catch((error) => console.error(error));
        //     return;
        // }

        // else if (inputStr.includes('all assignments')) {
        //   fetch("/get_assignments", {
        //     method: "POST",
        //     headers: {
        //       "Content-Type": "application/json",
        //     },
        //     body: JSON.stringify({ payload: inputText.value }),
        //   })
        //     .then((response) => response.text())
        //     .then((text) => {
        //       botResponse = text;
        //       if (inputText.value.length > 0) {
        //           const userMessageDiv = document.createElement("div");
        //           userMessageDiv.classList.add("message");
        //           userMessageDiv.classList.add("userMessage");
        //           userMessageDiv.innerText = inputText.value;
        //           messagesDiv.appendChild(userMessageDiv);
        //           console.log(botResponse)
        //           addBotMessage(botResponse);
        //           inputText.value = '';
        //           messagesDiv.scrollTop = messagesDiv.scrollHeight;
        //       }
        //     })
        //     .catch((error) => console.error(error));
        //     return;
        // }
        

        // else if (inputStr.includes('assignment')) {
        //   fetch("/get_assignments", {
        //     method: "POST",
        //     headers: {
        //       "Content-Type": "application/json",
        //     },
        //     body: JSON.stringify({ payload: inputText.value }),
        //   })
        //     .then((response) => response.text())
        //     .then((text) => {
        //       botResponse = text;
        //       if (inputText.value.length > 0) {
        //           const userMessageDiv = document.createElement("div");
        //           userMessageDiv.classList.add("message");
        //           userMessageDiv.classList.add("userMessage");
        //           userMessageDiv.innerText = inputText.value;
        //           messagesDiv.appendChild(userMessageDiv);
        //           console.log(botResponse)
        //           addBotMessage(botResponse);
        //           inputText.value = '';
        //           messagesDiv.scrollTop = messagesDiv.scrollHeight;
        //       }
        //     })
        //     .catch((error) => console.error(error));
        //     return;
        // }

        

        
        
    
    }
    
    function enterPress(event) {
        if (event.keyCode === 13) {
            addUserMessage();
        }
    }
        

    return (
        <div id="wrapper">
        <div id="voiceContainer">
            <div id="mainWindow" class="mainWindow">
                <div id="facePanel" class="facePanel">
                    <div id="face" class="face">
                        <div id="leftEye" data-staring="false" class="eye leftEye"></div>
                        <div id="rightEye" data-staring="false" class="eye rightEye"></div>
                        <div id="mouth" class="mouth">
                            <img id="smile" class="smile" src={smile}/>
                            <img id="mouthWave1" class="mouthWave" src={wave} />
                            <img id="mouthWave2" class="mouthWave" src={wave} />
                            <img id="mouthWave3" class="mouthWave" src={wave} />
                            <img id="mouthWave4" class="mouthWave" src={wave} />
                        </div>
                    </div>
                </div>
                <div id="leftPanel" class="panel leftPanel">
                    {/* <button id="colorMode" class="button">Dark Mode</button>
                    <button id="scaryMode" class="button">Scary Mode</button> */}
                </div>
                <div id="rightPanel" class="panel rightPanel"></div>
                </div>

            </div>
            <div id="textPanel" class="textPanel">
                    <div id="messages" class="messages">
                    </div>
                    <div id="userInput" class="userInput">
                        <input id="inputText" class="inputText" onKeyDown={enterPress}/>
                        <button id="enterButton" class="enterButton" onClick={addUserMessage}></button>
                    </div>
            </div>
        </div>
        
    );
}
 
export default Container;