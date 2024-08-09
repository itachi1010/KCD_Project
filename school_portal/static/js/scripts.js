document.addEventListener('DOMContentLoaded', function() {
    const popupMessageContainer = document.getElementById('popup-message-container');
    if (popupMessageContainer) {
        setTimeout(function() {
            popupMessageContainer.style.display = 'none';
        }, 5000); // Hide the message after 5 seconds
    }
});
