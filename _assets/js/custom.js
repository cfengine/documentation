'use strict';
$(document).ready(function() {
    /*show/hide moveTop link */
    var showMoveTop = false;
    $("#moveTop a").click(function(e) {
        $(window).scrollTop($('#nav_wrapper').offset().top);
        showMoveTop = false;
        $("#moveTop").hide();
        e.preventDefault();
    });

    $(window).scroll(function() {
        if ($(window).scrollTop() > 380 && showMoveTop===false) {
            $("#moveTop").show();
            showMoveTop = true;
        } else if($(window).scrollTop()<380 && showMoveTop === true ) {
            $("#moveTop").hide();
            showMoveTop = false;
        }
    });

    var ToC =
        "<nav role='navigation' class='table-of-contents'>" +
            "<h3>Table of contents:</h3>" +
                "<ul>";

    var newLine, el, title, link, elClass, url;
    $("article h2, article h3, article h4").each(function() {
        el      = $(this);
        title   = el.text();
        link    = "#" + el.attr("id");
        elClass = "link_" + el.prop("tagName")
        url     = window.location.pathname;


        newLine =
            "<li class='" + elClass  +  "'>" +
                "<a href='" + url + link + "'>" +
                    title +
                "</a>" +
            "</li>";

        ToC += newLine;
    });
    ToC +=
            "</ul>" +
        "</nav>";

    $("article #toc").append(ToC);
});