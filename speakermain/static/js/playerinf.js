$(document).ready(function() {
    $('.audio-link').click(function(e) {
        e.preventDefault();
        var audioId = $(this).data('id');
        
        $.ajax({
            url: '/audio-detail/' + audioId + '/',
            method: 'GET',
            success: function(data) {
                $('#det').html('<h4>' + data.nome + '</h4><p>' + data.corpo + '</p>');
                $('#audio-source').attr('src', data.caminho);
                $('#audio-player')[0].load();
            }
        });
    });
});
