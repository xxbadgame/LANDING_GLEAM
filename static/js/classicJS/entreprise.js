const textarea = document.querySelector("#questionEntreprise textarea");
const svgSiri = document.querySelector(".svgSiri");
const ombreSiri = document.querySelector(".ombreSiri");
const cercleOmbreSiri = document.querySelector(".cercleOmbreSiri");


textarea.addEventListener("input", e => {
    e.target.style.height = '6vh'; // Réinitialiser la hauteur
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