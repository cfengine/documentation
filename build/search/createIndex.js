const FlexSearch = require("flexsearch");
const fs = require('fs');
const {readdir} = require('fs').promises;

const htmlFilesDir = '../../_site';

const getHtmlFiles = async (dir) =>
    await Promise.all(
        (await readdir(dir, {withFileTypes: true}))
            // filter out non-html files and tags documents
            .filter(file => file.name.includes('.html') && !file.name.includes('tags-'))
            .map(file => file.name)
    );

(async () => {
    let index = new FlexSearch.Document({
        document: {
            id: 'number',
            index: ['content', 'title']
        },
        charset: "latin",
        tokenize: "full",
        matcher: "simple",
        cache: true
    })

    const htmlFiles = await getHtmlFiles(htmlFilesDir);
    let mappedFilesWithTitle = [];
    for (const key in htmlFiles) {
        const htmlContent = fs.readFileSync(`${htmlFilesDir}/${htmlFiles[key]}`).toString();
        let document = {
            number: key, // use sequential number as key to reduce search index size
            content: htmlContent.match(/<article>([\s\S]*?)<\/article>/gm)[0].replace(/<\/?[^>]+(>|$)/g, ""),
        };
        const titleMatch =  htmlContent.match(/<h1 id="top">([\s\S]*?)<\/h1>/gm);

        if (titleMatch != null) {
            const title = titleMatch[0].replace(/<\/?[^>]+(>|$)/g, "").trim();
            mappedFilesWithTitle.push({uri: (htmlFiles[key]), title })
            document.title = title;
        }

        index.add(document)
    }

    fs.writeFileSync(`searchIndex/fileNamesMap.json`, JSON.stringify(mappedFilesWithTitle));
    index.export((key, data) => fs.writeFileSync(`searchIndex/${key}.json`, data || ''));
})();
