const FlexSearch = require("flexsearch");
const fs = require('fs');
const path = require('path');
const {readdir} = require('fs').promises;
const contentTreeToJson = require('../../contentTreeToJson');
const {process} = require("../../contentTreeToJson");

const contentPath = path.resolve(__dirname + '/../../../content');

(async () => {
    let index = new FlexSearch.Document({
        document: {
            id: 'number',
            index: ['content', 'headers', 'title']
        },
        charset: "latin",
        tokenize: "full",
        matcher: "simple",
        cache: true
    })


    let docIndex = 0;
    const buildIndex = function (jsonTree, breadCrumbs = []) {

        for (const item of jsonTree) {
            docIndex++;
            const content = fs.readFileSync(item.filename).toString();
            const headersMatches = content.matchAll(/^\s*#{1,6}\s*(.*?)$/gm);
            let copiedBC = [...breadCrumbs];
            copiedBC.push({title:  item.title, url:  item.url});

            let document = {
                number: docIndex,
                content: content
                    .replace(/(---|\+\+\+)[\S\s]*?(---|\+\+\+)/gm, " ") // remove frontmatter
                    .replace(/[^a-zA-Z0-9_\(\.\)\'\"\:]/g, ' ') // remove chars except alphanumeric, (, ), ., ', ", :
                    .replace(/\s\s+/g, ' ') // remove extra spaces
                    .replace(/\n/g, " ") // remove newlines
                    .replace('Suggest changes', ''),
                title: item.title,
                headers: item.title,
                headersMap: {'top': item.title}
            };

            if (headersMatches) {
                for (const match of headersMatches) {
                    const header = match[1];
                    const headerId = header
                        .replace(/\W+/g, '-')
                        .replace(/-$/, '')
                        .toLowerCase();
                    document.headers += ` ${header}`;
                    document.headersMap[headerId] = header;
                }
            }

            fs.writeFileSync(path.resolve(__dirname + `/documents/${docIndex}.json`), JSON.stringify({
                ...document,
                uri: item.url,
                breadCrumbs: copiedBC
            }));

            index.add(document);

            if (item.hasOwnProperty('children')) {
                buildIndex(item.children, copiedBC);
            }
        }
    }

    const jsonTree = contentTreeToJson.orderJsonTree(contentTreeToJson.process(contentPath, contentPath));
    buildIndex(jsonTree.children);

    index.export((key, data) => fs.writeFileSync(path.resolve(__dirname + `/searchIndex/${key}.json`), data || ''));
})();
