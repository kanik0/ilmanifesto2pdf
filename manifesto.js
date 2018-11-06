var feedURL = "https://ilmanifesto.it/feed/";
var apikey = "your_rss2json.com_api_key_here";

function get_path(url){
    var content = new URL(url);
    parsed = content.pathname;
    return parsed.replace("/","").replace("/","");
}

function get_code(url){
    var content = new URL(url);
    parsed = content.search;
    return parsed.substring(3);
}

function link2pdf(url){
    $.ajax({
      type: 'GET',
      url: "https://api.rss2json.com/v1/api.json?rss_url=" + feedURL + "&api_key=" + apikey + "&count=50",
      dataType: 'jsonp',
      success: function(temp1) {
        var target = get_path(url);
        for (var i=0; i<temp1.items.length; i++){
            if (target == get_path(temp1.items[i].link)){
                var target_code = get_code(temp1.items[i].guid);
                result = 'https://ilmanifesto.it/read-offline/' + target_code + '/' + target + '/pdf/';
            }
        }
        alert(result);
      }
    });

}
