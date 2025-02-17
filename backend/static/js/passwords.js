document.addEventListener("DOMContentLoaded", function() {
    // Кнопка показа/скрытия пароля
    document.querySelectorAll('.show-password').forEach(button => {
        button.addEventListener('click', function() {
            const passwordField = this.previousElementSibling;
            if (passwordField.textContent === '••••••••') {
                passwordField.textContent = passwordField.dataset.password;
                this.innerHTML = '<i class="bi bi-eye-slash"></i>';
            } else {
                passwordField.textContent = '••••••••';
                this.innerHTML = '<i class="bi bi-eye"></i>';
            }
        });
    });

    // Кнопка копирования пароля
    document.querySelectorAll('.copy-password').forEach(button => {
        button.addEventListener('click', function() {
            const passwordField = this.previousElementSibling.previousElementSibling;
            const password = passwordField.dataset.password;

            if (!password) return;

            navigator.clipboard.writeText(password).then(() => {
                this.innerHTML = '<i class="bi bi-clipboard-check"></i>';
                setTimeout(() => {
                    this.innerHTML = '<i class="bi bi-clipboard"></i>';
                }, 2000);
            }).catch(err => console.error('Ошибка копирования:', err));
        });
    });
});