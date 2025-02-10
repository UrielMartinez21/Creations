import confetti from 'https://cdn.skypack.dev/canvas-confetti';

document.addEventListener("DOMContentLoaded", function () {
    const yesButton = document.getElementById('yesButton');
    const noButton = document.getElementById('noButton');
    const imageDisplay = document.getElementById('imageDisplay');
    const valentineQuestion = document.getElementById('valentineQuestion');
    const responseButtons = document.getElementById('responseButtons');

    let noClickCount = 0;
    let buttonHeight = 48; // Starting height in pixels
    let buttonWidth = 80;
    let fontSize = 20; // Starting font size in pixels
    const imagePaths = [
        "/static/images/valentine/v1/image1.gif",
        "/static/images/valentine/v1/image2.gif",
        "/static/images/valentine/v1/image3.gif",
        "/static/images/valentine/v1/image4.gif",
        "/static/images/valentine/v1/image5.gif",
        "/static/images/valentine/v1/image6.gif",
        "/static/images/valentine/v1/image7.gif"
    ];

    noButton.addEventListener('click', function () {
        if (noClickCount < 5) {
            noClickCount++;
            imageDisplay.src = imagePaths[noClickCount];
            buttonHeight += 35;
            buttonWidth += 35;
            fontSize += 25;
            yesButton.style.height = `${buttonHeight}px`;
            yesButton.style.width = `${buttonWidth}px`;
            yesButton.style.fontSize = `${fontSize}px`;
            if (noClickCount < 6) {
                noButton.textContent = [
                    "No",
                    "Are you sure?",
                    "Pookie please",
                    "Don't do this to me :(",
                    "You're breaking my heart",
                    "I'm gonna cry..."
                ][noClickCount];
            }
        }
    });

    yesButton.addEventListener('click', () => {
        imageDisplay.src = '/static/images/valentine/v1/image7.gif';
        valentineQuestion.textContent = "Yayyy!! :3";
        responseButtons.style.display = 'none';
        confetti();
    });
});
