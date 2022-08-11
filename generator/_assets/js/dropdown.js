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
    var selected = item.querySelector('a[selected="selected"]').textContent;
    item.querySelector('span div').textContent = selected;
});
