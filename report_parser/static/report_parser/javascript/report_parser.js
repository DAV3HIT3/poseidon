//import nearley from "./nearley.js";
const nearley = require("nearley");

//import grammarBasic from "./grammar-base-compiled.js";

function parseReport(report_data){
  console.log("In parseReport!");
  try{
    setTimeout(() => {
      const parser = new nearley.Parser(nearley.Grammar.fromCompiled(grammarBasic));
      parser.feed(report_data);

      console.log("RESULTS:",parser.results);

      // apply specific parser to each row...
      //
      // case "REGIONS"
      //
      // case "EVENTS"
    },100);
  }catch(erro){
    console.log("Can't parse report:", err);
    reject(err);
  }
}

