gsap.registerPlugin(ScrollTrigger)

const navigation = document.querySelector("#navigation")
const titre = document.querySelector("#titreTop")
const sousTitre = document.querySelector("#sousTexte")
const decouvrirButton = document.querySelector("#decouvrirButton")
const demonstartionButton = document.querySelector("#demonstartionButton")
const topDecouverte = document.querySelector("#topDecouverte p")
const propulse = document.querySelector("#propulsion")
const titreAnalyse = document.querySelector("#titreAnalyse")
const titreOptimisation = document.querySelector("#titreOptimisation")
const macTalent = document.querySelector("#macTalent")
const macProject = document.querySelector("#macProject")
const lastText = document.querySelector("#bottomDecouverte h2")
const lastButton = document.querySelector("#finalButton")
const neon = document.querySelector("#rectangle")



const titres = gsap.utils.toArray('#titreTop p')
const tl = gsap.timeline({
    repeat: -1,
    repeatDelay: 0,
})



titres.forEach(titre => {

    const titresArea = Splitting({
        target : titre,
        by:"chars"
    });

    tl
        .from(titresArea[0].chars,{
            opacity:0,
            y: 80,
            rotateX: -90,
            stagger: .02,
        }, "<")

        .to(titresArea[0].chars,{
            opacity:0,
            y: -80,
            rotateX: 90,
            stagger: .02,
            delay : 2,
        }, "<1")

})



    // Titre
gsap.from(titre,{
    opacity:0,
    duration:1,
    y:-100
})

gsap.to(titre,{
    xPercent : 100,
    scrollTrigger : {
        trigger : titre,
        toggleActions : "play reverse play reverse",
        start : "top 10%",
        scrub: 1,
    }
})

// sous Titre
gsap.from(sousTitre,{
    opacity:0,
    duration:1,
    delay:1,
    y:100
})

gsap.to(sousTitre,{
    xPercent : -100,
    scrollTrigger : {
        trigger : sousTitre,
        toggleActions : "play reverse play reverse",
        start : "top 50%",
        scrub: 1,
    }
})

// Boutton
gsap.from(decouvrirButton,{
    opacity:0,
    duration:2,
    delay:2,
    x:-100
})


gsap.to(decouvrirButton,{
    xPercent : -500,
    scrollTrigger : {
        trigger : decouvrirButton,
        toggleActions : "play reverse play reverse",
        start : "top 40%",
        scrub: 1,
    }
})


gsap.from(demonstartionButton,{
    opacity:0,
    duration:2,
    delay:2,
    x:100
})

gsap.to(demonstartionButton,{
    xPercent : 500,
    scrollTrigger : {
        trigger : demonstartionButton,
        toggleActions : "play reverse play reverse",
        start : "top 40%",
        scrub: 1,
    }
})

// disucssion 100%

gsap.to(topDecouverte, {
    yPercent : 400,
    scrollTrigger : {
        trigger : topDecouverte,
        toggleActions : "play reverse play reverse",
        start : "top 50%",
        scrub: 2,
    }
})

// propulsion

gsap.from(propulse, {
    yPercent : -200,
    scrollTrigger : {
        trigger : propulse,
        toggleActions : "play reverse play reverse",
        scrub: 2,
    }
})

//titre Analyse

gsap.from(titreAnalyse, {
    xPercent : -50,
    opacity : 0,
    scrollTrigger : {
        trigger : titreAnalyse,
        toggleActions : "play reverse play reverse",
        start : "top 100%",
        scrub: 2,
    }
})


//titre Optimisation

gsap.from(titreOptimisation, {
    xPercent : 50,
    opacity : 0,
    scrollTrigger : {
        trigger : titreOptimisation,
        toggleActions : "play reverse play reverse",
        start : "top 100%",
        scrub: 2,
    }
})

let analyseArea = Splitting({
    target : document.querySelector("#analyse .microExplication"),
    by:"chars"
});

gsap.from(analyseArea[0].chars, {
    color : "white",
    y: 30,
    stagger : 0.05,
    scrollTrigger : {
        trigger : titreAnalyse,
        start : "start 50%",
        end : "bottom 10%",
        scrub : true,
    }
})

let optimisationArea = Splitting({
    target : document.querySelector("#optimisation .microExplication"),
    by:"chars"
});

gsap.from(optimisationArea[0].chars, {
    color : "white",
    y: 20,
    stagger : 0.1,
    scrollTrigger : {
        trigger : titreOptimisation,
        start : "start 50%",
        end : "bottom 10%",
        scrub : true,
    }
})


const lenis = new Lenis()

lenis.on('scroll', ScrollTrigger.update)

gsap.ticker.add((time)=>{
  lenis.raf(time * 1000)
})

gsap.ticker.lagSmoothing(0)

// Ordi Talent

gsap.from(macTalent, {
    xPercent : -200,
    scrollTrigger : {
        trigger : titreAnalyse,
        toggleActions : "play reverse play reverse",
        scrub: 2,
    }
})

// Ordi optimisation

gsap.from(macProject, {
    xPercent : 200,
    scrollTrigger : {
        trigger : titreOptimisation,
        toggleActions : "play reverse play reverse",
        scrub: 2,
    }
})

gsap.from(lastText, {
    xPercent : 100,
    scrollTrigger : {
        trigger : lastText,
        toggleActions : "play reverse play reverse",
        start: "top 100%",
        end:"bottom 60%",
        scrub: 2,
    }
})

gsap.from(lastButton, {
    xPercent : -100,
    scrollTrigger : {
        trigger : lastText,
        toggleActions : "play reverse play reverse",
        start: "top 100%",
        end:"bottom 60%",
        scrub: 2,
    }
})

gsap.from(neon, {
    xPercent : -100,
    duration : 2,
    scrollTrigger : {
        trigger : neon,
        toggleActions : "play none none reverse",
        start: "top 100%",
        end:"bottom 90%",
    }
})


window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navigation');
    var scrollPosition = window.scrollY;

    if (scrollPosition > 500) { // Par exemple, après 50 pixels de défilement
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});