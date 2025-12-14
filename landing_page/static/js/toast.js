function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toast-message');
    
    toastMessage.textContent = message;
    toast.className = 'toast-notification show ' + type;
    
    setTimeout(function() {
        toast.className = 'toast-notification';
    }, 4000);
}
