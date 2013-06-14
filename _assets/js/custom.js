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

var ToC_start =
        "<nav role='navigation'>" +
             "<ul>";
    var ToC_End =
            "</ul>" +
        "</nav>";

    var newLine, el, title, link, elClass, url, ToC='';
    $("article h2, article h3, article h4").each(function() {
        el      = $(this);
        title   = el.text();
        link    = "#" + el.attr("id");
        elClass = "link_" + el.prop("tagName").toLowerCase()
        url     = window.location.pathname;


        newLine =
            "<li class='" + elClass  +  "'>" +
                "<a href='" + url + link + "'>" +
                    title +
                "</a>" +
            "</li>";
        ToC += newLine;
    });
    if (ToC.length)
    {
        $("#jumpto_wrapper").show();
        $("#jumpto_wrapper #jumpto_list").append(ToC_start + ToC + ToC_End);
    }
});