@{%
  
  const noop = () => null;

  const filterEmpty = (d) => {
    return d.filter((val) => {
      if (val == null) {
        return false;
      }
      if (Array.isArray(val) && val.length === 0) {
        return false;
      }
      return true;
    });
  }

  const array2String = (d) => {
    if (!Array.isArray(d)) {
      return d;
    }
    return d.reduce((result, val) => {
      if (Array.isArray(val)) {
        val = array2String(val);
      }
      if (val == null) {
        val = "";
      }
      result += val;
      return result;
    }, "");
  }

  const parseRegionCoordinates = (d) => {
    return {
      x: d[1],
      y: d[3],
      z: d[4].z,
      toString() {
        let title = d.slice();
        title[4] = title[4].title;
        return array2String(title);
      }
    };
  };

  const parseUnitName = (d) => {
    return {
      type: "UNIT_NAME",
      unitName: array2String(d[0]),
      unitId: d[3]
    };
  }
%}


# New line - send to noop processor, which 
NL ->
  [\n] {% noop %}

# One or more new lines
NL_ ->
  NL:+

# One or more Integers
INT ->
  [0-9]:+ {% (d) => parseInt(d[0].join("")) %}


# Simple single 'space'
_ ->
  [ ] {% id %}

# One or more 'space'
__ ->
  _:+ {% id %}

# 'space' and 'new line'
__AND_NL ->
  [ \n]:+ {% id %}

# One or more words followed by "." or "!"
SENTENCE ->
  WORD [.!]
  | WORD __ SENTENCE {% array2String %}
  | WORD NL __ SENTENCE {% array2String %}


TEXT ->
  WORD
  | WORD __ TEXT {% array2String %}
  | WORD NL __ TEXT {% array2String %}

# One or more words with no symbols "," "." or "!"
TEXT_NO_SYMBOLS ->
  WORD_NO_SYMBOLS
  | WORD_NO_SYMBOLS __ TEXT_NO_SYMBOLS {% array2String %}
  | WORD_NO_SYMBOLS NL __ TEXT_NO_SYMBOLS {% array2String %}

# One or more words (no new lines)
WORDS ->
  WORD
  | WORD __ WORDS {% array2String %}


# Word is one or more characters that is not "new line" or "carrige return", or "space"
WORD ->
  [^\n\r ]:+ {% array2String %}

# Word minus symbols "," "." "!"
WORD_NO_SYMBOLS ->
  [^\n\r,.! ]:+ {% array2String %}


BLOB ->
  [^\n\r]:+ {% array2String %}


REGION_COORDINATES ->
  "(" INT "," INT REGION_Z_LEVEL ")" {% parseRegionCoordinates  %}


LC_WORDS ->
  LC_WORD
  | LC_WORD __ LC_WORDS


LC_WORD ->
  [a-z\-]:+

# Unit name is pair "Unit name" (Unit ID)
#UNIT_NAME ->
#  [^():;]:+ __ "(" INT ")" {% parseUnitName %}


REGION_Z_LEVEL ->
  ",nexus" {% (d) => ({ title: d[0], z: 0 }) %}
  | null {% (d) => ({ title: "", z: 1 }) %}

  #Underworld
  | ",underworld" {% (d) => ({ title: d[0], z: 2 }) %}
  | "," INT NL:? _ "<underworld>" {% (d) => ({ title: array2String(d), z: parseInt(String(2) + String(d[1]), 10)}) %}

  #Underdeep
  | ",underdeep" {% (d) => ({ title: d[0], z: 3 }) %}
  | "," INT NL:? _ "<underdeep>" {% (d) => ({ title: array2String(d), z: parseInt(String(3) + String(d[1]), 10)}) %}

  #Abyss
  | ",abyss" {% (d) => ({ title: d[0], z: 4 }) %}
  | "," INT NL:? _ "<abyss>" {% (d) => ({ title: array2String(d), z: parseInt(String(4) + String(d[1]), 10)}) %}
