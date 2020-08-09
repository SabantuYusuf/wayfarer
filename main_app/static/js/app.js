console.log('I work')

// bulmaCarousel.attach('#carousel', {
//     slidesToScroll: 1,
//     slidesToShow: 1,
// });

// Shoutout to Traersy Media for help with this carousel!
// https://www.youtube.com/watch?v=7ZO2RTMNSAY

const sliderImages = document.querySelectorAll('.slide')
const arrowLeft = document.querySelector('#arrow-left')
const arrowRight = document.querySelector('#arrow-right')
let current = 0;

// Clears all images
function reset(){
    for(let i = 0; i < sliderImages.length; i++){
        sliderImages[i].style.display = 'none';
    }
}

// Start Slide 
function startSlide(){
    reset();
    sliderImages[0].style.display = 'block';
}

// Show Previous
function slideLeft(){
    reset();
    sliderImages[current - 1].style.display = 'block';
    current--;
}

// Show next
function slideRight(){
    reset();
    sliderImages[current + 1].style.display = 'block';
    current++;
}


// Event Left Arrow
arrowLeft.addEventListener('click', function(){
    if(current === 0){
        current = sliderImages.length;
    }
    slideLeft();
})

// Event Right Arrow
arrowRight.addEventListener('click', function(){
    if(current === sliderImages.length - 1){
        current = -1;
    }
    slideRight();
})


startSlide();




