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
});