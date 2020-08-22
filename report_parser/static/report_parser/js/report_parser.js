
function parseReport(report_data){
  //console.log("parseReport( " + report_data + " )");

  var json_data = null;
  
  require(['nearley', '/static/report_parser/js/grammar-base-compiled.js'], function (){
    //console.log("now parsing (" + report_data + " )");

    const parser = new nearley.Parser(nearley.Grammar.fromCompiled(window.grammar));

    //console.log("In parseReport, calling parser(" + report_data + ")");

    try{
      parser.feed(report_data);
      //console.log(parser.results);
      json_data = parser.results;
    } catch(err){
      alert("Error parsing report!", err);
      console.log("Error parsing report: ", err);
    }
  });

  return json_data;
}

