function confirmarExclusao(event, url) {
    event.preventDefault(); // Impede o redirecionamento imediato
    if (confirm("Você tem certeza de que deseja excluir sua conta?")) {
        window.location.href = url; // Redireciona para a URL de exclusão se confirmado
    }
}
