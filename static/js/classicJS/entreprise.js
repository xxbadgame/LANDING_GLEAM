const textarea = document.querySelector("#questionEntreprise textarea");
const svgSiri = document.querySelector(".svgSiri");
const ombreSiri = document.querySelector(".ombreSiri");
const cercleOmbreSiri = document.querySelector(".cercleOmbreSiri");


textarea.addEventListener("input", e => {
    e.target.style.height = '7vh'; // Réinitialiser la hauteur
    e.target.style.height = `${e.target.scrollHeight}px`; // Définir la nouvelle hauteur basée sur scrollHeight

});

textarea.addEventListener("keydown", () => {

    // Appliquer une mise à l'échelle
    svgSiri.setAttribute('transform', 'scale(1.2)');
    cercleOmbreSiri.classList.add('ombreSiri');

    // Réinitialiser la mise à l'échelle après une courte période pour permettre le redémarrage
    setTimeout(() => {
        svgSiri.setAttribute('transform', 'scale(1)');
        cercleOmbreSiri.classList.remove('ombreSiri');
    }, 600); // Durée de l'animation
});


$(document).ready(function() {

    $('#questionEntreprise').on('submit', function(event) {
        event.preventDefault();

        var message = $('#chatInput').val();
        $('#chatInput').val('');

        $.ajax(
            
          {
            url: botCreationProjetUrl,
            type: "POST",
            data: {
                message: message,
                thread_id: threadId,
                csrfmiddlewaretoken: csrfToken
            },
            
            success: function(response) {

                $('#responseArea').append('<p>' + response + '</p>');

            },
            error: function(xhr, errmsg, err) {
                $('#responseArea').append('<p>Erreur: ' + errmsg + '</p>');
            }

            
        });
    });
});
