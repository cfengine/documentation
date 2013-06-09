require 'fileutils'
require 'digest/md5'
require 'redcarpet'
require 'albino'

require 'sanitize'

class Redcarpet2Markdown <  Redcarpet::Render::HTML

    # wrap table with div
    def table(header, body)
        return '<div class="tableOverflow"><table><thead>' + header + '</thead><tbody>' + body + '</tbody></table></div>'
    end

    # add id attribute to the headers
    def header(text, header_level)
        # clean string from html
        stringHeader = Sanitize.clean(text)

        # replace all unwanted characters to space
        stringHeader = stringHeader.downcase.gsub(/[^a-z0-9_-]+/i, " ")

        # strip whitespaces from the beginning and end of a string
        stringHeader = stringHeader.strip

        # replace all unwanted characters to -
        stringHeader = stringHeader.downcase.gsub(/[^a-z0-9_-]+/i, "-")

        # convert number to string
        stringHeaderNum = header_level.to_s

        # create header
        result = '<h' + stringHeaderNum + ' id="' + stringHeader + '">' + text + '</h' + stringHeaderNum + '>'

        return result
    end
end