module Jekyll

  module CfeLiquidUtils
    
    $CfeUtils = CFE::CfeUtils.new
    
    def removeUnvantedChars(input)
      return $CfeUtils.removeUnvantedChars(input)
    end
  end  
end
Liquid::Template.register_filter Jekyll::CfeLiquidUtils