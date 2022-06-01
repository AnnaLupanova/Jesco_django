const swiper = new Swiper('.swiper', {
  // Optional parameters
  direction: 'vertical',
  loop: true,

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
});

$(document).ready(function(){

  $(".fa-magnifying-glass").click(function(){
    $(".icon__wrapper, .input").toggleClass("active");
    $(".header__icon").toggleClass("header-active");
    if ($(".icon__wrapper, .input").hasClass("active")){
        $("input[type='text']").focus();
    }
  });
    $('.header__burger').click(function (event){
        $('.header__burger, .header__menu').toggleClass('active_bur');
        console.log('dfgdfg')
    });

});
