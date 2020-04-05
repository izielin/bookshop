let owl = $('.carousel');
owl.owlCarousel({
    loop: true,
    margin: 15,
    autoplay: true,
    autoplayTimeout: 7500,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 3
        },
        960: {
            items: 4
        },
        1200: {
            items: 5
        }
    }
});
