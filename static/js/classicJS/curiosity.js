const textarea = document.querySelector("#questionEntreprise textarea");
const svgSiri = document.querySelector(".svgSiri");
const ombreSiri = document.querySelector(".ombreSiri");
const cercleOmbreSiri = document.querySelector(".cercleOmbreSiri");


document.addEventListener('DOMContentLoaded', function() {
    var typed = new Typed('#curiosityText', {
      strings: ['Bonjour '+ userFirstName +' !',' Je m\'appelle <span style="color:#FE981E;">Curiosity</span>.', 'Parlons de votre <span style="color:#E60CFE;">entreprise</span> !','Hello '+ userFirstName +' !','My name is<span style="color:#7030F3;"> Curiosity</span>.', 'Let\'s talk about your<span style="color:#FE981E;"> business</span> !'],
      typeSpeed: 50,
      backSpeed: 25,
      backDelay: 2000,
      loop: true
    });
  });

textarea.addEventListener("focus", function(){
    document.getElementById("questionEntreprise").classList.add('focused');
})

textarea.addEventListener('blur', function() {
    document.getElementById('questionEntreprise').classList.remove('focused');
});

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
    
                $("#responseArea").append('<p>'+response+'</p>')
        
            },
            error: function(xhr, errmsg, err) {
                console.log("erreur")
            }

            
        });
    });
});
