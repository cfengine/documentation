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
    for (const key in htmlFiles) {
        const htmlContent = fs.readFileSync(`${htmlFilesDir}/${htmlFiles[key]}`).toString();
        const htmlContentMatch = htmlContent.match(/<div class="article">([\s\S]*?)<div id="tags">/gm);
        const titleMatch = htmlContent.match(/<h1 id="top">([\s\S]*?)<\/h1>/gm);
        if (htmlContentMatch == null || titleMatch == null) continue;
        let document = {
            number: key, // use sequential number as key to reduce search index size
            content: htmlContentMatch[0]
                .replace(/<\/?[^>]+(>|$)/g, "")
                .replace(/\s\s+/g, ' ')
                .replace(/\n/g, " ")
                .replace('Suggest changes', ''),
            title: titleMatch[0].replace(/<\/?[^>]+(>|$)/g, "").trim(),
        };
        let breadCrumbs = '';
        const breadCrumbsMatch = htmlContent.match(/<div id="breadcrumbs">([^]*?)<\/div>/gm);
        if (breadCrumbsMatch != null) {
            breadCrumbs = breadCrumbsMatch[0].replace(/\s\s+/g, ' ').replace(/\n/g, " ");
        }

        fs.writeFileSync(`searchIndex/documents/${key}.json`, JSON.stringify({
            ...document,
            uri: (htmlFiles[key]),
            breadCrumbs
        }));
        index.add(document)
    }

    index.export((key, data) => fs.writeFileSync(`searchIndex/${key}.json`, data || ''));
})();
