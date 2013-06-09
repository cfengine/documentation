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

      #puts JSON.pretty_generate(breadcrumbs)


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
              struct['sortkey']   = p.data['sortkey']
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
#
      #puts JSON.pretty_generate(nav_pages)

      # Sort all pages by alphabet in all levels - recursively
      # if failed - add this to convert keys{|x, y| x.to_s <=> y.to_s}
      nav_pages = sort_by_key(nav_pages, true)

      #puts JSON.pretty_generate(nav_pages)
  
      $leftNavigation = {}
      
      buildLeftNavigation(nav_pages)
      

    
    site.config["leftNavigation"] = $leftNavigation;

    end #/fnc
      
      
 def buildLeftNavigation(navHash, parentSection='')
       navHash.each do |k, arr|
        $leftNavigation[k] ||={}
       
        #check if page has childrens and create level 1 and level2 pages if it has, and recursively call for childrens
          if (arr.has_key?('childrens') && !arr['childrens'].empty?)
                $leftNavigation[k]['level1']    = buildSingleLevelNav(navHash, arr['own_url']['alias'])

                # level1RAW - we need this to be able to restore parent nav for pages without children
                $leftNavigation[k]['level1RAW'] = getRawPagesArray(navHash)
                
                
                $leftNavigation[k]['level2'] = buildSingleLevelNav(arr['childrens'], nil) 
                
                buildLeftNavigation(arr['childrens'], k)
          
          else
            # if page doesn't have childrens => level 1 for it would be parent section or current section if there are no pages "above"
             
              if (parentSection !='' && $leftNavigation.has_key?(parentSection))
                $leftNavigation[k]['level1'] = buildSingleLevelNav($leftNavigation[parentSection]['level1RAW'], nil)
               
                # level 2 would be current section
                $leftNavigation[k]['level2']  = buildSingleLevelNav(navHash, arr['own_url']['alias'])
               
              else

                # current section - for page which doesn't have anything above (first level navigation)
                $leftNavigation[k]['level1']  = buildSingleLevelNav(navHash, arr['own_url']['alias'])
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
           if (!hash.empty?)
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