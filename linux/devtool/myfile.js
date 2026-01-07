// Get the button element
const startButton = document.getElementById('startButton');

// Add click event listener
startButton.addEventListener('click', function() {
    console.log('Welcome to the Chrome Developer Console!');
    console.log('Press F12 or right-click and select "Inspect" to open it.');
    console.log('This is where you can debug JavaScript, view errors, and test code!');
    
    // Change button text after click
    startButton.textContent = 'Check the Console! (F12)';
    startButton.style.backgroundColor = '#2ecc71';
    
    // Log some fun examples
    setTimeout(() => {
        console.log('------- Let\'s try some examples! -------');
        console.log('Example 1: Basic math:', 5 + 3);
        console.log('Example 2: String manipulation:', 'Hello, ' + 'Developer!');
        console.warn('This is a warning message!');
        console.error('This is an error message!');
        console.table({name: 'John', age: 25, role: 'Developer'});
    }, 1000);
});

// Log initial message when page loads
console.log('Page loaded! Click the button to start your learning journey.');
console.log('Tip: You can type JavaScript directly in the console to execute it!');