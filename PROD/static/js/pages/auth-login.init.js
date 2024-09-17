/*
Template Name: Tailwick - Admin & Dashboard Template
Author: Themesdesign
Version: 1.1.0
Website: https://themesdesign.in/
Contact: Themesdesign@gmail.com
File: auth login init Js File
*/
document.getElementById('signInForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting

    // Get input values
    const email = document.getElementById('email').value;  // Correct field ID
    const password = document.getElementById('password').value;  // Correct field ID

    // Define regular expressions for validation
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    const strongPasswordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

    // Validate email and password
    const emailError = document.getElementById('email-error');
    const passwordError = document.getElementById('password-error');
    const successAlert = document.getElementById('successAlert');
    const rememberMeCheckbox = document.getElementById('checkboxDefault1');
    const rememberError = document.getElementById('remember-error');

    emailError.classList.add('hidden'); // Hide any previous error message
    passwordError.classList.add('hidden');
    successAlert.classList.add('hidden'); // Hide the success message

    // Validation logic
    if (!emailRegex.test(email)) {
        emailError.classList.remove('hidden'); // Show email error message
    } else if (!strongPasswordRegex.test(password)) {
        passwordError.classList.remove('hidden'); // Show password error message
    } else {
        // Form is valid, show the success message
        successAlert.classList.remove('hidden');
    }

    // Check if "Remember me" is checked
    if (!rememberMeCheckbox.checked) {
        rememberError.classList.remove('hidden'); // Show error if not checked
    } else {
        rememberError.classList.add('hidden');
    }
});









 /*
document.getElementById('signInForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting

    // Get input values
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Define regular expressions for validation
    const strongPasswordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

    // Validate username and password
    const usernameError = document.getElementById('username-error');
    const passwordError = document.getElementById('password-error');
    const successAlert = document.getElementById('successAlert');
    const rememberMeCheckbox = document.getElementById('checkboxDefault1');
    const rememberError = document.getElementById('remember-error');

    usernameError.classList.add('hidden'); // Hide any previous error message
    passwordError.classList.add('hidden');
    successAlert.classList.add('hidden'); // Hide the success message

    // Assume any non-empty username is valid; adjust validation as needed
    if (username.trim() === '') {
        usernameError.classList.remove('hidden'); // Show error message
    } else if (!strongPasswordRegex.test(password)) {
        passwordError.classList.remove('hidden'); // Show error message
    } else {
        // Form is valid, show the success message
        successAlert.classList.remove('hidden');
    }

    if (!rememberMeCheckbox.checked) {
        // Prevent the form from submitting if the checkbox is not checked
        rememberError.classList.remove('hidden');
    } else {
        rememberError.classList.add('hidden');
    }
});





/*
document.getElementById('signInForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting

    // Get input values
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Define regular expressions for validation
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    const strongPasswordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

    // Validate username/email and password
    const usernameError = document.getElementById('username-error');
    const passwordError = document.getElementById('password-error');
    const successAlert = document.getElementById('successAlert');
    const rememberMeCheckbox = document.getElementById('checkboxDefault1');
    const rememberError = document.getElementById('remember-error');

    usernameError.classList.add('hidden'); // Hide any previous error message
    passwordError.classList.add('hidden');
    successAlert.classList.add('hidden'); // Hide the success message

    if (!emailRegex.test(username)) {
        usernameError.classList.remove('hidden'); // Show error message
    } else if (!strongPasswordRegex.test(password)) {
        passwordError.classList.remove('hidden'); // Show error message
    } else {
        // Form is valid, show the success message
        successAlert.classList.remove('hidden');
    }

    if (!rememberMeCheckbox.checked) {
        // Prevent the form from submitting if the checkbox is not checked
        event.preventDefault();
        rememberError.classList.remove('hidden');
    } else {
        rememberError.classList.add('hidden');
    }
}); */