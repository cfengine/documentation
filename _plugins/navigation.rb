module Jekyll
  require File.dirname(__FILE__) + "/CfeUtils.rb"
  class Navigation < Generator
    $CfeUtils = CFE::CfeUtils.new
    $menu_items = {}

    def generate(site)
      site.pages.each do |page|
        if page.data["published"] != true || page.data['categories'] == nil || page.data['categories'].first() == "index"
          next
        end
        writePageIntoMenuItems(page)
      end
      puts $menu_items
      site.config["mainNavigation"] = "<ul>" + buildHtmlMenu($menu_items, 1) + "</ul>";
    end

    def writePageIntoMenuItems(page)
      tmp = $menu_items
      i = 0
      page.data['categories'].each do |category|
        i += 1
        category = $CfeUtils.removeUnvantedChars(category)
        tmp = initCategory(tmp, category)

        # write title and url to the last category which is page
        if page.data['categories'].length == i
          tmp['title'] ||= page.data['title']
          tmp['url'] ||= page.data['alias']
        end
        tmp = tmp['children']
      end
    end

    def initCategory(obj, category)
      if obj.has_key?(category) == false
        obj[category] ||= {}
        obj[category]['children'] ||= {}
      end
      return obj[category]
    end

    def buildHtmlMenu(items, level)
      html = ""
      items.sort_by{|k, v| v["title"]}.each do |key, item|
        hasChildren = !item["children"].nil? && !item["children"].empty?
        html += "<li class=\"#{(hasChildren ? 'parent' : '')} level-#{level}\" data-url=\"/#{item["url"]}\"><a href=\"#{item["url"]}\">#{item["title"]}</a>"
        if hasChildren
          html += '<ul>'
          html += buildHtmlMenu(item["children"], level + 1)
          html += '</ul>'
        end
        html += "</li>"
      end
      return html
    end
  end
end
