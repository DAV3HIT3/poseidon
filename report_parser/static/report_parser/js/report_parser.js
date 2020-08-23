
function parseReport(report_data){
  require(['nearley', '/static/report_parser/js/grammar-base-compiled.js'], function (){

    // Create the parser with our compiled grammar
    const parser = new nearley.Parser(nearley.Grammar.fromCompiled(window.grammar));

    try{
      // Feed the parser the report text
      parser.feed(report_data);
      //console.log(parser.results[0]);
    } catch(err){
      alert("Error parsing report! " + err);
      console.log("Error parsing report: " + err);
    }
    // Convert the parsed JSON into a string then add to the hidden json_data
    // form field.
    $('#id_json_data').text(JSON.stringify(parser.results[0]));
    
  });
}

