module Jekyll
  require "pp"
  require "json"

  class SiteNavigation < Jekyll::Generator
    safe true
    priority :lowest
    ## sort keys inside hash
    def sort_by_key(data, recursive=false, &block)
      data.keys.sort(&block).reduce({}) do |seed, key|
        seed[key] = data[key]
        if recursive && seed[key].is_a?(Hash)
          seed[key] = sort_by_key(seed[key], true, &block)
        end
        seed
      end
    end

    def generate(site)

      # First remove all invisible items (default: nil = show in nav)
      published_pages = []

      site.pages.each do |page|
        published_pages << page if page.data["published"] != false
        #published_pages << page
      end

      #puts JSON.pretty_generate(published_pages)

      #create breadcrumbs array
      breadcrumbs = {}
      published_pages.each do |p|
        if p.data['categories'] !=nil
          key = p.data['categories'].last
          breadcrumbs[key] ||={}
          breadcrumbs[key]['title'] = p.data['title']
          breadcrumbs[key]['alias'] = p.data['alias']
        end
      end
      site.config["breadcrumbsAll"] = breadcrumbs
      # puts JSON.pretty_generate(breadcrumbs)

      # Create an array which consists of pages, placed by categories and levels
      nav_pages = {}
      published_pages.each do |p|

        tmp = nav_pages
        i = 0
        if p.data['categories'] != nil

          p.data['categories'].each do |value|

            if tmp.has_key?(value) == false
              tmp[value] ||= {}
            end

            i += 1

            if p.data['categories'].length == i
              if tmp[value].has_key?('childrens') == false
                tmp[value]['childrens'] ||={}
              end
            end

            if p.data['categories'].length == i
              struct = {}
              struct['published'] = p.data['published']
              struct['title']     = p.data['title']
              struct['type']      = 'page'
              struct['alias']     = p.data['alias']

              tmp[value]['own_url'] ||= {}
              tmp[value]['own_url'] = struct
            end

            if tmp.has_key?('childrens') == false
              tmp[value]['childrens'] ||= {}
            end

            tmp = tmp[value]['childrens']
          end

        end
      end

      # puts JSON.pretty_generate(nav_pages)

      # Sort all pages by alphabet in all levels - recursively
      # if failed - add this to convert keys{|x, y| x.to_s <=> y.to_s}
      nav_pages = sort_by_key(nav_pages, true)

      #puts JSON.pretty_generate(nav_pages)

      # Generate html list with pages
      # nav_level1 - store data for first level only - used to click and open
      # nav_html[] - store level2 and next levels

      level1 = '';
      li = ''

      nav_html = {}

      nav_pages.each do |k, arr|
        li += '<li><a href="#"  class="' + k.downcase.gsub(/[^a-z0-9_-]+/i, "-") +'">' + k + '</a></li>'
        nav_html[k] ||={}
        nav_html[k]['key']  = k
        nav_html[k]['data'] = HtmlListMaker.new(arr['childrens']).list
      end

      nav_level1 = '<ul id="nav_level1">' + li + "</ul>"

      #puts JSON.pretty_generate(nav_html)

      # Access this in Liquid using: site.html_nav_list
      site.config["nav_level1_html"] = nav_level1
      site.config["nav_levels_html"] = nav_html
    end
  end
end