
function parseReport(report_data){
  //console.log("parseReport( " + report_data + " )");

  require(['nearley', '/static/report_parser/js/grammar-base-compiled.js'], function (){
    //console.log("now parsing (" + report_data + " )");

    const parser = new nearley.Parser(nearley.Grammar.fromCompiled(window.grammar));

    //console.log("In parseReport, calling parser(" + report_data + ")");

    try{
      parser.feed(report_data);
      console.log(parser.results);
      $('#id_json_data').val(parser.results);
      return parser.results;
    } catch(err){
      alert("Error parsing report!", err);
      console.log("Error parsing report: ", err);
    }
  });
}

