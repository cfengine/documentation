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
        "<nav role='navigation'>" +
             "<ul>";
    var ToC_End =
            "</ul>" +
        "</nav>";

    var newLine, el, title, link, elClass, url, ToC='';
    $(".article h2, .article h3, .article h4").each(function() {
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
    } else {
        $("#TOCbox_wrapper").hide();
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

document.querySelectorAll('pre').forEach(function (pre) {
    pre.closest('div.highlight').innerHTML += '<i data-closest=".highlight" data-copyfrom="code" class="bi bi-clipboard copy-to-clipboard"></i>';
});

document.querySelectorAll(".copy-to-clipboard").forEach(function (el) {
    el.addEventListener("click", function (event) {
        event.preventDefault();
        var target = event.target;
        var copyText = target.closest(event.target.dataset.closest).querySelector(event.target.dataset.copyfrom).innerText;
        navigator.clipboard.writeText(copyText);
        target.classList.remove('bi-clipboard');
        target.className += ' bi-check2 ';
        setTimeout(function ()  { target.className = 'bi bi-clipboard copy-to-clipboard' }, 2000);
    })
});
