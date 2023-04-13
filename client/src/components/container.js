


const Container = () => {
    return (
        <div id="wrapper">
            <div id="voiceContainer">
                <div class="button-container">
                    <input type="checkbox" id="micButton" class="mic-checkbox"/>
                    <label for="micButton" class="mic-button">
                    <div class='mic'>
                        <div class='mic-button-loader'>
                        </div>
                        <div class="mic-base">
                        </div>
                        </div>
                    <div class="button-message">
                        <span>
                            PRESS TO TALK
                        </span>
                    </div>
                    </label>
                </div>
            </div>
            <div id="messageContainer">
                <h3>Message Reply Container</h3>
                <p>Here you would see the "message bubbles" between oneself and the AI</p>
                <br></br>
            </div>
            <div id="searchContainer">
                <h3>Query Container</h3>
                <p>Here the user can choose to type their query. Or they can use the microphone up top.
                    <br></br>
                    Microphone will most likely migrate to the right side of this container
                </p>
                <br></br>
            </div>
        </div>
    );
}
 
export default Container;