document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.btn-delete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', () => {
            const fileId = button.getAttribute('data-id');

            if (confirm('Você tem certeza que deseja excluir este arquivo?')) {
                fetch('/delete-file/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': getCookie('csrftoken')  // Captura o token CSRF
                    },
                    body: `id=${fileId}`
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        alert(data.message);
                        button.parentElement.remove();  // Remove o arquivo da lista
                    } else {
                        alert(data.message);
                    }
                })
                .catch(error => console.error('Erro:', error));
            }
        });
    });

    // Função para obter o token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
