const http = require('node:http');
const FlexSearch = require("flexsearch");
const fs = require('fs');
const url = require('url');
const searchResultsCount = 15;

const port = 8082;

const searchFilesPath = '/usr/share/search/index';

const fetchIndex = () => {
    let index = new FlexSearch.Document({
        document: {
            id: 'number',
            index: ['title', 'headers', 'content']
        },
        charset: "latin",
        tokenize: "full",
        matcher: "simple",
        cache: true
    });

    if (!fs.existsSync(searchFilesPath)) {
        throw new Error(`Search index does not exist`);
    }

    const keys = fs
        .readdirSync(`${searchFilesPath}/searchIndex`, {withFileTypes: true})
        .filter(item => !item.isDirectory() && item.name.includes('.json'))
        .map(item => item.name.slice(0, -5)); // remove .json from file name

    keys.map(key => {
        const data = fs.readFileSync(`${searchFilesPath}/searchIndex/${key}.json`, 'utf8')
        index.import(key, data ?? null)
    })

    return index;
}

const makeOccurredSubstringBold = (text, substring) => {
    const occurrenceIndex = text.toLocaleLowerCase().indexOf(substring.toLocaleLowerCase());
    if (occurrenceIndex > -1) {
        let contentArr = text.split('');
        contentArr.splice((occurrenceIndex + substring.length), 0, '</b>')
        contentArr.splice(occurrenceIndex, 0, '<b>');
        text = contentArr.join('');
    }
    return text;
}

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');

    const parsedURL = url.parse(req.url, true);
    const searchQuery = parsedURL.query.searchQuery;

    if (!searchQuery) {
        res.statusCode = 409;
        res.end('searchQuery is required\n');
        return;
    }


    const index = fetchIndex();
    let ids = [];
    let headerIds = [];
    index.search(searchQuery, searchResultsCount).forEach(item => {
        if (item.field == 'headers') {
            headerIds = item.result;
        }
        ids.push(...item.result)
    });
    const searchRes = [...new Set(ids)].slice(0, searchResultsCount).map(key => {
        const document = JSON.parse(fs.readFileSync(`${searchFilesPath}/documents/${key}.json`, 'utf8'));
        const contentLength = document.content.length;
        const indexOfQuery = document.content.toLocaleLowerCase().indexOf(searchQuery.toLocaleLowerCase());

        if (indexOfQuery == -1 || indexOfQuery < 80) { // if no findings or index of a finding less than 80 return first 160 chars
            document.content = document.content.substring(0, 160) + '...';
        } else if ((indexOfQuery + 80) > contentLength) { // if a finding + 80 chars more than content length then return last 160 chars
            document.content = document.content.substring(contentLength - 160) + '...';
        } else { // return text with a finding surronded by 80 chars from left and right sides
            document.content = '...' + document.content.substring((indexOfQuery - 80), (indexOfQuery + 80)) + '...';
        }

        if (headerIds.includes(key)) {
            Object.keys(document.headersMap).forEach((id) => {
                // if there is exact text match in a title then extend the URI with the header id and change result title
                // to header
                if (!document.foundHeaderId && document.headersMap[id].toLocaleLowerCase().indexOf(searchQuery.toLocaleLowerCase()) > -1) {
                    document.foundHeaderId = id;
                    document.isExactMatch = document.headersMap[id].toLocaleLowerCase().trim() == searchQuery.toLocaleLowerCase().trim();
                    document.uri += `#${id}`;
                    document.title = document.headersMap[id];
                }
            });

        } else if (indexOfQuery > -1) {
            // if there is exact text match then extend the URI with Scroll To Text Fragment Chrome feature
            // which will scroll to finding
            document.uri += `#:~:text=${searchQuery}`;
        }

        document.content = makeOccurredSubstringBold(document.content, searchQuery);

        return document;
    })
        // results with partial search query occurrence in a header are ranked higher
        .sort((a, b) =>
            (b.hasOwnProperty('foundHeaderId') ? 1 : 0) - (a.hasOwnProperty('foundHeaderId') ? 1 : 0))
        // results with exact search query match in a header are ranked higher
        .sort((a, b) =>
            (b.hasOwnProperty('isExactMatch') && b.isExactMatch ? 1 : 0) - (a.hasOwnProperty('isExactMatch') && a.isExactMatch ? 1 : 0));
    // return unique first ${searchResultsCount} elements
    res.end(JSON.stringify(searchRes));
});

server.listen(port);
