'use strict';
var is_mobile = true;
$(document).ready(function() {
    if ($(window).width() > 800)
    {
        is_mobile = false;
    }
    var scrollPos = 380;
    /*show/hide moveTop link */
    var showMoveTop = false;

    if (is_mobile === false)
    {
        $("#moveTop a").click(function(e) {
            $(window).scrollTop($('#nav_wrapper').offset().top);
            showMoveTop = false;
            $("#moveTop").hide();
            e.preventDefault();
        });

        $(window).scroll(function() {
            if ($(window).scrollTop() > scrollPos && showMoveTop===false) {
                $("#moveTop").show();
                showMoveTop = true;
            } else if($(window).scrollTop() < scrollPos && showMoveTop === true ) {
                $("#moveTop").hide();
                showMoveTop = false;
            }
        });
    }

    if ($(window).scrollTop() > scrollPos && is_mobile === false)
    {
        $("#moveTop").show();
        showMoveTop = true;
    }


    var ToC_start =
        "<div class='TOCheader'>Table of Contents</div>" +
        "<nav role='navigation'>" +
             "<ul>";
    var ToC_End =
            "</ul>" +
        "</nav>";

    var newLine, el, title, link, elClass, url, ToC='';
    $("article h1, article h2, article h3, article h4").each(function() {
        el      = $(this);
        title   = el.text();
        link    = "#" + el.attr("id");
        elClass = "link_" + el.prop("tagName").toLowerCase()
        url     = window.location.pathname;

        // if header has data-behavior= exclude-from-toc - do not include it to the TOC list
        if (el.children('center').attr('data-behavior') !=="exclude-from-toc")
        {
            newLine =
                "<li class='" + elClass  +  "'>" +
                    "<a href='" + url + link + "'>" +
                        title +
                    "</a>" +
                "</li>";
            ToC += newLine;
        }
    });
    
    if (ToC.length)
    {
        if  (is_mobile === false)
        {
            $("#TOCbox_wrapper").show();
        }
        var result = ToC_start + ToC + ToC_End;

        $("#TOCbox_wrapper #TOCbox_list").html('');
        $("#print_TOC").html('');

        $("#TOCbox_wrapper #TOCbox_list").append(result);
        $("#print_TOC").append(result);
    }

    // detect print event, display TOC
    var beforePrint = function() {
        $("#print_TOC_wrapper").show();
    };
    var afterPrint = function() {
        $("#print_TOC_wrapper").hide();
    };

    if (window.matchMedia) {
        var mediaQueryList = window.matchMedia('print');
        mediaQueryList.addListener(function(mql) {
            if (mql.matches) {
                beforePrint();
            } else {
                afterPrint();
            }
        });
    }

    window.onbeforeprint = beforePrint;
    window.onafterprint = afterPrint;

    if (is_mobile === true)
    {
     // mobile navigation
        $('#mobile_left_menu').sidr({
            name: 'leftMenyMobile',
            side: 'left',
            source: '#left_col'
        });
        $('#mobile_right_menu').sidr({
            name: 'TOCbox_list_mobile',
            side: 'right',
            source: '#TOCbox_list'
        });

        $('.sidr-inner a, .sidr-inner span').on('click', function(){
            if ($("#leftMenyMobile").is(":visible") === true)
            {
                closeSideMenues('leftMenyMobile');
            }

            if ($("#TOCbox_list_mobile").is(":visible") === true)
            {
                closeSideMenues('TOCbox_list_mobile');
            }
        });
    }





 var element = window;//document.getElementById('w');
 var openedMenues = [];

var closeRight = $('<div id="closeRight" style="z-index:99999"><a href="#closeRight"><--close right</a></div>');
var closeLeft = $('<div id="closeLeft" style="z-index:999"><a style="z-index:99999" href="#closeLeft">close left--></a></div>');

    Hammer(element).on("swipeleft", function() {
        if (openedMenues.indexOf('leftMenyMobile') === -1)
        {
            if (openedMenues.indexOf('TOCbox_list_mobile') !== -1 || $("#TOCbox_list_mobile").is(":visible") === true)
            {
                closeSideMenues('TOCbox_list_mobile');
            }
            else
            {
                openMenu('leftMenyMobile')
            }
        }
    });

    Hammer(element).on("swiperight", function() {
        if (openedMenues.indexOf('TOCbox_list_mobile') === -1)
        {
            if (openedMenues.indexOf('leftMenyMobile') !== -1 || $("#leftMenyMobile").is(":visible") === true)
            {
                closeSideMenues('leftMenyMobile');
            }
            else
            {
                openMenu('TOCbox_list_mobile');
            }
        }
    });


    function openMenu(menuName)
    {
        $.sidr('open', menuName);
        openedMenues.push(menuName);
        //TODO: refactor
        if (menuName === 'TOCbox_list_mobile')
        {
            if ($("#TOCbox_list_mobile #closeRight").length === 0)
            {
                $("#TOCbox_list_mobile").append(closeRight);
            }
        }

        if(menuName === 'leftMenyMobile')
        {
            if ($("#leftMenyMobile #closeLeft").length === 0)
            {
                $("#leftMenyMobile").append(closeLeft);
            }
        }
    }

    function closeSideMenues(menuItem)
    {
        var pos = openedMenues.indexOf(menuItem);
        if (pos !== -1)
        {
            openedMenues.splice(pos, 1);
        }
        $.sidr('close', menuItem);
    }


    $(".sidr").on("click", "#closeRight a, #closeLeft a", function(event){
        $.sidr('close', 'leftMenyMobile');
        $.sidr('close', "TOCbox_list_mobile");
        openedMenues=[];
    });
});