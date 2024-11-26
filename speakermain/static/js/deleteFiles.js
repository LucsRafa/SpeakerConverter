document.addEventListener("DOMContentLoaded", () => {
  const deleteButtons = document.querySelectorAll(".btn-delete");

  deleteButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const fileId = button.getAttribute("data-id"); // Obtém o ID do arquivo

      // Confirmação de exclusão
      if (confirm("Você tem certeza que deseja excluir este arquivo?")) {
        fetch("/delete-file/", {
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCookie("csrftoken"), // Captura o token CSRF
          },
          body: `id=${fileId}`, // Passa o ID do arquivo para a requisição
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.status === "success") {
              alert(data.message);
              location.reload(); // Atualiza a página
            } else {
              alert(data.message); // Exibe mensagem de erro caso falhe
            }
          })
          .catch((error) => console.error("Erro:", error)); // Em caso de erro na requisição
      }
    });
  });

  // Função para obter o token CSRF
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
