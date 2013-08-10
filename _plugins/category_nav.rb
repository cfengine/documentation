module Jekyll
  require "pp"
  require "json"
  require File.dirname(__FILE__) + "CfeUtils.rb"

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
      
      #puts JSON.pretty_generate(nav_pages) 
 
      $leftNavigation = {}
      $breadcrumbsNavigation = {}
      $parent = '';

      buildNavigation(nav_pages)
      
      leftNavHtml = {}
      
      leftNavHtml = buildLeftNavHTML($leftNavigation)

      site.config["leftNavigation"] = leftNavHtml;
      site.config["breadcrumbsNavigation"] = $breadcrumbsNavigation;

    end #/fnc

    
    # Build html list navigation based on $leftNavigation
    # navigationsArray - source array
    #
    # returny array with the html navigation list for each pages
    
    def buildLeftNavHTML(navigationsArray)
      result ||= {}  

      navigationsArray.each do |k, arr|
        str = '';
        
        # becouse navigation already exist, we can set level1 = level0 to use same code for html rendering
        if (arr.has_key?('level0') && !arr['level0'].empty?)
          arr['level1'] = arr['level0']
        end  #if level0
            
            arr['level1'].each do |pageKey, page|
                # check if this page is current
                if (pageKey == k)
                  str += '<li class="selected"><span>' + page['title'] + '</span>'
                else
                  str += '<li>' + '<a href="' + page['alias']  +'">' + page['title'] + '</a>'
                end

                        ## second level
                        if (page.has_key?('childrens') && !page['childrens'].empty?)
                          str += '<ul class="level2">'
            
                          page['childrens'].each do |childrensKey, childrensPage|
                            # check if this page is current
                            if (childrensKey == k)
                              str += '<li class="selected"><span>' + childrensPage['title'] + '</span></li>'
                            else
                              str += '<li><a href="'+ childrensPage['alias'] +'">' + childrensPage['title'] + '</a></li>'
                            end
                          end
                          str += '</ul>'
                        end
                str += '</li>'
            end #loop level0          
        

       result[k] = "<ul>" + str + "</ul>"
      end #loop nav
      return result
    end #func

  # Build breadcrumbs and left navigation hashes with level1 and level2 separation
  # this function works with $leftNavigation and $breadcrumbsNavigation global varibles
  #
  # navHash - hash with all pages from jekyll
  # parentSection - reference for proper parent->child linking
  # 
 def buildNavigation(navHash, parentSection='')
   if (navHash != nil && !navHash.empty?)
       navHash.each do |k, arr|

          itemKey = $CfeUtils.removeUnvantedChars(k)
  
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
      
          $leftNavigation[itemKey]['level1'] ||= {}
          
            navHash.each do |pageKey, pages|
              # create first level pages
              $leftNavigation[itemKey]['level1'][pageKey] ||= {}
              $leftNavigation[itemKey]['level1'][pageKey]['alias'] = pages['own_url']['alias']
              $leftNavigation[itemKey]['level1'][pageKey]['title'] = pages['own_url']['title']
   
              # check if page has children
              if ( pageKey == k && arr.has_key?('childrens') && !arr['childrens'].empty?)
                $leftNavigation[itemKey]['level1'][pageKey]['childrens'] ||= {}
                  pages['childrens'].each do |level2Key, level2Pages|
                    $leftNavigation[itemKey]['level1'][pageKey]['childrens'][level2Key] ||= {}
                    $leftNavigation[itemKey]['level1'][pageKey]['childrens'][level2Key]['alias'] = level2Pages['own_url']['alias']
                    $leftNavigation[itemKey]['level1'][pageKey]['childrens'][level2Key]['title'] = level2Pages['own_url']['title']
                  end  
                buildNavigation(pages['childrens'], itemKey)   
                
               else 
                  # if this is last level page - we will show his parent as first level, and this page as children
                  # we set level0 as parent array, and remove leve1, because we don't need it anymore
                  if (parentSection != '' && pageKey == k)           
                    $leftNavigation[itemKey]['level0'] ||= {}
                    $leftNavigation[itemKey]['level0'] = $leftNavigation[parentSection]['level1']
                    $leftNavigation[itemKey].delete('level1')
                    break;
                  end
              end
            end #navhash pages loop  
        end 
       end  #navhash arr loop  
    end #func
    
    
   end #class
end