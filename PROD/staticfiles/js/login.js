
document.addEventListener('DOMContentLoaded', function() {
  var current = null;
  
  var emailInput = document.querySelector('#id_username'); // Update to match Django form field ID
  var passwordInput = document.querySelector('#id_password'); // Update to match Django form field ID
  var submitButton = document.querySelector('#submit'); // Ensure this matches the submit button's ID
  
  // Safely attach event listeners if elements exist
  if (emailInput) {
    emailInput.addEventListener('focus', function(e) {
      if (current) current.pause();
      current = anime({
        targets: 'path',
        strokeDashoffset: {
          value: 0,
          duration: 700,
          easing: 'easeOutQuart'
        },
        strokeDasharray: {
          value: '240 1386',
          duration: 700,
          easing: 'easeOutQuart'
        }
      });
    });
  } else {
    console.error('#id_username not found');
  }

  if (passwordInput) {
    passwordInput.addEventListener('focus', function(e) {
      if (current) current.pause();
      current = anime({
        targets: 'path',
        strokeDashoffset: {
          value: -336,
          duration: 700,
          easing: 'easeOutQuart'
        },
        strokeDasharray: {
          value: '240 1386',
          duration: 700,
          easing: 'easeOutQuart'
        }
      });
    });
  } else {
    console.error('#id_password not found');
  }

  if (submitButton) {
    submitButton.addEventListener('focus', function(e) {
      if (current) current.pause();
      current = anime({
        targets: 'path',
        strokeDashoffset: {
          value: -730,
          duration: 700,
          easing: 'easeOutQuart'
        },
        strokeDasharray: {
          value: '530 1386',
          duration: 700,
          easing: 'easeOutQuart'
        }
      });
    });
  } else {
    console.error('#submit not found');
  }
});







/*
document.addEventListener('DOMContentLoaded', function() {
  var current = null;
  
  var emailInput = document.querySelector('#email');
  var passwordInput = document.querySelector('#password');
  var submitButton = document.querySelector('#submit');
  
  // Check if #email exists before adding the event listener
  if (emailInput) {
    emailInput.addEventListener('focus', function(e) {
      if (current) current.pause();
      current = anime({
        targets: 'path',
        strokeDashoffset: {
          value: 0,
          duration: 700,
          easing: 'easeOutQuart'
        },
        strokeDasharray: {
          value: '240 1386',
          duration: 700,
          easing: 'easeOutQuart'
        }
      });
    });
  }

  // Check if #password exists before adding the event listener
  if (passwordInput) {
    passwordInput.addEventListener('focus', function(e) {
      if (current) current.pause();
      current = anime({
        targets: 'path',
        strokeDashoffset: {
          value: -336,
          duration: 700,
          easing: 'easeOutQuart'
        },
        strokeDasharray: {
          value: '240 1386',
          duration: 700,
          easing: 'easeOutQuart'
        }
      });
    });
  }

  // Check if #submit exists before adding the event listener
  if (submitButton) {
    submitButton.addEventListener('focus', function(e) {
      if (current) current.pause();
      current = anime({
        targets: 'path',
        strokeDashoffset: {
          value: -730,
          duration: 700,
          easing: 'easeOutQuart'
        },
        strokeDasharray: {
          value: '530 1386',
          duration: 700,
          easing: 'easeOutQuart'
        }
      });
    });
  }
});

*/