document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("login-frm");

    if (loginForm) {
        loginForm.addEventListener("submit", function(e) {
            e.preventDefault();
            const submitButton = loginForm.querySelector('button[type="submit"]');
            submitButton.setAttribute('disabled', true);
            submitButton.innerHTML = 'Logging in...';

            const formData = new FormData(loginForm);
            fetch('/login/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/home/';
                } else {
                    const errorMessage = document.createElement("div");
                    errorMessage.classList.add("alert", "alert-danger");
                    errorMessage.textContent = data.error;
                    loginForm.prepend(errorMessage);
                    submitButton.removeAttribute('disabled');
                    submitButton.innerHTML = 'Login';
                }
            })
            .catch(error => {
                console.error("Error:", error);
                submitButton.removeAttribute('disabled');
                submitButton.innerHTML = 'Login';
            });
        });
    }
});
