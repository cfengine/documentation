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
        "<div class='TOCheader'><i class='fa fa-chevron-down'></i>Table of Contents</div>" +
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


});

$(document).ready(function() {
    $("#TOCbox_wrapper").click(function() { 
        $("#TOCbox_list").toggle();
    });

    $(document).click(function(event) { 
        if(!$(event.target).closest('#TOCbox_wrapper').length) {
            if($('#TOCbox_list').is(":visible")) {
                $('#TOCbox_list').hide();
            }
        }
    });
    
    $(".article :header").each(function(){
        var url = window.location.href;
        url = url.replace(window.location.hash,'');
        $(this).prepend('<a class="anchor" href="' + url + '#' + $(this).attr("id") + '"><i class="fa fa-link"></i></a>');
    });
    
});

