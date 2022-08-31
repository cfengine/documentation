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
    // select first version in dropdown if no selected version
    // this happens on build previews, because branch name isn't master there
    var selected = item.querySelector('a[selected="selected"], a').textContent;
    item.querySelector('span div').textContent = selected;
});
