'use strict';
$(document).ready(function() {
    var scrollPos = 380;
    /*show/hide moveTop link */
    var showMoveTop = false;
    $("#moveTop a").click(function(e) {
        $(window).scrollTop($('#nav_wrapper').offset().top);
        showMoveTop = false;
        $("#moveTop").hide();
        e.preventDefault();
    });

    $(window).scroll(function() {
        if ($(window).scrollTop() > scrollPos && showMoveTop===false) {
            $("#moveTop").show();
            $("#TOCbox_wrapper").addClass('TOCbox_Fixed');
            showMoveTop = true;
        } else if($(window).scrollTop() < scrollPos && showMoveTop === true ) {
            $("#moveTop").hide();
            $("#TOCbox_wrapper").removeClass('TOCbox_Fixed');
            showMoveTop = false;
        }
    });

    if ($(window).scrollTop() > scrollPos)
    {
        $("#moveTop").show();
        $("#TOCbox_wrapper").addClass('TOCbox_Fixed');
        showMoveTop = true;
    }


var ToC_start =
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
        $("#TOCbox_wrapper").show();
        $("#TOCbox_wrapper #TOCbox_list").append(ToC_start + ToC + ToC_End);
    }
});