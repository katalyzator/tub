
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

// �������� ����� ������� � ���������� ����������
$('.tabs-nav > li > a').on('click', function (event) {
    event.preventDefault();
    $('.tabs-nav > li a').removeClass('tab-active');
    $(this).addClass('tab-active');
    $('.tabs-stage > div').hide();
    $($(this).attr('href')).show();
});

$('a[href^="#"]').on('click', function(event) {
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





