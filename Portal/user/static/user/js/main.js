
document.getElementById('toggle-password').addEventListener('click', function () {
    const passwordField = document.querySelector('input[name="password"]');
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);

    // Toggle the icon
    this.classList.toggle('zmdi-eye');
    this.classList.toggle('zmdi-eye-off');
})