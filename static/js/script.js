let secretNumber;

window.onload = function() {
    fetch('/secret')
        .then(response => response.json())
        .then(data => {
            secretNumber = data.secret_number;
        });
};

function makeGuess() {
    const guess = document.getElementById('guess').value;
    fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            guess: guess,
            secret_number: secretNumber
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.result;
    });
}
