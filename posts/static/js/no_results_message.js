document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
      var messageElement = document.getElementById("no-results-message");
      if (messageElement) {
        messageElement.style.display = 'none';
      }
    }, 3000);
  });