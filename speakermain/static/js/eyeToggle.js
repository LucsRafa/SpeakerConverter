function togglePassword() {
  var passwordField = document.getElementById("id_password");
  var eyeIcon = document.getElementById("eye-icon");

  // Alternar entre mostrar e esconder a senha
  if (passwordField.type === "password") {
    passwordField.type = "text";
    eyeIcon.classList.remove("fa-eye");  // Remover ícone de olho fechado
    eyeIcon.classList.add("fa-eye-slash");  // Adicionar ícone de olho aberto
  } else {
    passwordField.type = "password";
    eyeIcon.classList.remove("fa-eye-slash");
    eyeIcon.classList.add("fa-eye");
  }
}