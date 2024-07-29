const textarea = document.querySelector("#questionEntreprise textarea");
const svgSiri = document.querySelector(".svgSiri");
const ombreSiri = document.querySelector(".ombreSiri");
const cercleOmbreSiri = document.querySelector(".cercleOmbreSiri");
var typed

document.addEventListener('DOMContentLoaded', function() {
    typed = new Typed('#WelcomeText', {
      strings: ['Bonjour '+ userFirstName +' !',' Je m\'appelle <span style="color:#FE981E;">Curiosity</span>.', 'Parlons de votre <span style="color:#E60CFE;">Business</span> !'],
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
    svgSiri.setAttribute('transform', 'scale(1.1)');
    cercleOmbreSiri.classList.add('ombreSiri');

    // Réinitialiser la mise à l'échelle après une courte période pour permettre le redémarrage
    setTimeout(() => {
        svgSiri.setAttribute('transform', 'scale(1)');
        cercleOmbreSiri.classList.remove('ombreSiri');
    }, 600); // Durée de l'animation
});


$(document).ready(function() {

    $('#suggestions button').on('click', function() {
            
        var buttonText = $(this).text();
        var currentInput = $('#chatInput').val();
        $('#chatInput').val(currentInput + ' ' + buttonText);
    });

    $('#questionEntreprise').on('submit', function(event) {
        event.preventDefault();

        document.querySelector('#cercleCheck').classList.add('submited1')
        document.querySelector('#suggestions').classList.add('noSuggestions')

        var message = $('#chatInput').val();
        $('#chatInput').val('');

        $.ajax(
            
          {
            url: roversPersonalityUrl,
            type: "POST",
            data: {
                message: message,
                thread_id: threadId,
                csrfmiddlewaretoken: csrfToken
            },
            
            success: function(response) {

                var jsonData = JSON.parse(response);

                // Nombre de questions
                var nbQuestionText = jsonData.nbQuestion;
                console.log(nbQuestionText)
                const ArrayQuestionTotal = nbQuestionText.split('/').map(element => element.trim());
                var pourcentageQuestion = (ArrayQuestionTotal[0]/ArrayQuestionTotal[1])*100;
                $('#pourcentageComp').text(Math.ceil(pourcentageQuestion))


                if(jsonData.status === "finProcessCuriosity"){

                    typed.destroy();

                    typed = new Typed('#WelcomeText', {
                        strings: ["Merci de la part de curiosity"],
                        typeSpeed: 25,
                        loop: false
                    });
                    
                    document.querySelector('#bigBottom').classList.add('fin')
                    document.querySelector('#finButtonCuriosity').classList.add('fin')
                    document.querySelector('#cercleCheck .checkIcon').classList.add('fin')
                    document.querySelector('#cercleCheck').classList.add('fin')         

                }else if(jsonData.status === "finProcessAll"){

                    typed.destroy();

                    typed = new Typed('#WelcomeText', {
                        strings: ["Découvrir votre économie avec GLEAM ?"],
                        typeSpeed: 25,
                        loop: false
                    });

                    document.querySelector('#bigBottom').classList.add('fin')
                    document.querySelector('#finButtonAll').classList.add('fin')
                    document.querySelector('#cercleCheck .checkIcon').classList.add('fin')
                    document.querySelector('#cercleCheck').classList.add('fin') 

                }else if(jsonData.status === "enCours"){

                    
                    // Place aux questions
                    typed.destroy();
                    document.querySelector('#WelcomeTextArea p').classList.add('questionned')
                
                    var question = jsonData.questions;
                    typed = new Typed('#WelcomeText', {
                        strings: [question],
                        typeSpeed: 25,
                        loop: false
                    });


                    // Animation de changement questions
                    document.querySelector('#cercleCheck').classList.add('submited2')
                    document.querySelector('#cercleCheck .checkIcon').classList.add('submited')
                    
                    setTimeout(()=>{
                        document.querySelector('#cercleCheck').classList.remove('submited1'),
                        document.querySelector('#cercleCheck').classList.remove('submited2'),
                        document.querySelector('#cercleCheck .checkIcon').classList.remove('submited')
                        document.querySelector('#suggestions').classList.remove('noSuggestions')
                    },3000)

                    // Ajouter des suggestions
                    
                    var suggestions = jsonData.suggestionsBot;
                    const suggestionsButtons = document.getElementById('suggestions');
                    const buttons = suggestionsButtons.getElementsByTagName('button')
                    
                    for (var i=0; i < suggestions.length; i++){
                        $(buttons[i]).text(suggestions[i])
                    }

                }else{
                    console.log("erreur status")
                }
            },
            error: function(xhr, errmsg, err) {
                console.log("erreur")
            }

            
        });
    });
});
