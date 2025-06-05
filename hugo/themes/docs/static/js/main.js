'use strict';
const currentUrl = document.location.pathname;

const currentMenuUrl = (function () {
    const menuItemsElements = document.querySelectorAll('li[data-url]');
    const menuUrls = [...menuItemsElements].map(i => i.dataset.url).sort((a, b) => b.length - a.length);
    return menuUrls.find(url => currentUrl.endsWith(url.replace(/^(\.\/|\.\.\/)+/, '')));
})();

document.querySelectorAll('pre').forEach(function (pre) {
    const closest = pre.closest('div.highlight');
    if (closest) {
        closest.innerHTML += '<i data-closest=".highlight" data-copyfrom="code" class="bi bi-clipboard copy-to-clipboard"></i>';
    }
});

document.querySelectorAll(".copy-to-clipboard").forEach(function (el) {
    el.addEventListener("click", function (event) {
        event.preventDefault();
        const target = event.target;
        const copyText = target
            .closest(event.target.dataset.closest)
            .querySelector(event.target.dataset.copyfrom)
            .innerText
            .replace(/\n+$/, ""); // remove trailing newlines from the copied text
        navigator.clipboard.writeText(copyText);
        target.classList.remove('bi-clipboard');
        target.className += ' bi-check2 ';
        setTimeout(function () { target.className = 'bi bi-clipboard copy-to-clipboard' }, 2000);
    })
});

(function tocToggleHandler() {
    const tableOfContents = document.querySelector('.table-of-contents .TOC');
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
})();

const menu = document.querySelector('.top_menu ul');
const overlay = document.querySelector('#overlay');
const openedClass = "opened";

const openNavigationHandler = function () {
    document.querySelector('.left-menu').classList.add(openedClass);
    overlay.style.display = "block";
}

const openMenuHandler = function (collapseMenu) {
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

const topMenuVersions = document.querySelector('.top_menu-versions');
topMenuVersions.onclick = function (event) {
    topMenuVersions.classList.toggle('opened');
}

document.querySelector('.top_menu-versions-title > span > span').innerText = document.querySelector('.top_menu-versions-list a[selected="selected"], .top_menu-versions-list a').innerText;

const mainMenuCopy = document.querySelector('.left-menu ul.mainMenu').cloneNode(true);
const clickedMenuHistory = [{ href: '/', name: 'Home' }];
const renderNestedMenu = function (href) {

    if (href == null) {
        document.querySelector('.left-menu ul.mainMenu').replaceWith(mainMenuCopy);
    } else {
        const selectedLi = mainMenuCopy.querySelector('li[data-url="' + href + '"]');
        let ul = selectedLi.querySelector('ul') ?
            selectedLi.querySelector('ul').cloneNode(true) :
            selectedLi.closest('ul').cloneNode(true);

        ul.classList.add('mainMenu');
        document.querySelector('.left-menu ul.mainMenu').replaceWith(ul);
        const selected = document.querySelector('li[data-url="' + document.location.pathname + '"]');
        if (selected) {
            selected.className += ' opened current';
        }
    }

    applyOnclickToMenuItems();
}
const menuItemClickFn = function (e) {
    if (window.innerWidth < 1024) { // if the window width is less than 1024 then treat the menu as mobile one
        if (e.target.closest('li').classList.contains('parent')) {
            e.preventDefault();
            renderNestedMenu(e.target.getAttribute('href'));
            clickedMenuHistory.push({ href: e.target.getAttribute('href'), name: e.target.innerText });
            buildBreadcrumbs(clickedMenuHistory);
        }
    }
};

const applyOnclickToMenuItems = function () {
    document
        .querySelector('.left-menu')
        .querySelectorAll('ul li.parent > a')
        .forEach(function (item) {
            item.onclick = menuItemClickFn
        });
}
applyOnclickToMenuItems();

const selectedMenu = document.querySelector('.selectedMenu');
const leftMenuBreadcrumbs = document.querySelector('.left-menu-breadcrumbs');
const buildBreadcrumbs = function (items) {
    let html = '';
    if (items.length > 3) {
        items = items.slice(-3);
        html = '<li>...</li><li>/</li>';
    }
    items.forEach(function (item, index) {
        if (index > 0) {
            html += '<li>/</li>';
        }
        html += `<li title="${item.name}"><a href="${item.href}"><span>${item.name}</span></a></li>`;
    })
    leftMenuBreadcrumbs.innerHTML = html;
    let lastItem = items[items.length - 1];
    selectedMenu.innerHTML = lastItem.name !== 'Home' ?
        '<a href="' + lastItem.href + '">' + lastItem.name + ' <i class="bi bi-box-arrow-up-right"></i></a>' :
        '';
}


document.querySelector('.menu-back').onclick = function () {
    if (clickedMenuHistory.length != 1) {
        clickedMenuHistory.pop();
        let lastHistoryElement = clickedMenuHistory[clickedMenuHistory.length - 1];
        renderNestedMenu(lastHistoryElement['name'] !== 'Home' ? lastHistoryElement['href'] : null);
        buildBreadcrumbs(clickedMenuHistory);
    }
}

const processCurrentMenuItem = function () {
    const currentMenuItem = document.querySelector('.left-menu li[data-url="' + currentMenuUrl + '"]');

    if (currentMenuItem != null) {
        currentMenuItem.className += ' opened current';

        if (window.innerWidth > 1023) { // if the window width more than 1023 then treat the menu as desktop one
            let closest = currentMenuItem.closest('ul').closest('li');
            while (true) {
                if (!closest) break;
                closest.classList.add('opened');
                closest = closest.closest('ul').closest('li');
            }
        }
    }
}
processCurrentMenuItem();

if (window.innerWidth > 1023) {
    document.querySelectorAll('.mainMenu li.parent > i').forEach(function (element) {
        element.onclick = function (event) {
            event.stopImmediatePropagation();
            const parent = element.closest('li.parent');
            parent.classList.toggle('opened');
            const openedSubmenus = parent.querySelectorAll('.' + openedClass);
            openedSubmenus.forEach((subMenu) => {
                subMenu.classList.remove(openedClass);
            })
        }
    });
} else {
    const urlParts = (function(path) {
        const parts = path.split('/');
        parts.pop()
        let up = [];
        // collect ./ and ../ parts into the first item
        while (parts.length && (parts[0] === '.' || parts[0] === '..' || parts[0] === '')) {
            const part = parts.shift(); // get part and remove from paths
            if (part === '.' || part === '') continue;
            up.push('..');
        }

        const upPath = up.length ? up.join('/') : '.';
        return [upPath, ...parts];
    })(currentMenuUrl);
   
    let historyUrl = urlParts.shift() + '/';
    const selectedLi = document.querySelector('.left-menu ul.mainMenu li[data-url="' + currentMenuUrl + '"]');
    if (selectedLi) {
        if (!selectedLi.classList.contains('parent')) {
            urlParts.pop()
        }

        urlParts.forEach((item) => {
            if (item == '') return;
            historyUrl += item + '/';
 
            clickedMenuHistory.push({
                href: historyUrl,
                name: mainMenuCopy.querySelector('li[data-url="' + historyUrl + '"] > a').text
            });
        })
        renderNestedMenu(currentMenuUrl);
    }
}

document.addEventListener("DOMContentLoaded", function () {

    const anchors = document.querySelectorAll(".article h1, .article h2, .article h3, .article h4");
    anchors.forEach(function (el) {
        let url = new URL(window.location.href);
        el.insertAdjacentHTML('beforeend', '<a class="anchor" href="' + url.origin + url.pathname + '#' + el.id + '"><i class="bi bi-link-45deg"></i></a>');
    });

    document.querySelectorAll('a.anchor').forEach(function (a) {
        a.onclick = function (e) {
            e.preventDefault();
            navigator.clipboard.writeText(a.href);
            a.classList.add('url-copied');
            history.replaceState(null, null, a.href);
            setTimeout(function () {
                a.classList.remove('url-copied')
            }, 2000);
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
        const fetchOffsets = anchors => [...anchors].map(a => a.offsetTop + 70);
        let anchorsOffsets;

        let timeout = undefined;
        const updateActiveTocItem = () => {
            if (timeout) {
                clearTimeout(timeout)
            }
            anchorsOffsets = fetchOffsets(anchors);
            // The current TOC menu item will be calculated in 100 ms after the user stops scrolling.
            // Otherwise, there might be redundant calculations.
            timeout = setTimeout(() => {
                let scrollTop = window.scrollY;
                tocLinks.forEach(link => link.classList.remove('current'));

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
            let i = 0;
            const offsetArr = [...tocLinks].map((el,) => {
                const li = el.parentElement;
                i += li.clientHeight + parseInt(window.getComputedStyle(li).getPropertyValue('margin-bottom'));
                return i;
            })
            const selectedOffset = window.innerHeight - TOC_TOP_OFFSET - (Math.min(offsetArr.length - 1, n + 1))
            tocWrapper.style.top = (selectedOffset < 0 ? 12 + selectedOffset : 12) + 'px';
        }
        if (window.location.hash) {
            const id = window.location.hash.slice(1);
            const n = [...anchors].findIndex(a => a.id === id);
            setActiveLink(id, n);
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

buildBreadcrumbs(clickedMenuHistory);

window.onclick = function (e) {
    if (!e.target.closest('.dropdown-select') || e.target.parentElement.classList.contains('dropdown-select_options')) {
        document.querySelectorAll('.dropdown-select').forEach(function (item) {
            item.classList.remove('opened')
        });
    }
};

document.querySelectorAll('.dropdown-select span').forEach(function (item) {
    item.onclick = function () {
        item.closest('.dropdown-select').classList.toggle('opened');
    }
});

document.querySelectorAll('.dropdown-select').forEach(function (item) {
    var selected_version = item.querySelector('a[selected="selected"]');
    // select first version in dropdown if no selected version
    // this happens on build previews, because branch name isn't master there
    if (!selected_version) {
        selected_version = item.querySelector('a');
    }
    item.querySelector('span div').textContent = selected_version.textContent;
});

function selectVersion(value) {
    if (value.indexOf('archive') == -1 && window.currentVersionLink) {
        window.location = window.location.href.replace(window.currentVersionLink, value);
    } else {
        window.location = value;
    }
};
window.selectVersion = selectVersion;
