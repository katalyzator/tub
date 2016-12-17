$('ul.language > li:first-child > a').addClass('l_active');

// »зменить класс вкладки и отобразить содержимое
$('ul.language > li > a').on('click', function (event) {
    event.preventDefault();
    $('ul.language > li a').removeClass('l_active');
    $(this).addClass('l_active');
});


$('.slider').slick({
    cssEase: 'ease-in',
    dots: true,
    autoplay: true,
    autoplaySpeed: 3000,
    arrows: false
});

$('.tabs-stage > div').hide();
$('.tabs-stage > div:nth-child(1)').show();
$('.tabs-nav  li:first-child a').addClass('tab-active');

// »зменить класс вкладки и отобразить содержимое
$('.tabs-nav > li > a').on('click', function (event) {
    event.preventDefault();
    $('.tabs-nav > li a').removeClass('tab-active');
    $(this).addClass('tab-active');
    $('.tabs-stage > div').hide("slower");
    $($(this).attr('href')).show('slower');
});

$('ul.menu > li > a[href^="#"]').on('click', function(event) {
    var target = $(this.getAttribute('href'));
    if( target.length ) {
        event.preventDefault();
        $('html, body').stop().animate({
            scrollTop: target.offset().top
        }, 1000);
    }
});


$(window).scroll(function () {
    if ($(window).scrollTop() >= 173) {
        $('.fixed-header').addClass('fix_head');
    }
    else {
        $('.fixed-header').removeClass('fix_head');
    }
});


new WOW().init();


$('.council > div').hide();
$('.council > div:nth-child(1)').show();
$('.student_council  li:first-child a').addClass('tab-active');

// »зменить класс вкладки и отобразить содержимое
$('.student_council > li > a').on('click', function (event) {
    event.preventDefault();
    $('.student_council > li a').removeClass('tab-active');
    $(this).addClass('tab-active');
    $('.council > div').hide("slower");
    $($(this).attr('href')).show('slower');
});





