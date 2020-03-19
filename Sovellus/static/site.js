$('document').ready(function() {
    if (window.location != 'login' && sessionStorage.getItem('loginValid') !== 'true') {
        window.location = 'login';
    }
});