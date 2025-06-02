const fs = require('fs');
const path = require('path');

const contentPath = path.resolve(__dirname + '/../content');
const menuHtmlPath = path.resolve(__dirname + '/../layouts/partials/mainMenu.html');
const contentTreeToJson = require('./contentTreeToJson.js');


const buildHtmlMenuFromJsonTree = function (jsonTree, level) {
    let html = '';

    if (Array.isArray(jsonTree)) {
        for (const key in jsonTree) {
            const item = jsonTree[key];
            const isParent = item.hasOwnProperty('children');
            html += `<li class="${isParent ? 'parent' : ''} level-${level}" data-url="${item.url}">${isParent ? '<i></i>' : ''}<a href="${item.url}">${item.title}</a>`;
            if (isParent) {
                html += '<ul>';
                html += buildHtmlMenuFromJsonTree(item.children, level++);
                html += '</ul>';
            }
            html += '</li>';
        }

    } else if (jsonTree.hasOwnProperty('children')) {
        html += buildHtmlMenuFromJsonTree(jsonTree.children, level++);
    }

    return html;
}


const orderedJsonFilesTree = contentTreeToJson.orderJsonTree((contentTreeToJson.process(contentPath, contentPath)));
const menuHtml = buildHtmlMenuFromJsonTree(orderedJsonFilesTree, 1);
fs.writeFileSync(menuHtmlPath, menuHtml);

