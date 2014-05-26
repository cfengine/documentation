module Jekyll
  require File.dirname(__FILE__) + "/CfeUtils.rb"

  module CfeLiquidUtils

    CfeUtils = CFE::CfeUtils.new

    def removeUnvantedChars(input)
      return CfeUtils.removeUnvantedChars(input)
    end

    # return posts array sorted by title (case insensitive)
    def sortPostsByTitle(arrayOfPosts)
      return arrayOfPosts.sort{ |a,b|  a.data['title'].downcase <=> b.data['title'].downcase }
    end

  end
end
Liquid::Template.register_filter Jekyll::CfeLiquidUtils