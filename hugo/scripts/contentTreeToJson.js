const fs = require('fs');
const path = require('path');

module.exports = {
    process: function (filename, contentPath) {
        // skip if not directory or .md file
        if (!['', '.md', '.markdown'].includes(path.extname(filename)) || path.basename(filename) == '_index.md' | path.basename(filename) == '_index.markdown') {
            return;
        }

        let result = {
            url: filename.replace(contentPath, '').replace(path.extname(filename), '') + '/',
            title: null,
            sorting: 100
        };

        const fileStat = fs.lstatSync(filename);
        let content = '';

        const titleRegex = /^title:(.*)$/m;
        const sortingRegex = /^sorting:*.(\d+)$/m;
        const unpublishedRegex = /^(published:*.+(false)|draft:*.+(true)|hidden:*.+(true))$/m;

        if (fileStat.isDirectory()) {
            const indexFilePath = filename + '/_index.markdown';
            try {
                content = fs.readFileSync(indexFilePath, "utf8");
            } catch (e) {
                console.log(`Directory index file '${indexFilePath}' is not found.`);
                return;
            }
            result.children = fs.readdirSync(filename).map(childItem => this.process(filename + '/' + childItem, contentPath));
            result.filename = indexFilePath;
        } else {
            try {
                content = fs.readFileSync(filename, "utf8");
                result.filename = filename;
            } catch (e) {
                console.log(`File '${filename}' cannot be opened: ${e.toString()}`)
            }
        }

        if (unpublishedRegex.test(content)) {
            return;
        }

        if (titleRegex.test(content)) {
            result.title = content.match(titleRegex)[1].trim();
        }

        if (sortingRegex.test(content)) {
            result.sorting = parseInt(content.match(sortingRegex)[1]);
        }

        return result;
    },

    orderJsonTree: function (tree) {
        if (Array.isArray(tree)) {
            tree = tree.filter(item => item !== undefined).sort((a, b) => a.sorting - b.sorting);

            for (const key in tree) {
                if (tree[key].hasOwnProperty('children')) {
                    tree[key].children = this.orderJsonTree(tree[key].children);
                }
            }

        } else if (tree.hasOwnProperty('children')) {
            tree.children = this.orderJsonTree(tree.children);
        }

        return tree;
    }
}
