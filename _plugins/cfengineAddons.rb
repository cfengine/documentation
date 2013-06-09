require 'fileutils'
require 'digest/md5'
require 'redcarpet'
require 'albino'


class Redcarpet2Markdown <  Redcarpet::Render::HTML

    # wrap table with div
    def table(header, body)
        return '<div class="tableOverflow"><table><thead>' + header + '</thead><tbody>' + body + '</tbody></table></div>'
    end
end