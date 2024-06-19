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


// Qui etes vous dans l'entreprise
// Projet petit(vous estimez moins de 2 semaines), moyen(entre 2 et 8 semaines) ou large(plus de 8 semaines) ?

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
