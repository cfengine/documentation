'use strict';
import '../styles/cfengine.less';

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
    var closest = pre.closest('div.highlight');
    if (closest) {
        closest.innerHTML += '<i data-closest=".highlight" data-copyfrom="code" class="bi bi-clipboard copy-to-clipboard"></i>';
    }
});

document.querySelectorAll(".copy-to-clipboard").forEach(function (el) {
    el.addEventListener("click", function (event) {
        event.preventDefault();
        var target = event.target;
        var copyText = target
            .closest(event.target.dataset.closest)
            .querySelector(event.target.dataset.copyfrom)
            .innerText
            .replace(/\n+$/, ""); // remove trailing newlines from the copied text
        navigator.clipboard.writeText(copyText);
        target.classList.remove('bi-clipboard');
        target.className += ' bi-check2 ';
        setTimeout(function ()  { target.className = 'bi bi-clipboard copy-to-clipboard' }, 2000);
    })
});

var tableOfContents = document.querySelector('.table-of-contents .TOC');
if (tableOfContents) {
    window.onclick = function (e) {
        if (!e.target.closest('.TOC') && !tableOfContents.querySelector('.closed')) {
            tableOfContents.classList.add('closed');
        }
    };
    tableOfContents.onclick = function () {
        tableOfContents.classList.toggle('closed');
    };
}


var menu = document.querySelector('.top_menu ul');
var overlay = document.querySelector('#overlay');
var openedClass = "opened";

window.openMenuHandler = function (collapseMenu) {
    if (collapseMenu.className.indexOf(openedClass) == -1) {
        collapseMenu.classList.add(openedClass);
        menu.classList.add('d-b');
        overlay.style.display = "block";
    } else {
        collapseMenu.classList.remove(openedClass);
        menu.classList.remove('d-b');
        overlay.style.display = "none";
    }
}

window.openNavigationHandler = function () {
    document.querySelector('.left-menu').classList.add(openedClass);
    overlay.style.display = "block";
}

document.querySelector('.left-menu .menu-close').onclick = function () {
    document.querySelector('.left-menu').classList.remove(openedClass);
    overlay.style.display = "none";
}

overlay.onclick = function () {
    document.querySelector('.collapse').classList.remove(openedClass);
    document.querySelector('.left-menu').classList.remove(openedClass);
    menu.classList.remove('d-b');
    overlay.style.display = "none";
}

var topMenuVersions = document.querySelector('.top_menu-versions');
topMenuVersions.onclick = function (event) {
    topMenuVersions.classList.toggle('opened');
}

document.querySelector('.top_menu-versions-title > span > span').innerText = document.querySelector('.top_menu-versions-list a[selected="selected"], .top_menu-versions-list a').innerText;

var mainMenuCopy = document.querySelector('.left-menu ul.mainMenu').cloneNode(true);
var clickedMenuHistory = [{href: './', name: 'Home'}];

var urlPaths = document.location.pathname.split('/');
var url = urlPaths[urlPaths.length - 1]; // get last url part
var currentMenuItem = document.querySelector('.left-menu li[data-url="'+ url +'"]');

var renderNestedMenu = function (href) {
    if (href == null) {
        document.querySelector('.left-menu ul.mainMenu').replaceWith(mainMenuCopy);
    } else {
        var ul = mainMenuCopy.querySelector('li[data-url="'+ href +'"]').querySelector('ul').cloneNode(true);
        ul.classList.add('mainMenu');
        document.querySelector('.left-menu ul.mainMenu').replaceWith(ul);
        var selected = document.querySelector('li[data-url="'+ url +'"]');
        if (selected){
            selected.className += ' opened current';
        }
    }

    applyOnclickToMenuItems();
}
var menuItemClickFn = function (e) {
    if (window.innerWidth < 1024) { // if the window width is less than 1024 then treat the menu as mobile one
        if (e.target.closest('li').classList.contains('parent')) {
            e.preventDefault();
            renderNestedMenu(e.target.getAttribute('href'));
            clickedMenuHistory.push({href: e.target.getAttribute('href'), name: e.target.innerText});
            buildBreadcrumbs(clickedMenuHistory);
        }
    }
};

var applyOnclickToMenuItems = function () {
    document
        .querySelector('.left-menu')
        .querySelectorAll('ul li.parent > a')
        .forEach(function (item) {
            item.onclick = menuItemClickFn
        });
}
applyOnclickToMenuItems();

var selectedMenu = document.querySelector('.selectedMenu');
var leftMenuBreadcrumbs = document.querySelector('.left-menu-breadcrumbs');
var buildBreadcrumbs = function (items) {
    var html = '';
    if (items.length > 3) {
        items = items.slice(-3);
        html = '<li>...</li><li>/</li>';
    }
    items.forEach(function (item, index) {
        if (index > 0) {
            html += '<li>/</li>';
        }
        html += '<li><a href="'+ item.href +'"><span>'+ item.name +'</span></a></li>'
    })
    leftMenuBreadcrumbs.innerHTML = html;
    var lastItem = items[items.length - 1];
    if (window.innerWidth < 1024){
        selectedMenu.innerHTML = lastItem.name !== 'Home' ?
            '<a href="'+ lastItem.href +'">'+ lastItem.name +' <i class="bi bi-box-arrow-up-right"></i></a>' :
            '';
    }
}

document.querySelector('.menu-back').onclick = function () {
    if (clickedMenuHistory.length != 1) {
        clickedMenuHistory.pop();
        var lastHistoryElement = clickedMenuHistory[clickedMenuHistory.length - 1];
        renderNestedMenu(lastHistoryElement['name'] !== 'Home' ? lastHistoryElement['href'] : null);
        buildBreadcrumbs(clickedMenuHistory);
    }
}



if (currentMenuItem != null) {
    currentMenuItem.className += ' opened current';
    var menuHistory = [];
    var currentLink = currentMenuItem.querySelector('a');
    // if selected menu item is a parent we show children on mobile menu
    if (currentLink && currentMenuItem.classList.contains('parent')){
        menuHistory.unshift({href: currentLink.getAttribute('href'), name: currentLink.innerText});
    }
    var closest = currentMenuItem.closest('ul').closest('li');

    while (true) {
        if (!closest) break;
        if (window.innerWidth > 1023) { // if the window width more than 1023 then treat the menu as desktop one
            closest.classList.add('opened');
        } else {
            // Restore history from html
            var link = closest.querySelector('a');
            if (link){
                menuHistory.unshift({href: link.getAttribute('href'), name: link.innerText});
            }
        }
        closest = closest.closest('ul').closest('li');
    }
    clickedMenuHistory = clickedMenuHistory.concat(menuHistory);
}
buildBreadcrumbs(clickedMenuHistory);

if (window.innerWidth > 1023) {
    document.querySelectorAll('.mainMenu li.parent > i').forEach(function (element) {
        element.onclick = function (event) {
            event.stopImmediatePropagation();
            element.closest('li.parent').classList.toggle('opened');
        }
    });
} else {
    // Small screen
    var lastHistoryElement = clickedMenuHistory[clickedMenuHistory.length - 1];
    renderNestedMenu(lastHistoryElement.href);
}

function fillVersionWrapperSelect(url) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', url, true);
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState != 4 || xmlhttp.status != 200) {
            return
        }
        var str = ''; //generated HTML
        var data = JSON.parse(xmlhttp.responseText);
        for (var i = 0; i < data.docs.length; i++) {
            var branch = data.docs[i];
            var selected = '';
            if (location.pathname.indexOf(branch.Link) == 0) {
                // this is version that we're currently looking at
                selected = ' selected';
                window.currentVersionLink = branch.Link;
            }
            str += '<option value="' + branch.Link + '"' + selected + '>' + branch.Title + '</option>';
        }
        var top_version_wrapper = document.querySelector('#top_version_wrapper select');

        if (top_version_wrapper) {
            top_version_wrapper.innerHTML = str;
        }
    }
    xmlhttp.send(null);
};

function selectVersion(value) {
    if (value.indexOf('archive') == -1 && window.currentVersionLink) {
        window.location = window.location.href.replace(window.currentVersionLink, value);
    } else {
        window.location = value;
    }
};
window.selectVersion = selectVersion;

document.addEventListener("DOMContentLoaded", function () {
    fillVersionWrapperSelect('/docs/branches.json')

    const anchors = document.querySelectorAll(
        ".article h1[id], .article h2[id], .article h3[id], .article h4[id], .article h5[id], .article h6[id]"
    );

    anchors.forEach(function(el){
        const url = new URL(window.location.href);
        el.insertAdjacentHTML('beforeend', '<a class="anchor" href="' + url.origin + url.pathname + '#' + el.id + '"><i class="bi bi-link-45deg"></i></a>');
    });

    document.querySelectorAll('a.anchor').forEach(function (a) {
        a.onclick = function (e) {
            e.preventDefault();
            navigator.clipboard.writeText(a.href);
            a.classList.add('url-copied');
            history.replaceState(null, null, a.href);
            setTimeout(function ()  { a.classList.remove('url-copied') }, 2000);
        }
    });

    /**
     * Highlight the current TOC item when a user scrolls to the corresponding page section.
     */
    (() => {
        const tocLinks = document.querySelectorAll('#TOCbox_list li a');

        if (!tocLinks || !anchors) {
            return;
        }

        // offsetTop returns offset to the offsetParent, which is main wrapper, we need to add 130px to get actual offset
        const fetchOffsets = anchors => [...anchors].map(a => a.offsetTop + 130);
        let anchorsOffsets = fetchOffsets(anchors);

        let timeout = undefined;
        const updateActiveTocItem = () => {
            if (timeout) {
                clearTimeout(timeout)
            }

            // The current TOC menu item will be calculated in 100 ms after the user stops scrolling.
            // Otherwise, there might be redundant calculations.
            timeout = setTimeout( () => {
                let scrollTop = window.scrollY;
                tocLinks.forEach(link =>  link.classList.remove('current'));

                for (let i = anchorsOffsets.length - 1; i >= 0; i--) {
                    if (scrollTop > anchorsOffsets[i]) {
                        setActiveLink(anchors[i].id, i);
                        break;
                    }
                }
            }, 50); // 0.05s threshold

        }

        const setActiveLink = (id, n) => {
            const activeLink = document.querySelector(`#TOCbox_list li a[href$="#${id}"]`);
            if (activeLink) {
                activeLink.classList.add('current');
            }
            const tocWrapper = document.getElementById('TOCbox_wrapper');
            const TOC_TOP_OFFSET = 42;
            const LI_HEIGHT = 30;
            const selectedOffset = window.innerHeight-TOC_TOP_OFFSET - (LI_HEIGHT * (n + 1))
            tocWrapper.style.top = (selectedOffset < 0 ? 12 + selectedOffset : 12) + 'px';
        }

        window.addEventListener('scroll', updateActiveTocItem);
        window.addEventListener("resize", () => {
            // anchors position change when the window is resized
            anchorsOffsets = fetchOffsets(anchors);
        });
    })();

    /**
     * Display scroll to top button when the scroll reaches 350px
     * from the top and window width less than 1280px
     */
    (() => {
        const scrollToTopBtn = document.getElementById('scrollToTopBtn');
        const showClass = 'show';

        if (!scrollToTopBtn) {
            return;
        }

        const handleScrollToTopVisibility = () => {
            if (window.scrollY > 350 && window.innerWidth <= 1280) {
                scrollToTopBtn.classList.add(showClass);
            } else {
                scrollToTopBtn.classList.remove(showClass);
            }
        }

        window.addEventListener('scroll', handleScrollToTopVisibility);
    })();
});
