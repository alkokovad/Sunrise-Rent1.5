new Swiper('.photo_swiper', {
  navigation: {
    nextEl: '.next_btn',
    prevEl: '.prev_btn',
  },
  simulateTouch: true,
  touchRatio: 1,
  touchAngle: 45,
  grabCursor: true,
  slidesPerView: 'auto',
  watchOverflow: true,
  loop: true,
  loopedSlides: 4,
  freeMode: true,
  spaceBetween: 0,
  freeModeMomentum: false,
});

new Swiper('.beach_photo_slider', {
  simulateTouch: true,
  touchRatio: 1,
  touchAngle: 45,
  grabCursor: true,
  slidesPerView: 'auto',
  spaceBetween: 24,
  pagination: {
    el: '.beach-pagination',
    clikable: true,
  },
});

new Swiper('.beaches_carousel', {
  slidesPerView: 3.5,
  slidesPerGroup: 3.5,
  spaceBetween: 20,
  navigation: {
    nextEl: '.next_btn_beaches',
    prevEl: '.prev_btn_beaches',
  },
});