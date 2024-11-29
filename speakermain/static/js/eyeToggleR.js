function togglePassword(passwordFieldId, eyeIconId) {
    var passwordField = document.getElementById(passwordFieldId);
    var eyeIcon = document.getElementById(eyeIconId);
  
    // Alterna entre mostrar e esconder a senha
    if (passwordField.type === "password") {
      passwordField.type = "text";
      eyeIcon.classList.remove("fa-eye");  // Remove ícone de olho fechado
      eyeIcon.classList.add("fa-eye-slash");  // Adiciona ícone de olho aberto
    } else {
      passwordField.type = "password";
      eyeIcon.classList.remove("fa-eye-slash");
      eyeIcon.classList.add("fa-eye");
    }
  }
  