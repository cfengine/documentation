module Jekyll
  require "pp"
  require "json"
  require File.dirname(__FILE__) + "/CfeUtils.rb"

  class SiteNavigation < Jekyll::Generator
    safe true
    priority :lowest
    
    $CfeUtils = CFE::CfeUtils.new
    
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
        key=''
        if p.data['categories'] != nil

          p.data['categories'].each do |value|
            value = $CfeUtils.removeUnvantedChars(value)
            
            # create proper page key with parent->child like category1_category2_category3_....
            # to ensure that we won't have pages with same keys so they can overwrite each other
            if (key == '') 
              key = value
            else
              key = key + '_' + value
            end
            
            if tmp.has_key?(key) == false
              tmp[key] ||= {}
            end

            i += 1

            if p.data['categories'].length == i
              if tmp[key].has_key?('childrens') == false
                tmp[key]['childrens'] ||={}
              end
            end

            if p.data['categories'].length == i
              struct = {}
              struct['published'] = p.data['published']
              struct['title']     = p.data['title']
              struct['type']      = 'page'
              struct['alias']     = p.data['alias']
              struct['level']     = i

              tmp[key]['own_url'] ||= {}
              tmp[key]['own_url'] = struct
              
              # if sorting is not set - use ASCII number
              if (p.data['sorting'] == nil)
                if (p.data['title'] != nil)
                  tmp[key]['sorting'] = (p.data['title'][0].ord)*100 + p.data['title'][1].ord
                else
                  tmp[key]['sorting'] = 10 
                end  
              else
                tmp[key]['sorting'] = p.data['sorting'].to_i
              end  
            end

            if tmp.has_key?('childrens') == false
              tmp[key]['childrens'] ||= {}
            end

            tmp = tmp[key]['childrens']
          end

        end
      end

     
      nav_pages = sortNavBySortingKey(nav_pages, true)
      
     # puts JSON.pretty_generate(nav_pages) 
     # puts "-- after sort --"

      
      linksForNavigation = {}
      linksForNavigation = createResultArray(nav_pages)

       

      # create flatten array for all existin pages in navigation     
      
      #puts " result" 
      #puts JSON.pretty_generate(linksForNavigation) 
      #puts "-- --"
 

      $breadcrumbsNavigation = {}
      $leftNavigation = {}
      buildNavigation(linksForNavigation)  
   
      
      leftNavHtml = {}
      leftNavHtml = buildLeftNavHTML($leftNavigation)


      # temporal solution for the index page. because we don't know what to show there
      indexMenu = ''
      $result.each do |page, pageData|

        if (page != 'index' && pageData['level'] == 1)
          indexMenu += '<li><a href="' + pageData['alias']  +'">' + pageData['title'] + '</a></li>'
        end  
        
        leftNavHtml['index'] = '<ul>' + indexMenu + '</ul>'
      end  

      site.config["leftNavigation"] = leftNavHtml;
      site.config["breadcrumbsNavigation"] = $breadcrumbsNavigation;

    end #/fnc


    # Build html list navigation based on $leftNavigation
    # navigationsArray - source array
    #
    # return array with the html navigation list for each pages
    
    
   def buildLeftNavHTML(navigationsArray)
      result ||= {}

      navigationsArray.each do |pageKey, pageData|
        li = ''

          
        if (pageData['level'] == 1)
          li += getLI_forchildrenstHTML(pageData['childrens'], pageKey)
        elsif(pageData['level'] == 3) 
          if (pageData.has_key?('parentReference') &&  !pageData['parentReference'].empty?)
             key = pageData['parentReference']['parentKey']
             activeLink = pageKey
             li = get2levelList(pageData['parentReference']['parentKey'], pageData['parentReference']['parentData'][key], activeLink);
          end 
        else
          li = get2levelList(pageKey, pageData, pageKey);
        end   
        
        result[pageKey] = '<ul>' + li + '</ul>'
      end  
      return result
   end
   
   
   # returns 2 level of html list
   # params
   # pageKey - current page
   # pageData array od pages including 2 level
   # activeLink - which link should be set as active. this is equal to the pageKey in all cases except level3
   
   def get2levelList(pageKey, pageData, activeLink)
      if (pageData == nil && pageData.empty?)
        puts "Empty data"
        return  ''
      end 
       
      if (!pageData.has_key?('uncles')  || pageData['uncles'].empty?)
        puts "Empty data"
        return  ''
      end   
   
      li_level1 = '' 
          
      pageData['uncles'].each do |uncleKey, unclePageData|
      
      li_level1 += '<li>'
      if (uncleKey != pageKey)
        li_level1 += '<a href="' + unclePageData['alias']  +'">' + unclePageData['title'] + '</a>'
       
      else
        if pageKey == activeLink
          li_level1 += '<a class="active" href="' + pageData['alias']  +'">' + pageData['title'] + '</a>'
        else
          li_level1 += '<a href="' + pageData['alias']  +'">' + pageData['title'] + '</a>'  
        end
        
        # show all childrens if  available
        if (pageData.has_key?('childrens') && !pageData['childrens'].empty?)
          li_level1 += '<ul class="level2">' + getLI_forchildrenstHTML(pageData['childrens'], activeLink) + '</ul>'
        end  
      end  
      
      li_level1 += '</li>'
      end  
    return li_level1
   end  
   
    
    # Return html string with <li> for given array of links
    #
    #
    
    def getLI_forchildrenstHTML(data, activeLink)
      if (data == nil && data.empty?)
        #puts "Empty data"
        return  
      end  
      
      li = ''
      
      data.each do |pageId, pageData|
        li += '<li>'
        if (activeLink == pageId)
          li += '<a class="active" href="' + pageData['alias']  +'">' + pageData['title'] + '</a>'  
        else
          li += '<a href="' + pageData['alias']  +'">' + pageData['title'] + '</a>'  
        end
        li += '</li>'
      end  
      return  li 
    end

   
    # This funtion returns array of pages for each page.
    # navHash is array of chaned pages, pageLevel1->pageLeve2... ->pagelevel3
    # we must have chain for each page, in order to build simple list for left navigation
    
    # this function also prepare breadcrumb array
    
   
    def buildNavigation(navHash, parentItemKey = '')
       if (navHash == nil && navHash.empty?)
        puts "Empty hash "
        return  
       end  
    
    
       navHash.each do |pageId, pageData|

         itemKey = $CfeUtils.removeUnvantedChars(pageId)

          $leftNavigation[itemKey] ||= {}
        
          if (pageData.has_key?('alias') && !pageData['alias'].empty?)
            $breadcrumbsNavigation[itemKey] ||= {}
            $breadcrumbsNavigation[itemKey]['title'] = pageData['title']
            $breadcrumbsNavigation[itemKey]['alias'] = pageData['alias']
          else
            puts "--------------------------------------------------------"
            puts "WARNING: Page: " +  k + ". Full path: " + itemKey + " doesn't have right meta tags"  
            puts "--------------------------------------------------------"
          end


         $leftNavigation[itemKey] ||= {}
         $leftNavigation[itemKey]['childrens'] ||= {}
         
         if (parentItemKey != '')
           
         # we need pages which are in the same lavel as current,
         # best way to do this is to get parent level page children  
         $leftNavigation[itemKey]['uncles'] ||= {} 
          if (!$leftNavigation[parentItemKey].empty?)
          $leftNavigation[itemKey]['uncles'] = $leftNavigation[parentItemKey]['childrens']
          end
         end
        

          
          # current page properties
             $leftNavigation[itemKey]['alias'] = pageData['alias']
             $leftNavigation[itemKey]['title'] = pageData['title']
             $leftNavigation[itemKey]['level'] = pageData['level']
             
             

           if (!pageData.empty? && !pageData.has_key?('childrens'))
            #puts "Empty hash level2. Key=" + itemKey
            # for the 3-rd level pages we must set their parent reference
            if (pageData['level'] == 3)
              $leftNavigation[itemKey]['parentReference'] ||= {}
              $leftNavigation[itemKey]['parentReference']['parentKey'] = parentItemKey
              $leftNavigation[itemKey]['parentReference']['parentData'] ||= {}
              $leftNavigation[itemKey]['parentReference']['parentData'][parentItemKey] = $leftNavigation[parentItemKey]
            end
            next  
           end  
            
        
         # level 1
           pageData['childrens'].each do |pageKey, pages|
               pageKey = $CfeUtils.removeUnvantedChars(pageKey)
               $leftNavigation[itemKey]['childrens'][pageKey] ||= {}
               $leftNavigation[itemKey]['childrens'][pageKey]['alias'] = pages['alias']
               $leftNavigation[itemKey]['childrens'][pageKey]['title'] = pages['title']
               $leftNavigation[itemKey]['childrens'][pageKey]['level'] = pages['level']
           end 

           #recursively call for all 2 level pages
           buildNavigation(pageData['childrens'], itemKey)
       end
    end
    
    
    def createResultArray(nav_pages)
      $result = {}
     nav_pages.each do |k, arr|
  
        # puts arr
        itemKey = $CfeUtils.removeUnvantedChars(k)
     
        $result[k] ||= {}

        $result[k]['title'] = arr['own_url']['title'];
        $result[k]['alias'] = arr['own_url']['alias'];
        $result[k]['level'] = arr['own_url']['level'];
     
     
        
        if (arr['own_url']['level'] == 1)
            if (arr.has_key?('childrens') && !arr['childrens'].empty?)
              
              $result[k]['childrens'] ||= {}
              
              
                arr['childrens'].each do |level1_k, level1_p|
                  
                
                  $result[k]['childrens'][level1_k] ||={}
                  $result[k]['childrens'][level1_k]['title'] = level1_p['own_url']['title']
                  $result[k]['childrens'][level1_k]['alias'] = level1_p['own_url']['alias']
                  $result[k]['childrens'][level1_k]['level'] = level1_p['own_url']['level'];
                  

                      if (level1_p.has_key?('childrens') && !level1_p['childrens'].empty?)
                    
                          $result[k]['childrens'][level1_k] ||= {}
                    
                          level1_p['childrens'].each do |level2_k, level2_p|
                              $result[k]['childrens'][level1_k]['childrens'] ||= {}
                              $result[k]['childrens'][level1_k]['childrens'][level2_k] ||= {}
                              $result[k]['childrens'][level1_k]['childrens'][level2_k]['title'] = level2_p['own_url']['title']
                              $result[k]['childrens'][level1_k]['childrens'][level2_k]['alias'] = level2_p['own_url']['alias']
                              $result[k]['childrens'][level1_k]['childrens'][level2_k]['level'] = level2_p['own_url']['level']

                          
                              if (level2_p.has_key?('childrens') && !level2_p['childrens'].empty?)
                                puts "--------------------------------------------------------"
                                puts "WARNING: Page: " +  level2_k + " is 3 level page and it has some childrens (sublevels)." 
                                puts "Please review your document structure. All sublevels after level 3 will be ignored "  
                                puts "--------------------------------------------------------"
                              end
                          end
                      end  #first level if
                end  # first level loop
            end ## second if
        end ## first if   
      end  #loop
      
      return $result
    end
    
    
    
   end #class
end