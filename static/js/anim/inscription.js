gsap.from("#FreelanceForm",{
    opacity:0,
    duration:1,
    x:-200
})

gsap.from("#FreelanceIllustration",{
    opacity:0,
    duration:1,
    x:200
})

gsap.to("#sousTitreFree",{
    yPercent : 200,
    opacity :0,
    scrollTrigger : {
        trigger : "#FreelanceForm",
        toggleActions : "play reverse play reverse",
        start : "top 10%",
        scrub: 1,
    }
})

gsap.from("#slogantFree",{
    yPercent : -700,
    scrollTrigger : {
        trigger : "#FreelanceIllustration img",
        toggleActions : "play reverse play reverse",
        start : "top 50%",
        end : "bottom 50%",
        scrub: 1,
    }
})

gsap.from("#endLogoFree",{
    yPercent : 400,
    opacity : 0,
    scrollTrigger : {
        trigger : "#FreelanceForm",
        toggleActions : "play reverse play reverse",
        start : "top 75%",
        end : "bottom 90%",
        scrub: 1,
    }
})