let cards = document.querySelectorAll('.dataGallery .card');
let next = document.getElementById('next');
let prev = document.getElementById('prev');
let webLabel = document.getElementById('webLabel');
let dataLabel = document.getElementById('dataLabel');
let projets = {
    0:"data-collecte",
    1:"data-creationOutils",
    2:"data-dahsboard",
    3:"data-automatisation",
    4:"data-integration",
    5:"data-bigData",
    6:"data-qualite",
    7:"web-ecommerce",
    8:"web-marketingDigital",
    9:"web-design",
    10:"web-analyse",
    11:"autre",
}

let active = 0;

function loadShow(){
    let stt = 0;
    cards[active].style.transform = `none`;
    cards[active].style.zIndex = 1;
    cards[active].style.filter = 'none'
    cards[active].style.opacity = 1

    // Partie de droite et centre du carousel
    for(var i = active + 1; i<cards.length; i++){
        stt++;
        cards[i].style.transform = `translateX(${150*stt}px) scale(${1-0.2*stt}) perspective(50px) rotateY(-1deg)`;
        cards[i].style.zIndex = -stt
        cards[i].style.filter = 'blur(5px)';
        cards[i].style.opacity = stt > 2 ? 0 : 0.6;
    }

    // Partie gauche
    stt = 0;
    for(var i=active-1; i>=0; i--){
        stt++;
        cards[i].style.transform = `translateX(${-150*stt}px) scale(${1-0.2*stt}) perspective(30px) rotateY(1deg)`;
        cards[i].style.zIndex = -stt
        cards[i].style.filter = 'blur(5px)';
        cards[i].style.opacity = stt > 2 ? 0 : 0.6;
    }

    function setActive(label) {
        label.style.color = 'black';
    }
    
    function setInactive(label) {
        label.style.color = 'lightgrey';
    }    

    //Data et web parse
    if(active > 6 && active <=10){
        setActive(webLabel);
        setInactive(dataLabel);
    }else if(active <= 6){
        setActive(dataLabel);
        setInactive(webLabel);
    }else{
        setInactive(dataLabel);
        setInactive(webLabel);
    }

}

loadShow();


next.onclick = function(){
    active = active +1 < cards.length ? active + 1 : active;
    loadShow();
}
prev.onclick = function(){
    active = active - 1 >= 0 ? active - 1 : active;
    loadShow();
}

webLabel.onclick = function(){
    active = 7
    loadShow();
}

dataLabel.onclick = function(){
    active = 0
    loadShow();
}
