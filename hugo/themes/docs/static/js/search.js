const queryParams = new URLSearchParams(window.location.search);
const searchInput = document.getElementById('top_search');
const searchResults = document.getElementById('searchResults');
const searchFor = document.querySelector('.searchQuery');
const resultsCount = document.querySelector('.resultsCount span');

const buildBreadCrumbs = breadCrumbs => {
    let html = '';

    for (const bc of breadCrumbs) {

        if (html.length > 0) { // add bc divider before items, except the first one
            html += '<li>/</li>';
        }

        html += `<li itemProp="itemListElement" itemScope="" itemType="http://schema.org/ListItem">
                     <a itemID="examples-tutorials.html" itemProp="item" itemScope="" itemType="http://schema.org/Thing" href="${bc.url}"> 
                         <span itemProp="name">${bc.title}</span> 
                     </a>
                 </li>`;
    }

    return html;
}
const displayResults = (results) => {
    let html = '<ul>';
    resultsCount.innerHTML = results.length;
    if (results.length > 0) {
        for (const result of results) {
            html += `<li ${result.foundHeaderId ? 'class="headerItem"' : ''}">
                         <div id="breadcrumbs">
                             <ul itemscope="" itemtype="http://schema.org/BreadcrumbList">${buildBreadCrumbs(result.breadCrumbs)}</ul>
                         </div>
                         <a href="${result.uri}">${result.title}</a>
                         <div class="search-description">${result.content}</div>
                     </li>`;
        }
        html += `</ul>`;
    } else {
        html = `No results found`;
    }

    searchResults.innerHTML = html;
}
const searchBase = document.querySelector('meta[name="search-base"]').content;
const search = searchQuery =>
    fetch(`${searchBase}?searchQuery=${searchQuery}`)
        .then(response => response.json()).then(data => displayResults(data))
        .catch(() => searchResults.innerTextr = 'An error happened while search');

searchInput.oninput = searchInput.onchange = () => {
    search(searchInput.value);
    searchFor.innerText = searchInput.value;
}

if (queryParams.has('q')) {
    searchInput.value = queryParams.get('q');
    searchFor.innerText = queryParams.get('q');
    searchInput.dispatchEvent(new Event('change'));
}
