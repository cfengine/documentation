require 'fileutils'
require 'digest/md5'
require 'redcarpet'
require 'albino'

PYGMENTS_CACHE_DIR = File.expand_path('../../_cache', __FILE__)
FileUtils.mkdir_p(PYGMENTS_CACHE_DIR)

COMMAND_TYPE = "command"
OUTPUT_TYPE = "output"
FILE_TYPE = "file"
CODE_TYPE = "code"
DEFAULT_LANGUAGE = "text"

class Redcarpet2Markdown < Redcarpet::Render::HTML
  def block_code(code, lang)
    lang = lang || DEFAULT_LANGUAGE
    path = File.join(PYGMENTS_CACHE_DIR, "#{lang}-#{Digest::MD5.hexdigest code}.html")
    meta_data = process_meta_data(code)
    if lang == COMMAND_TYPE || lang == OUTPUT_TYPE
      meta_data = [lang]
      lang = DEFAULT_LANGUAGE
    elsif meta_data[0] == FILE_TYPE || meta_data[0] == OUTPUT_TYPE
      code = code.lines.to_a[1..-1].join #remove the first meta-line from the code
    end
    cache(path) do
      colorized = Albino.colorize(code, lang.downcase)
      add_code_tags(colorized, lang, meta_data)
    end
  end

  def add_code_tags(code, lang, meta_data)
    code
    .sub(
      /<pre>/,
      "<div class='code_block #{meta_data[0]}'><div><i class='#{meta_data[0]}'></i> #{meta_data[1] || meta_data[0]}</div>
      <pre><code class=\"#{lang}\">"
      )
    .sub(/<\/pre>/, "</code></pre></div>")
    .sub(/class="highlight"/, "class=\"highlight #{meta_data[0]}\"")

  end

  def process_meta_data(code)
    firstLine = code.lines.first ? code.lines.first.strip.strip : ""
    fileRegex = /^\[(file=)(?<file>.*)\]$/
    if fileRegex =~ firstLine
      file = firstLine.match(fileRegex)[:file]
      return FILE_TYPE, file
    elsif /^\[output\]$/ =~ firstLine
      return OUTPUT_TYPE, nil
    end

    return CODE_TYPE, nil
  end

  def cache(path)
    if File.exist?(path)
      File.read(path)
    else
      content = yield
      File.open(path, 'w') {|f| f.print(content) }
      content
    end
  end
end

class Jekyll::MarkdownConverter
  def extensions
    Hash[ *@config['redcarpet']['extensions'].map {|e| [e.to_sym, true] }.flatten ]
  end

  def markdown
    @markdown ||= Redcarpet::Markdown.new(Redcarpet2Markdown.new(extensions), extensions)
  end

  def convert(content)
    return super unless @config['markdown'] == 'redcarpet2'
    markdown.render(content)
  end
end