module Jekyll

  module TextFilter
  def cleanString(input)
    return input.gsub(/[^a-z0-9_-]+/i, "-")
  end
end

end

Liquid::Template.register_filter Jekyll::TextFilter