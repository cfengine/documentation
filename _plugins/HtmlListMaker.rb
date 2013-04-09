  # This class is used to generate html or haml list (<ul><li>) from hash
  class ListMaker
    def initialize(hash)
      @hash = hash
      @indent = "  "
      @level = 0
      @out = []
    end

    def append(tag,value=nil)
      str = @indent * @level + "#{tag}"
      str += @tag_space + value unless value.nil?
      str += "\n"
      @out << str
    end

    def ul(hash)
      open_tag('ul') { li(hash) }
    end

    def li(hash)
      @level += 1

      hash.each do |key,value|


  	# pages without children has type key, so this is the "last" stop, and we don't have to recursively look inside that page

        if (value.has_key?('childrens') == true)
           open_tag('li', key, value['own_url']) { ul(value['childrens']) if value.is_a?(Hash)&&value['childrens'].length>0}

        elsif (value.has_key?('type') == false)
          # create list with subnodes
          open_tag('li',key) { ul(value) if value.is_a?(Hash) }
        else
           # create list for a single page
           open_tag('li',key, value)
        end
      end
      @level -= 1
    end

    def list
      ul(@hash)
      @out.join
    end
  end

  class HtmlListMaker < ListMaker
    def initialize(hash)
      super
      @tag_space = ""
    end

    def open_tag(tag, value=nil, data=nil, &block)
   	  if data == nil
      	append("<#{tag}>",value)
      else
      	append("<#{tag}>", '<a href="' + data['alias'] + '">' + data['title'] + "</a>")
      end
      yield if block_given?
      append("</#{tag}>")
    end
  end

  class HamlListMaker < ListMaker
    def initialize(hash)
      super
      @tag_space = " "
    end

    def open_tag(tag,value=nil,&block)
      append("%#{tag}",value)
      yield if block_given?
    end
  end
