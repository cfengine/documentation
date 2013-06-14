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
    
    
    def sortNavBySortingKey(data, recursive=false)
      data.each  do |k, arr|
          if (recursive && arr.has_key?('childrens') && !arr['childrens'].empty?)
              data[k]['childrens'] = sortNavBySortingKey(arr['childrens'], true)
          end
      end
      
      
      begin
          return data.sort_by { |i, v| v['sorting'] }
          
          rescue
                  puts "-----------------------------------------------"
                  puts "ERROR: INDEX PAGE FOR THE CATEGORY IS MISSING. Check the first level section and find item without 'own_url' field"
                  puts JSON.pretty_generate(data)
                  puts "-----------------------------------------------"      
                  return nil
          ensure
      end      
  
    end

          
    def generate(site)

      # First remove all invisible items (default: nil = show in nav)
      published_pages = []

      site.pages.each do |page|
        published_pages << page if page.data["published"] != false
      end

      #puts JSON.pretty_generate(published_pages)

      # Create an array which consists of pages, placed by categories and levels
      nav_pages    = {}
      pages_levels = {}
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
              
              # if sorting is not set - use ASCII number
              if (p.data['sorting'] == nil)
                if (p.data['title'] != nil)
                  tmp[value]['sorting'] = (p.data['title'][0].ord)*100 + p.data['title'][1].ord
                else
                  tmp[value]['sorting'] = 10 
                end  
              else
                tmp[value]['sorting'] = p.data['sorting'].to_i
              end  
            end

            if tmp.has_key?('childrens') == false
              tmp[value]['childrens'] ||= {}
            end

            tmp = tmp[value]['childrens']
          end

        end
      end

      #puts JSON.pretty_generate(nav_pages)
      
      nav_pages = sortNavBySortingKey(nav_pages, true)
 
      $leftNavigation = {}
      $breadcrumbsNavigation = {}

      buildNavigation(nav_pages)


      #puts JSON.pretty_generate($breadcrumbsNavigation)

    site.config["leftNavigation"] = $leftNavigation;
    site.config["breadcrumbsNavigation"] = $breadcrumbsNavigation;

    end #/fnc


 def buildNavigation(navHash, parentSection='')
   if (navHash != nil && !navHash.empty?)
       navHash.each do |k, arr|

        # create unique key
        if (parentSection !='')
          itemKey = parentSection + '_' + k
        else
          itemKey = k
        end

        #puts JSON.pretty_generate(navHash)

        $leftNavigation[itemKey] ||= {}
        
        if (arr.has_key?('own_url') && !arr['own_url'].empty?)
          $breadcrumbsNavigation[itemKey] ||= {}
          $breadcrumbsNavigation[itemKey]['title'] = arr['own_url']['title']
          $breadcrumbsNavigation[itemKey]['alias'] = arr['own_url']['alias']
        else
          puts "--------------------------------------------------------"
          puts "WARNING: Page: " +  k + ". Full path: " + itemKey + " doesn't have right meta tags"  
          puts "--------------------------------------------------------"
        end


        #check if page has childrens and create level 1 and level2 pages if it has, and recursively call for childrens
          if (arr.has_key?('childrens') && !arr['childrens'].empty?)
                $leftNavigation[itemKey]['level1']    = buildSingleLevelNav(navHash, arr['own_url']['alias'])

                # level1RAW - we need this to be able to restore parent nav for pages without children
                $leftNavigation[itemKey]['level1RAW'] = getRawPagesArray(navHash)


                $leftNavigation[itemKey]['level2'] = buildSingleLevelNav(arr['childrens'], nil)

                buildNavigation(arr['childrens'], itemKey)

          else
            # if page doesn't have childrens => level 1 for it would be parent section or current section if there are no pages "above"
              if (parentSection !='' && $leftNavigation.has_key?(parentSection) &&  $leftNavigation[parentSection].has_key?('level1RAW') )
                $leftNavigation[itemKey]['level1'] = buildSingleLevelNav($leftNavigation[parentSection]['level1RAW'], nil)

                # level 2 would be current section
                $leftNavigation[itemKey]['level2']  = buildSingleLevelNav(navHash, arr['own_url']['alias'])

              else

                # current section - for page which doesn't have anything above (first level navigation)
                $leftNavigation[itemKey]['level1']  = buildSingleLevelNav(navHash, arr['own_url']['alias'])
              end

          end
        end
       end
    end

     def getRawPagesArray(hash)
        result = {}
        if (!hash.empty?)
            hash.each do |k, arr|
              if (arr.has_key?('own_url') && !arr['own_url'].empty?)
                result[k] = arr
              end
            end
         end

        return result
     end

     def buildSingleLevelNav(hash, currentPage='')
       result = []
       str = ''
           if (hash != nil && !hash.empty?)
               hash.each do |k, arr|
                  if (arr.has_key?('own_url') && !arr['own_url'].empty?)


                    if (currentPage ==  arr['own_url']['alias'])
                       # active page
                       result <<  '<li class="selected"><span>'+ arr['own_url']['title']  +'</span></li>';
                    else
                       result <<  '<li><a href="' + arr['own_url']['alias'] + '">'+ arr['own_url']['title']  +'</a></li>';
                    end
                  end
               end
           end

        if (!result.empty?)
          str ='<ul>' + result.join() + '</ul>'
        end

         return str
     end
  end



end