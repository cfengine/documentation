module Jekyll
  class CfeUtils
    
    #produce proper key for hashes    
    def removeUnvantedChars(string)
      tmp_str = string.downcase.gsub(/[^a-z0-9\-_]+/i, "-")
      return tmp_str
    end  
        
  end
end  