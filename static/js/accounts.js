gsap.registerPlugin(ScrollTrigger)

// Gauche conn
gsap.from("#connexionBox",{
    opacity:0,
    duration:1,
    x:-200
})

// Droite conn
gsap.from("#illustrationConn",{
    opacity:0,
    duration:1,
    x:200
})

// Block QUI

gsap.from("#quiEstCe h1",{
    opacity:0,
    duration:2,
    y:-200
})

gsap.from("#entrepQUI",{
    opacity:0,
    duration:2,
    x:-200
})

gsap.from("#freeQUI",{
    opacity:0,
    duration:2,
    x:200
})

gsap.from("#dejaCompte",{
    opacity:0,
    duration:2,
    y:200
})

// INSCRIPTION ENTREPRISE
gsap.from("#InscriptionBox",{
    opacity:0,
    duration:1,
    x:-200
})

gsap.from("#illustrationEntreprise",{
    opacity:0,
    duration:1,
    x:200
})
